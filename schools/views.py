from .models import School
from vendors.models import InventoryRecord
from curricula.models import GradeCurriculum
from django.views.generic import ListView
import simplejson as json

class SchoolCurriculaMatch(ListView):

    context_object_name = "book_inventory"
    template_name = "analysis/school_curricula_match.html"

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
    template_name = "analysis/school_inventory.html"

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
    template_name = "analysis/school.html"

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
    template_name = "analysis/schools_list.html"
    model = School


class SchoolTest(ListView):

    context_object_name = "curricula"
    template_name = "school_test.html"

    def get_queryset(self):
        self.school = School.objects.get(school_code=self.kwargs['id'])
        all_books = InventoryRecord.objects.select_related('material').filter(school=self.school)
        return all_books

    def get_materials_for_grade_curriculum(self, grade_curriculum, array_name):
        self.book_list[array_name] = []
        for material in grade_curriculum.all():
            self.book_list[array_name].append(
                {
                    'title': material.title,
                    'isbn': material.isbn,
                })

    def get_context_data(self, **kwargs):
        context = super(SchoolTest, self).get_context_data(**kwargs)
        context['school'] = self.school.name
        context['grade_start'] = self.school.grade_start
        context['grade_end'] = self.school.grade_end
        context['curricula_in_use'] = self.school.curricula_in_use
        self.book_list = {}
        self.book_list['all_books'] = []
        gc = GradeCurriculum.objects.filter(id=86)[0].necessary_materials
        self.get_materials_for_grade_curriculum(gc, 'reading_books')
        self.get_materials_for_grade_curriculum(gc, 'mathematics_books')
        for material in context['curricula']:
            self.book_list['all_books'].append(
                {
                    'title': material.material.title,
                    'isbn': material.material.isbn,
                    'quantity': material.get_inventory_total(),
                })
        context['book_list'] = json.dumps(self.book_list)
        return context
