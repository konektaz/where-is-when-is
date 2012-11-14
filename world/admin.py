# -*- coding: utf-8 -*-

from django.contrib.gis import admin
from mptt.admin import MPTTModelAdmin

from models import Zone, WorldBorder, LocationType, Location, Area


class ZoneAdmin(admin.ModelAdmin):
    pass


class LocationAdmin(admin.OSMGeoAdmin):
    list_filter = ('zone',)
    list_display = ('name', 'zone')


class WorldBorderAdmin(admin.OSMGeoAdmin):
    list_filter = ('zone',)
    list_display = ('name_1', 'zone')
    list_editable = ('zone',)


class AreaAdmin(MPTTModelAdmin):
    list_display = ('name', 'type', 'path')


admin.site.register(Zone, ZoneAdmin)
admin.site.register(LocationType)
admin.site.register(Location, LocationAdmin)
admin.site.register(WorldBorder, WorldBorderAdmin)
admin.site.register(Area, AreaAdmin)
