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

        if level == 0:
            for feat in layer:
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

                areageom = Geom(area=area)
                areageom.geom = area_geom
                areageom.save()

        else:

            with Area.objects.delay_mptt_updates():

	        for feat in layer:
                    parent_id = feat['ID_%s' % (level-1,)].value
                    area_id = feat['ID_%s' % level].value
                    area_name = unicode(feat['NAME_%s' % level].value, 'iso-8859-1')
                    area_varname = unicode(feat['VARNAME_%s' % level].value, 'iso-8859-1')
                    area_type = unicode(feat['TYPE_%s' % level].value, 'iso-8859-1')

                    try:
                        Area.objects.get(shape_id=area_id)
                    except Area.DoesNotExist:
                        pass
                    else:
                        continue

                    mpgeom = OGRGeometry('MultiPolygon')
                    mpgeom.add(feat.geom)

                    area_geom = GEOSGeometry(mpgeom.wkt)

                    print "%s (%s): %s (%s)" % (area_id, parent_id, area_name, area_type)

                    area = Area()
                    area.shape_id = area_id
                    area.parent_id = Area.objects.get(shape_id=parent_id).pk
                    area.name = area_name
                    area.varname = area_varname
                    area.type = area_type

                    area.save()

                    areageom = Geom(area=area)
                    areageom.geom = area_geom
                    areageom.save()
