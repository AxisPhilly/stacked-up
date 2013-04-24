from django.conf.urls import patterns, include, url
from curricula.views import LearningMaterialDetailView, GradeCurriculumDetailView, CurriculumListView, IndexListView
from schools.views import SchoolDetailView, SchoolsListView, SchoolCurriculaMatch, SchoolInventory, SchoolTest
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
    url(r'^admin/', include(admin.site.urls)),
    url(r'^schools/$',
        SchoolsListView.as_view()),
    url(r'^school/match/(?P<id>(.+))/$',
        SchoolCurriculaMatch.as_view()),
    url(r'^school/test/(?P<id>(.+))/$',
        SchoolTest.as_view()),
    url(r'^school/inventory/(?P<id>(.+))/$',
        SchoolInventory.as_view()),
    url(r'^school/(?P<id>(.+))/$',
        SchoolDetailView.as_view()),
    url(r'^curricula/$',
        CurriculumListView.as_view()),
    url(r'^gradecurriculum/(?P<id>(.+))/$',
        GradeCurriculumDetailView.as_view()),
    url(r'^learningmaterial/(?P<id>(.+))/$',
        LearningMaterialDetailView.as_view()),
    url(r'^api/', include('api.urls')),
)
