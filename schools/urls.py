from django.conf.urls import patterns, url
from .views import SchoolAggregateView, SchoolInventory

urlpatterns = patterns('',
    url(r'^inventory/(?P<id>(.+))/$',
        SchoolInventory.as_view()),
    url(r'^(?P<id>(.+))/(?P<grade>(.+))/$',
        SchoolAggregateView.as_view()),
    url(r'^(?P<id>(.+))/$',
        SchoolAggregateView.as_view()),
)
