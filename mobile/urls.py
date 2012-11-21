# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from views import home, LocationDetailView, LocationTypeListView, LocationTypeDetailView, NavigateView


urlpatterns = patterns(
    '',

    url(r'^$', home, name='mobile_home'),
    url(r'^type/$', LocationTypeListView.as_view(), name='mobile-type'),
    url(r'^type/(?P<pk>\d+)/$', LocationTypeDetailView.as_view(), name='mobile-type-detail'),
    url(r'^location/(?P<slug>[-\w]+)/$', LocationDetailView.as_view(), name='mobile-location-detail'),
    url(r'^(?P<path>[0-9A-Za-z-_.//]+)/$', NavigateView.as_view(), name='mobile-navigate'),
)
