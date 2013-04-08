# from vendors.models import InventoryRecord
# from schools.models import School
# from curricula.models import GradeCurriculum, LearningMaterial
# from django.views.generic import ListView


# class SchoolDetailView(ListView):

#     context_object_name = "book_inventory"
#     template_name = "school.html"

#     def get_queryset(self):
#         self.school = School.objects.get(school_id=self.kwargs['id'])
#         self.each_book = InventoryRecord.objects.filter(school=self.school).order_by('-qty_onsite', 'material')
#         return self.each_book

#     def get_context_data(self, **kwargs):
#         context = super(SchoolDetailView, self).get_context_data(**kwargs)
#         all_books = self.get_queryset()
#         matched_books = {}
#         unmatched_books = {}
#         matched_curricula = {}
#         for book in all_books:
#             match_list = book.material.curricula.all()
#             title = book.material.title.encode("utf-8")
#             isbn = book.material.isbn.encode("utf-8")
#             teacher_edition = str(book.material.isTeacherEdition)
#             publisher = book.material.publisher
#             material_type = book.material.material_type
#             total_book_count = 0
#             total_book_count = total_book_count + book.qty_onsite + book.qty_to_student_home + book.qty_to_student_class + book.qty_lost_stolen + book.qty_unusable
#             book_count_list = [book.qty_onsite, book.qty_to_student_home, book.qty_to_student_class, book.qty_lost_stolen, book.qty_unusable]
#             if match_list:
#                 for match in match_list:
#                     curricula_set = (match.curriculum.name, str(match.grade_level_start) + ' to ' + str(match.grade_level_end), match.curriculum.subject_area, match.curriculum.publisher, match.pk)
#                 try:
#                     matched_curricula[curricula_set] = total_book_count + matched_curricula[curricula_set]
#                 except KeyError:
#                     matched_curricula[curricula_set] = total_book_count
#                 matched_books[isbn] = {'matches': match_list, 'title': title, 'teacher_edition': teacher_edition, 'material_type': material_type, 'publisher': publisher, 'book_count': book_count_list}
#             else:
#                 unmatched_books[isbn] = {'title': title, 'teacher_edition': teacher_edition, 'material_type': material_type, 'publisher': publisher, 'book_count': book_count_list}
#         context['matched_books'] = matched_books
#         context['unmatched_books'] = unmatched_books
#         context['school'] = self.school
#         context['matched_curricula'] = matched_curricula
#         return context


# class LearningMaterialDetailView(ListView):

#     context_object_name = "learning_material_detail"
#     template_name = "match.html"

#     def get_queryset(self):
#             self.school = LearningMaterial.objects.get(isbn=self.kwargs['id'])
#             return self.school

#     def get_context_data(self, **kwargs):
#         context = super(LearningMaterialDetailView, self).get_context_data(**kwargs)
#         context['book_name'] = self.school.title
#         self.school = LearningMaterial.objects.get(isbn=self.kwargs['id'])
#         context['book_list'] = self.school.curricula.all()
#         return context


# class CurriculumDetailView(ListView):

#     context_object_name = "curriculum_list"
#     template_name = "curriculum.html"

#     def get_queryset(self):
#         self.curriculum = GradeCurriculum.objects.get(id=self.kwargs['id'])
#         return self.curriculum

#     def get_context_data(self, **kwargs):
#         context = super(CurriculumDetailView, self).get_context_data(**kwargs)
#         return context


# class CurriculumListView(ListView):

#     context_object_name = "curricula"
#     template_name = "curricula.html"
#     model = GradeCurriculum


# class SchoolsListView(ListView):

#     context_object_name = "schools"
#     template_name = "schools_list.html"
#     model = School
