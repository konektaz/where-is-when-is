from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'core.views.home', name='home'),
    url(r'^about/$', 'core.views.about', name='about'),

    url(r'^feedback/$', 'core.views.feedback', name='feedback'),

    url(r'^mobile/', include('mobile.urls')),

    url(r'', include('world.urls')),
)
