from vendors.models import InventoryRecord
from schools.models import School
from curricula.models import GradeCurriculum, LearningMaterial
from django.views.generic import ListView
from django.shortcuts import get_object_or_404


class VendorListView(ListView):

    context_object_name = "book_inventory"
    template_name = "school.html"

    def get_queryset(self):
        self.s = School.objects.get(school_id=self.kwargs['id'])
        self.each_book = InventoryRecord.objects.filter(school=self.s).order_by('-qty_onsite', 'material')
        return self.each_book

    def get_context_data(self, **kwargs):

        all_books = self.get_queryset()
        a = {}
        for x in all_books:
            a[str(x.material.isbn)] = {}
            a[str(x.material.isbn)]["title"] = x.material.title.encode("utf-8")
            a[str(x.material.isbn)]["teacher"] = str(x.material.isTeacherEdition)
            r = LearningMaterial.objects.get(isbn=str(x.material.isbn))
            d = 0
            v = InventoryRecord.objects.filter(school=self.s, material=r)
            for z in v:
                d = d + z.qty_onsite + z.qty_to_student_home + z.qty_to_student_class + z.qty_lost_stolen
            a[str(x.material.isbn)]["total"] = d
            s = r.curricula.all()
            t = []
            count = 0
            for u in s:
                count += 1
                t.append(str(u.curriculum.name))
                t.append(str(u.curriculum.subject_area))
                t.append(str(u.grade_level_start))
                t.append(str(u.grade_level_end))
                a[str(x.material.isbn)]["curricula"] = t
        context = super(VendorListView, self).get_context_data(**kwargs)
        x = a
        a = {}
        for key in x:
            if set(['curricula']).issubset(x[key]):
                curricula = x[key]['curricula']
                print curricula
                print len(curricula)
                curricula_title = curricula[0]
                curricula_grade = ""
                for g in range(0, len(curricula)/4):
                    curricula_grade = curricula_grade + curricula[4 * g + 2] + " to " + curricula[4 * g + 3] + ", "
                curricula_grade = curricula_grade[:-2]
                total = x[key]['total']
                key = (curricula_title, curricula_grade)
                if key in a:
                    a[key] = a[key] + total
                else:
                    a[key] = total
            html = ""
            for key, value in sorted(a.iteritems(), key=lambda (k,v): (v,k), reverse=True):
                html += '<div class="section row"><div class="twelve columns mobile-full"><div class="number"><h4>'+str(value)+'</h4></div><div class="curriculum">'+str(key)+'</div></div></div>' # I'm sorry this is terrible I will fix it.

        context['returner'] = html
        context['school_name'] = self.s.name
        context['grade_start'] = self.s.grade_start
        context['grade_end'] = self.s.grade_end
        return context


class MatchWithCurriculum(ListView):

    context_object_name = "book_list"
    template_name = "match.html"

    def get_queryset(self):
        self.s = LearningMaterial.objects.get(isbn=self.kwargs['id'])
        return self.s.curricula.all()

    def get_context_data(self, **kwargs):
        context = super(MatchWithCurriculum, self).get_context_data(**kwargs)
        context['school_name'] = self.s.title
        return context


class IndexListView(ListView):

    context_object_name = "school_list"
    template_name = "index.html"

    def get_queryset(self):
        self.s = School.objects.all()
        return self.s

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        return context
