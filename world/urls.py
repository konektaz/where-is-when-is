# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from views import details, location_detail, LocationAddView, LocationValidateView, global_autocomplete


urlpatterns = patterns(
    '',

    url(r'^location/add/$', LocationAddView.as_view(), name='world_location_add'),
    url(r'^location/(?P<slug>[-\w]+)/$', location_detail, name='world_location_detail'),
    url(r'^location/validate/(?P<slug>[-\w]+)/$', LocationValidateView.as_view(), name='world_location_validate'),

    url(r'^globalautocomplete/$', global_autocomplete, name='global_autocomplete'),

    url(r'^(?P<path>[0-9A-Za-z-_.//]+)/$', details, name='area-details'),
)
