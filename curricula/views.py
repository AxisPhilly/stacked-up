from curricula.models import GradeCurriculum, LearningMaterial
from django.views.generic import ListView


class LearningMaterialDetailView(ListView):

    context_object_name = "learning_material_detail"
    template_name = "match.html"

    def get_queryset(self):
            self.school = LearningMaterial.objects.get(isbn=self.kwargs['id'])
            return self.school

    def get_context_data(self, **kwargs):
        context = super(LearningMaterialDetailView, self).get_context_data(**kwargs)
        context['book_name'] = self.school.title
        self.school = LearningMaterial.objects.get(isbn=self.kwargs['id'])
        context['book_list'] = self.school.curricula.all()
        return context


class CurriculumDetailView(ListView):

    context_object_name = "curriculum_list"
    template_name = "curriculum.html"

    def get_queryset(self):
        self.curriculum = GradeCurriculum.objects.get(id=self.kwargs['id'])
        return self.curriculum

    def get_context_data(self, **kwargs):
        context = super(CurriculumDetailView, self).get_context_data(**kwargs)
        return context


class CurriculumListView(ListView):

    context_object_name = "curricula"
    template_name = "curricula.html"
    model = GradeCurriculum
