from django.conf.urls import patterns, include, url
from vendors.views import VendorListView, MatchWithCurriculum, IndexListView
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
    url(r'^school/(?P<id>(.+))/$',
        VendorListView.as_view()),
    url(r'^book/(?P<id>(.+))/$',
        MatchWithCurriculum.as_view()),
)
