# -*- coding: utf-8 -*-

from django.contrib.gis import admin
from mptt.admin import MPTTModelAdmin

from models import LocationType, Location, Area


class LocationAdmin(admin.OSMGeoAdmin):
    list_display = ('name',)


class AreaAdmin(MPTTModelAdmin):
    list_display = ('name', 'type', 'path')


admin.site.register(LocationType)
admin.site.register(Location, LocationAdmin)
admin.site.register(Area, AreaAdmin)
