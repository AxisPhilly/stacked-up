from django.conf.urls import patterns, url
from .views import SchoolsListView, SchoolTest

urlpatterns = patterns('',
    url(r'^$',
        SchoolsListView.as_view()),
    url(r'^test/(?P<id>(.+))/$',
        SchoolTest.as_view()),
)
