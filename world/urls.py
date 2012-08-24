# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from views import zone_detail


urlpatterns = patterns(
    '',

    url(r'^zone/(?P<slug>[-\w]+)/$', zone_detail, name='world_zone_detail'),
)
