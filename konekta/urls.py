from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'konekta.views.home', name='home'),
    # url(r'^konekta/', include('konekta.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
