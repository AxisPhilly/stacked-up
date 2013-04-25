from tastypie.resources import ModelResource
from curricula import models as curricula
from schools import models as schools


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


class SchoolResource(ModelResource):
    class Meta:
        queryset = schools.School.objects.all()
        resource_name = 'schools'
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

    def determind_format(self, request):
            return 'application/json'
