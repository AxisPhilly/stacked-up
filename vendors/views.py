from vendors.models import InventoryRecord
from schools.models import School
from curricula.models import GradeCurriculum, LearningMaterial
from django.views.generic import ListView, DetailView


class VendorListView(ListView):

    context_object_name = "book_inventory"
    template_name = "school.html"

    def get_queryset(self):
        self.school = School.objects.get(school_id=self.kwargs['id'])
        self.each_book = InventoryRecord.objects.filter(school=self.school).order_by('-qty_onsite', 'material')
        return self.each_book

    def get_context_data(self, **kwargs):

        all_books = self.get_queryset()
        a = {}
        for x in all_books:
            a[str(x.material.isbn)] = {}
            a[str(x.material.isbn)]["title"] = x.material.title.encode("utf-8")
            a[str(x.material.isbn)]["teacher"] = str(x.material.isTeacherEdition)
            a[str(x.material.isbn)]["publisher"] = [str(x.material.publisher.name), str(x.material.publisher.group), str(x.material.publisher.pk)]
            a[str(x.material.isbn)]["material"] = str(x.material.material_type)
            r = LearningMaterial.objects.get(isbn=str(x.material.isbn))
            v = InventoryRecord.objects.filter(school=self.school, material=r)
            d = 0
            qty_to_student_home = 0
            qty_to_student_class = 0
            qty_lost_stolen = 0
            qty_onsite = 0
            qty_unusable = 0
            for z in v:
                d = d + z.qty_onsite + z.qty_to_student_home + z.qty_to_student_class + z.qty_lost_stolen + z.qty_unusable
                qty_onsite += z.qty_onsite
                qty_to_student_home += z.qty_to_student_home
                qty_to_student_class += z.qty_to_student_class
                qty_lost_stolen += z.qty_lost_stolen
                qty_unusable += z.qty_unusable
                book_count_list = [qty_onsite, qty_to_student_home, qty_to_student_class, qty_lost_stolen, qty_unusable]
            a[str(x.material.isbn)]["total"] = d
            a[str(x.material.isbn)]["book_count_list"] = book_count_list
            s = r.curricula.all()
            t = []
            for u in s:
                t.append(str(u.curriculum.name))
                t.append(str(u.curriculum.subject_area))
                t.append(str(u.grade_level_start))
                t.append(str(u.grade_level_end))
                t.append(str(u.curriculum.publisher))
                t.append(str(u.id))
                a[str(x.material.isbn)]["curricula"] = t
        context = super(VendorListView, self).get_context_data(**kwargs)
        x = a
        a = {}
        unmatched = {}
        matched = {}
        for key in x:
            if set(['curricula']).issubset(x[key]):
                curricula = x[key]['curricula']
                curricula_title = curricula[0]
                curricula_subject = curricula[1]
                curricula_publisher = curricula[4]
                curricula_id = curricula[5]
                curricula_grade = ""
                for g in range(0, len(curricula)/6):
                    curricula_grade = curricula_grade + curricula[6 * g + 2] + " to " + curricula[6 * g + 3] + ", "
                curricula_grade = curricula_grade[:-2]
                count = x[key]['total']
                title = x[key]['title']
                book_count_list = x[key]['book_count_list']
                curriculum_set = (curricula_title, curricula_grade, curricula_subject, curricula_publisher, curricula_id)
                try:
                    a[curriculum_set] = count + a[curriculum_set]
                except KeyError:
                    a[curriculum_set] = count

                isbn = key
                publisher = x[key]['publisher']
                teacher = x[key]['teacher']
                material_type = x[key]['material']
                matched[isbn] = [count, title, publisher, book_count_list, teacher, material_type]
            else:
                count = x[key]['total']
                title = x[key]['title']
                publisher = x[key]['publisher']
                book_count_list = x[key]['book_count_list']
                teacher = x[key]['teacher']
                material_type = x[key]['material']
                isbn = key
                unmatched[isbn] = [count, title, publisher, book_count_list, teacher, material_type]
        context['matched_books'] = matched
        context['unmatched_books'] = unmatched
        context['school'] = self.school
        context['matched_curricula'] = a
        context['returned'] = a
        return context


class MatchWithCurriculum(ListView):

    context_object_name = "book_detail"
    template_name = "match.html"

    def get_queryset(self):
        self.school = LearningMaterial.objects.get(isbn=self.kwargs['id'])
        return self.school

    def get_context_data(self, **kwargs):
        context = super(MatchWithCurriculum, self).get_context_data(**kwargs)
        context['book_name'] = self.school.title
        self.school = LearningMaterial.objects.get(isbn=self.kwargs['id'])
        context['book_list'] = self.school.curricula.all()
        return context


class CurriculumDetailView(DetailView):

    context_object_name = "curriculum_list"
    template_name = "curriculum.html"
    model = School


class IndexListView(ListView):

    context_object_name = "school_list"
    template_name = "index.html"
    model = School
