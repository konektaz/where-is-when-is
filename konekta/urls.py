from django.conf.urls import patterns, include, url
from django.contrib import admin

from world.api import LocationResource


admin.autodiscover()

location_resource = LocationResource()


urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'core.views.home', name='home'),
    url(r'^about/$', 'core.views.about', name='about'),

    url(r'^feedback/$', 'core.views.feedback', name='feedback'),

    url(r'^mobile/', include('mobile.urls')),

    (r'^api/', include(location_resource.urls)),

    url(r'', include('world.urls')),
)
