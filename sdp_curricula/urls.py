from django.conf.urls import patterns, include, url

from curricula.views import LearningMaterialDetailView, GradeCurriculumDetailView, CurriculumListView, AnalysisIndexListView
from schools.views import SchoolDetailView, SchoolsListView, SchoolCurriculaMatch, SchoolInventory, SchoolAggregateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sdp_curricula.views.home', name='home'),
    # url(r'^sdp_curricula/', include('sdp_curricula.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$',
        AnalysisIndexListView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'^school/$', include('schools.urls')),

    url(r'^school/test/(?P<id>(.+))/(?P<grade>(.+))/$',
        SchoolAggregateView.as_view()),
    url(r'^school/test/(?P<id>(.+))/$',
        SchoolAggregateView.as_view()),

    # Analysis views
    url(r'^analysis/$',
        AnalysisIndexListView.as_view()),
    url(r'^analysis/schools/$',
        SchoolsListView.as_view()),
    url(r'^analysis/school/match/(?P<id>(.+))/$',
        SchoolCurriculaMatch.as_view()),
    url(r'^analysis/school/inventory/(?P<id>(.+))/$',
        SchoolInventory.as_view()),
    url(r'^analysis/school/(?P<id>(.+))/$',
        SchoolDetailView.as_view()),
    url(r'^analysis/curricula/$',
        CurriculumListView.as_view()),
    url(r'^analysis/gradecurriculum/(?P<id>(.+))/$',
        GradeCurriculumDetailView.as_view()),
    url(r'^analysis/learningmaterial/(?P<id>(.+))/$',
        LearningMaterialDetailView.as_view()),
)
