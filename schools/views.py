from .models import School
from vendors.models import InventoryRecord, NegotiatedPrice
from curricula.models import GradeCurriculum
from students.models import Grade, Cohort
from django.views.generic import ListView
import simplejson as json


class SchoolCurriculaMatch(ListView):

    context_object_name = "book_inventory"
    template_name = "school_curricula_match.html"

    def get_queryset(self):
        self.school = School.objects.get(school_code=self.kwargs['id'])
        each_book = InventoryRecord.objects.filter(school=self.school).prefetch_related('material__publisher__group')
        return each_book

    def get_context_data(self, **kwargs):
        context = super(SchoolCurriculaMatch, self).get_context_data(**kwargs)
        all_books = context['book_inventory']
        matched_books = {}
        unmatched_books = {}
        matched_curricula = {}
        for book in all_books:
            match_list = book.material.curricula.all()
            title = book.material.title
            isbn = book.material.isbn
            teacher_edition = book.material.isTeacherEdition
            publisher = book.material.publisher
            material_type = book.material.material_type
            total_book_count = 0
            total_book_count = total_book_count + book.qty_onsite + book.qty_to_student_home + book.qty_to_student_class + book.qty_lost_stolen + book.qty_unusable
            book_count_list = [book.qty_onsite, book.qty_to_student_home, book.qty_to_student_class, book.qty_lost_stolen, book.qty_unusable]
            if match_list:
                for match in match_list:
                    curricula_set = (match.curriculum.name, str(match.grade_level_start) + ' to ' + str(match.grade_level_end), match.curriculum.subject_area, match.curriculum.publisher, match.pk)
                try:
                    matched_curricula[curricula_set] = total_book_count + matched_curricula[curricula_set]
                except KeyError:
                    matched_curricula[curricula_set] = total_book_count
                matched_books[isbn] = {'matches': match_list, 'title': title, 'teacher_edition': teacher_edition, 'material_type': material_type, 'publisher': publisher, 'book_count': book_count_list}
            else:
                unmatched_books[isbn] = {'title': title, 'teacher_edition': teacher_edition, 'material_type': material_type, 'publisher': publisher, 'book_count': book_count_list}
        context['matched_books'] = matched_books
        context['unmatched_books'] = unmatched_books
        context['school'] = self.school
        context['matched_curricula'] = matched_curricula
        return context


class SchoolInventory(ListView):

    context_object_name = "book_inventory"
    template_name = "school_inventory.html"

    def get_queryset(self):
        self.school = School.objects.get(school_code=self.kwargs['id'])
        each_book = InventoryRecord.objects.filter(school=self.school).prefetch_related('material__publisher__group').order_by('material')
        return each_book

    def get_context_data(self, **kwargs):
        context = super(SchoolInventory, self).get_context_data(**kwargs)
        context['school'] = self.school
        return context


class SchoolDetailView(ListView):

    context_object_name = "book_inventory"
    template_name = "school.html"

    def get_queryset(self):
        self.school = School.objects.get(school_code=self.kwargs['id'])
        each_book = InventoryRecord.objects.filter(school=self.school)
        return each_book

    def get_context_data(self, **kwargs):
        context = super(SchoolDetailView, self).get_context_data(**kwargs)
        context['school'] = self.school
        return context


class SchoolsListView(ListView):

    context_object_name = "schools"
    template_name = "schools_list.html"
    model = School


class SchoolAggregateView(ListView):

    context_object_name = "curricula"
    template_name = "school_aggregate.html"

    def get_queryset(self):
        self.school = School.objects.get(school_code=self.kwargs['id'])
        all_books = InventoryRecord.objects.select_related('material').filter(school=self.school)
        return all_books

    def enough_books(self, number_of_books, students_in_grade):
        if number_of_books >= students_in_grade:
            return('True')
        else:
            return('False')

    def get_materials_for_grade_curriculum(self, students_in_grade, array_name, all_books, grade_curriculum_id):
        self.book_list[array_name] = []
        required_books = GradeCurriculum.objects.get(id=grade_curriculum_id).materials  # place .materials with .necessary_materials to get only necessary material when this data has been added
        for material in required_books.all():
            if all_books.filter(material=material).exists():
                number_of_books = all_books.filter(material=material)[0].get_inventory_total()
            else:
                number_of_books = 0
            enough_books = self.enough_books(number_of_books, number_of_books)
            cost_of_book = NegotiatedPrice.objects.filter(material=material)[0].value
            self.book_list[array_name].append(
                {
                    'title': material.title,
                    'total copies': number_of_books,
                    'needed': students_in_grade,
                    'cost': float(cost_of_book),
                    'enough': enough_books,
                    'difference': abs(students_in_grade - number_of_books),
                })
            if (students_in_grade - number_of_books) >= 0:
                self.total_cost += (students_in_grade - number_of_books) * cost_of_book
            else:
                self.total_cost += 0

    def get_context_data(self, **kwargs):
        context = super(SchoolAggregateView, self).get_context_data(**kwargs)
        self.total_cost = 0
        context['school'] = self.school
        grade = Grade.objects.get(school=self.school, grade_level=5)
        cohort = Cohort.objects.filter(grade=grade)
        students_in_grade = cohort.get(grade=grade, year_end=2013).number_of_students
        self.book_list = {}
        self.get_materials_for_grade_curriculum(students_in_grade, 'reading', context['curricula'], 38)
        self.get_materials_for_grade_curriculum(students_in_grade, 'mathematics', context['curricula'], 30)
        context['book_list'] = self.book_list
        context['outtwo'] = json.dumps([obj for obj in cohort.values()])
        return context
