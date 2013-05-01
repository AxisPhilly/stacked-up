from django.conf.urls import patterns, url
from .views import SchoolsListView, SchoolAggregateView

urlpatterns = patterns('',
    url(r'^$',
        SchoolsListView.as_view()),
    url(r'^(?P<id>(.+))/(?P<grade>(.+))/$',
        SchoolAggregateView.as_view()),
    url(r'^(?P<id>(.+))/$',
        SchoolAggregateView.as_view()),
)
