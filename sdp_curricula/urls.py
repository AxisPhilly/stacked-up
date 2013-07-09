from django.conf.urls import patterns, include, url

from curricula.views import LearningMaterialDetailView, GradeCurriculumDetailView, CurriculumListView, AnalysisIndexListView, GradeCurriculumUse
from schools.views import SchoolDetailView, SchoolCurriculaMatch, AnalysisSchoolsListView, AnalysisSchoolInventory
from core.views import IndexListView, SchoolsListView

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
        IndexListView.as_view()),
    url(r'^schools/$',
        SchoolsListView.as_view(),
        name='schools_list'),
    url(r'^siteadmin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'^school/', include('schools.urls'), name='school_listing'),
    url(r'^gradecurriculum/(?P<id>(.+))/$',
        GradeCurriculumUse.as_view()),

    # Analysis views
    url(r'^analysis/$',
        AnalysisIndexListView.as_view()),
    url(r'^analysis/schools/$',
        AnalysisSchoolsListView.as_view()),
    url(r'^analysis/school/match/(?P<id>(.+))/$',
        SchoolCurriculaMatch.as_view()),
    url(r'^analysis/school/inventory/(?P<id>(.+))/$',
        AnalysisSchoolInventory.as_view()),
    url(r'^analysis/school/(?P<id>(.+))/$',
        SchoolDetailView.as_view()),
    url(r'^analysis/curricula/$',
        CurriculumListView.as_view()),
    url(r'^analysis/gradecurriculum/(?P<id>(.+))/$',
        GradeCurriculumDetailView.as_view()),
    url(r'^analysis/learningmaterial/(?P<id>(.+))/$',
        LearningMaterialDetailView.as_view()),
)
