from django.conf.urls.defaults import *
from tastypie.api import Api
from .api import *

v1_api = Api(api_name='')
v1_api.register(CurriculaResource())
v1_api.register(InventoryRecordResource())
v1_api.register(SchoolResource())
v1_api.register(LearningMaterialResource())
v1_api.register(GradeCurriculaResource())
v1_api.register(SchoolResource())
v1_api.register(SchoolCurriculaResource())

urlpatterns = patterns('', (r'^v1', include(v1_api.urls)))
