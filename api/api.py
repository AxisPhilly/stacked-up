from tastypie.resources import ModelResource
from curricula import models as curricula
from vendors import models as inventory
from schools.models import School
from curricula.models import LearningMaterial
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


class SchoolResource(ModelResource):
    curricula_in_use = fields.ManyToManyField(CurriculaResource, 'curricula_in_use', full=True)

    class Meta:
        queryset = School.objects.all()
        resource_name = 'schools'
        always_return_data = True
        allowed_methods = ['get']
        filtering = {
            'name': ('exact'),
            'id': ('exact')
        }

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
