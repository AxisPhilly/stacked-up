from tastypie.resources import ModelResource
from curricula import models as curricula


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

    def determine_format(self, request):
            return 'application/json'
