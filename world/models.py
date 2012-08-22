# -*- coding: utf-8 -*-

from django.contrib.gis.db import models


class WorldBorder(models.Model):
    id_0 = models.IntegerField()
    iso = models.CharField('ISO', max_length=3)
    name_0 = models.CharField('name 0', max_length=75)
    id_1 = models.IntegerField()
    name_1 = models.CharField('name 1', max_length=75)
    varname_1 = models.CharField('var name 1', max_length=150)
    nl_name_1 = models.CharField('nl name 1', max_length=50)
    hasc_1 = models.CharField('hasc 1', max_length=15)
    cc_1 = models.CharField('cc 1', max_length=15)
    type_1 = models.CharField('type 1', max_length=50)
    engtype_1 = models.CharField('engtype 1', max_length=50)
    validfr_1 = models.CharField('validfr 1', max_length=25)
    validto_1 = models.CharField('validto 1', max_length=25)
    remarks_1 = models.CharField('remarks 1', max_length=125)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()

    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name_1

    @property
    def poly_simplify(self):
        return self.mpoly.simplify(tolerance=0.001, preserve_topology=True)
