from .models import GradeCurriculum, LearningMaterial
from django.views.generic import TemplateView, ListView
from vendors.models import InventoryRecord
from schools.models import School


class LearningMaterialDetailView(ListView):

    context_object_name = "learning_material_detail"
    template_name = "analysis/learning_material_detail.html"

    def get_queryset(self):
            self.learning_material = LearningMaterial.objects.get(isbn=self.kwargs['id'])
            return self.learning_material

    def get_context_data(self, **kwargs):
        context = super(LearningMaterialDetailView, self).get_context_data(**kwargs)
        context['book_name'] = self.learning_material.title
        context['book_list'] = self.learning_material.curricula.all()
        return context


class GradeCurriculumDetailView(ListView):

    context_object_name = "curriculum_list"
    template_name = "analysis/curriculum.html"

    def get_queryset(self):
        self.curriculum = GradeCurriculum.objects.get(id=self.kwargs['id'])
        return self.curriculum

    def get_context_data(self, **kwargs):
        context = super(GradeCurriculumDetailView, self).get_context_data(**kwargs)
        return context


class CurriculumListView(ListView):

    context_object_name = "curricula"
    template_name = "analysis/curricula.html"
    model = GradeCurriculum


class AnalysisIndexListView(TemplateView):

    template_name = "analysis/index.html"


class GradeCurriculumUse(ListView):

    context_object_name = "curriculum_list"
    template_name = "curriculum.html"

    def get_queryset(self):
        self.curriculum = GradeCurriculum.objects.get(id=self.kwargs['id'])
        return self.curriculum

    def get_context_data(self, **kwargs):
        context = super(GradeCurriculumUse, self).get_context_data(**kwargs)
        material_list = context['curriculum_list'].materials
        output = {}
        for material in material_list.all().iterator():
            output[material.title] = {
                'title': material.title,
                'number_schools': 0,
                'number_books': 0
            }
            for school in School.objects.all()[0:10]:
                try:
                    a = InventoryRecord.objects.select_related('material_id').select_related('school_id').get(school=school, material=material)
                    output[material.title]['number_schools'] += 1
                    output[material.title]['number_books'] += (a.qty_onsite + a.qty_to_student_home + a.qty_to_student_class)
                except:
                    print 1
        context['output'] = output
        return context
