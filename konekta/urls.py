from django.conf.urls import patterns, include, url
from django.contrib import admin

from apiv1.api import Api
from apiv1.resources import AreaResource, LocationResource


admin.autodiscover()

v1_api = Api()
v1_api.register(AreaResource())
v1_api.register(LocationResource())

urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'core.views.home', name='home'),
    url(r'^about/$', 'core.views.about', name='about'),
    url(r'^feedback/$', 'core.views.feedback', name='feedback'),
    url(r'^mobile/', include('mobile.urls')),
    (r'^accounts/', include('allauth.urls')),
    url(r'^api/', include(v1_api.urls)),
    url(r'', include('world.urls')),
)
