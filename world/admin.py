# -*- coding: utf-8 -*-

from django.contrib.gis import admin

from models import Zone, WorldBorder, LocationType, Location


class ZoneAdmin(admin.ModelAdmin):
    pass


class LocationAdmin(admin.GeoModelAdmin):
    list_filter = ('zone',)
    list_display = ('name', 'zone')


class WorldBorderAdmin(admin.GeoModelAdmin):
    list_filter = ('zone',)
    list_display = ('name_1', 'zone')
    list_editable = ('zone',)


admin.site.register(Zone, ZoneAdmin)
admin.site.register(LocationType)
admin.site.register(Location, LocationAdmin)
admin.site.register(WorldBorder, WorldBorderAdmin)
