from tastypie.resources import ModelResource
from curricula import models as curricula
from vendors import models as inventory
from vendors.models import InventoryRecord, NegotiatedPrice
from schools.models import School
from curricula.models import LearningMaterial, GradeCurriculum
from students.models import Grade, Cohort
import simplejson as json
from tastypie import fields


class CurriculaResource(ModelResource):
    class Meta:
        queryset = curricula.Curriculum.objects.all()
        resource_name = 'curricula'

    def determine_format(self, request):
            return 'application/json'


class GradeCurriculaResource(ModelResource):
    class Meta:
        queryset = curricula.GradeCurriculum.objects.all()
        resource_name = 'grade_curricula'
        always_return_data = True
        filtering = {
            'name': ('exact'),
            'id': ('exact')
        }

    def determine_format(self, request):
            return 'application/json'


class SchoolCurriculaResource(ModelResource):

    class Meta:
        queryset = School.objects.all()
        resource_name = 'school_curricula'
        allowed_methods = ['get']

    # Functions to help assemble cirriculum data for school and grade
    # Taken from curricula.views#SchoolAggregateView
    context = {}

    def is_enough_books(self, number_of_books, students_in_grade):
        if number_of_books >= students_in_grade:
            return('True')
        else:
            return('False')

    def get_materials_for_grade_curriculum(self, students_in_grade, subject,
                                           all_books, cohort, grade_curriculum_id, grade_curriculum_name):
        self.context['curriculum_list'][subject]['curricula'][grade_curriculum_name] = {
            'necessary_material': {},
            'cost_shortfall': 0,
            'book_shortfall': 0
        }
        grade_curriculum = GradeCurriculum.objects.get(id=grade_curriculum_id)
        self.context['curriculum_list'][subject]['curricula'][grade_curriculum_name]['necessary_material'] = []
        for material in grade_curriculum.necessary_materials.all():
            if all_books.filter(material=material).exists():
                number_of_books = all_books.filter(material=material)[0].get_inventory_total()
                enough_books = self.is_enough_books(number_of_books, students_in_grade)
                cost_of_book = NegotiatedPrice.objects.filter(material=material)[0].value
                difference = number_of_books - students_in_grade
                if (students_in_grade - number_of_books) >= 0:
                    self.context['curriculum_list'][subject]['curricula'][grade_curriculum_name]['cost_shortfall'] += (students_in_grade - number_of_books) * cost_of_book
                else:
                    self.context['curriculum_list'][subject]['curricula'][grade_curriculum_name]['cost_shortfall'] += 0
                if (students_in_grade - number_of_books) >= 0:
                    self.context['curriculum_list'][subject]['curricula'][grade_curriculum_name]['book_shortfall'] += (students_in_grade - number_of_books)
                else:
                    self.context['curriculum_list'][subject]['curricula'][grade_curriculum_name]['book_shortfall'] += 0
            else:
                number_of_books = "N/A"
                difference = "N/A"
                cost_of_book = "N/A"
                enough_books = "N/A"

            self.context['curriculum_list'][subject]['curricula'][grade_curriculum_name]['necessary_material'].append(
                {
                    'title': material.title,
                    'total_copies': number_of_books,
                    'needed': students_in_grade,
                    'cost': cost_of_book,
                    'enough': enough_books,
                    'difference': difference,
                })

    def get_grade_curricula_by_subject(self, students_in_grade, subject, all_books, cohort):
        self.context['curriculum_list'][subject] = {
            'curricula': {}
        }
        if subject == "math":
            for grade_curriculum in cohort.associated_math_curriculum.all():
                self.get_materials_for_grade_curriculum(students_in_grade, 'math', all_books, cohort, grade_curriculum.id, grade_curriculum.curriculum.name)
        if subject == "reading":
            for grade_curriculum in cohort.associated_reading_curriculum.all():
                self.get_materials_for_grade_curriculum(students_in_grade, 'reading', all_books, cohort, grade_curriculum.id, grade_curriculum.curriculum.name)

    def get_school_aggregate(self, school, students_in_grade, grade):
        """
            In this grade, we have x students, x books of the common materials, and x shortfall
        """
        aggregate = {}
        aggregate['students'] = students_in_grade
        aggregate['materials'] = {}
        aggregate['materials']['math'] = grade.math_material_count()
        aggregate['materials']['reading'] = grade.reading_material_count()
        aggregate['material_count'] = (aggregate['materials']['math'] + aggregate['materials']['reading'])
        aggregate['difference'] = aggregate['material_count'] - aggregate['students']
        return aggregate

    def dehydrate(self, bundle):
        self.school = School.objects.get(pk=bundle.obj.pk)
        self.all_books = InventoryRecord.objects.select_related('material').filter(school=self.school)
        self.context = {}

        try:
            grade = bundle.request.GET['grade']
        except KeyError:
            grade = bundle.obj.grade_start

        cohort_set = Cohort.objects.filter(grade=Grade.objects.get(school=bundle.obj.pk, grade_level=grade))
        current_cohort = cohort_set.get(year_end=2013)
        current_grade = Grade.objects.get(school=bundle.obj.pk, grade_level=grade)
        students_in_grade = current_cohort.number_of_students

        self.context['curriculum_list'] = {}
        self.get_grade_curricula_by_subject(students_in_grade, 'reading', self.all_books, current_cohort)
        self.get_grade_curricula_by_subject(students_in_grade, 'math', self.all_books, current_cohort)
        self.context['current_grade'] = current_grade.human_grade()
        self.context['school_aggregate'] = self.get_school_aggregate(self.school, students_in_grade, current_grade)
        self.context['pssa_test_scores'] = json.dumps([obj for obj in cohort_set.values()])
        self.context['school'] = bundle.obj

        bundle.data['cirriculum'] = self.context

        return bundle

    def determine_format(self, request):
        return 'application/json'


class SchoolResource(ModelResource):

    class Meta:
        queryset = School.objects.all()
        resource_name = 'schools'
        allowed_methods = ['get']
        limit = 300
        excludes = [
            'city',
            'grade_end',
            'grade_start',
            'phone',
            'school_level',
            'state',
            'street_addr',
            'website',
            'zipcode'
        ]

    def determine_format(self, request):
        return 'application/json'


class LearningMaterialResource(ModelResource):

    class Meta:
        queryset = LearningMaterial.objects.all()
        resource_name = 'learning_material'
        allowed_methods = ['get']
        fields = ['isbn', 'title']
        always_return_data = True
        filtering = {
            "school": ('exact'),
            "id": ('exact')
        }

    def determine_format(self, request):
            return 'application/json'


class InventoryRecordResource(ModelResource):

    school = fields.ForeignKey(SchoolResource, 'school')
    material = fields.ForeignKey(LearningMaterialResource, 'material', full=True)

    class Meta:
        queryset = inventory.InventoryRecord.objects.select_related('material').all()
        resource_name = 'inventory_record'
        allowed_methods = ['get']
        always_return_data = True
        filtering = {
            "school": ('exact'),
            "id": ('exact')
        }

    def determine_format(self, request):
        return 'application/json'
