from django.conf.urls import patterns, include, url
from curricula.views import LearningMaterialDetailView, CurriculumDetailView, CurriculumListView
from schools.views import SchoolDetailView, SchoolsListView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sdp_curricula.views.home', name='home'),
    # url(r'^sdp_curricula/', include('sdp_curricula.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^$',
    #     IndexListView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^schools/$',
        SchoolsListView.as_view()),
    url(r'^school/(?P<id>(.+))/$',
        SchoolDetailView.as_view()),
    url(r'^curricula/$',
        CurriculumListView.as_view()),
    url(r'^curriculum/(?P<id>(.+))/$',
        CurriculumDetailView.as_view()),
    url(r'^learningmaterial/(?P<id>(.+))/$',
        LearningMaterialDetailView.as_view()),
)
