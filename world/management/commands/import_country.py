# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.contrib.gis.gdal import DataSource, OGRGeometry
from django.contrib.gis.geos import GEOSGeometry

from world.models import Area, Geom


class Command(BaseCommand):
    args = '<shape file>'
    help = 'Import a country shape file into the database'

    def handle(self, *args, **kwargs):
        shape_file = args[0]

        ds = DataSource(shape_file)
        layer = ds[0]

        for feat in layer:
            try:
                area_id = feat['ID_0'].value
            except:
                area_id = feat['GADMID'].value
            area_name = unicode(feat['NAME_ENGLI'].value, 'iso-8859-1')
            area_varname = unicode(feat['NAME_LOCAL'].value, 'iso-8859-1')

            mpgeom = OGRGeometry('MultiPolygon')
            mpgeom.add(feat.geom)

            area_geom = GEOSGeometry(mpgeom.wkt)

            print "%s %s %s" % (area_id, area_name, area_varname)

            area = Area()
            area.shape_id = area_id
            area.name = area_name
            area.varname = area_varname
            area.type = 'Country'
            area.save()
            area.update_path()
            area.save()

            print "Tree ID: %d" % (area.tree_id,)

            areageom = Geom(area=area)
            areageom.geom = area_geom
            areageom.save()
