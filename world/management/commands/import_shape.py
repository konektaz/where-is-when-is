# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.contrib.gis.gdal import DataSource, OGRGeometry
from django.contrib.gis.geos import GEOSGeometry

from world.models import Area, Geom


class Command(BaseCommand):
    args = '<level> <shape file>'
    help = 'Import a shape file into the database'

    def handle(self, *args, **kwargs):
        level = int(args[0])
        shape_file = args[1]

        ds = DataSource(shape_file)
        layer = ds[0]

        print layer.fields

        if level == 0:
            for feat in layer:
                area_id = feat['GADMID'].value
                area_name = feat['NAME_ENGLI'].value
                area_varname = feat['NAME_LOCAL'].value

                mpgeom = OGRGeometry('MultiPolygon')
                mpgeom.add(feat.geom)

                area_geom = GEOSGeometry(mpgeom.wkt)

                print "%s %s %s" % (area_id, area_name, area_varname)

                area = Area()
                area.id = area_id
                area.name = area_name
                area.varname = area_varname
                area.type = 'Country'
                area.save()

                areageom = Geom(area=area)
                areageom.geom = area_geom
                areageom.save()

        else:

            for feat in layer:
                parent_id = feat['ID_%s' % (level-1,)].value
                area_id = feat['ID_%s' % level].value
                area_name = unicode(feat['NAME_%s' % level].value, 'iso-8859-1')
                area_varname = unicode(feat['VARNAME_%s' % level].value, 'iso-8859-1')
                area_type = unicode(feat['TYPE_%s' % level].value, 'iso-8859-1')

                mpgeom = OGRGeometry('MultiPolygon')
                mpgeom.add(feat.geom)

                area_geom = GEOSGeometry(mpgeom.wkt)

                print "%s (%s): %s (%s)" % (area_id, parent_id, area_name, area_type)

                area = Area()
                area.id = area_id
                area.parent_id = parent_id
                area.name = area_name
                area.varname = area_varname
                area.type = area_type

                area.save()

                areageom = Geom(area=area)
                areageom.geom = area_geom
                areageom.save()
