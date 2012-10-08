# -*- coding: utf-8 -*-

from django.contrib.gis.db import models
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse

from autoslug import AutoSlugField
from taggit.managers import TaggableManager


class Zone(models.Model):
    name = models.CharField('name', max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('world_zone_detail', [self.slug])


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

    zone = models.ForeignKey(Zone, null=True, blank=True)

    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

    class Meta:
        ordering = ('name_1',)

    def __unicode__(self):
        return self.name_1

    @property
    def poly_simplify(self):
        return self.mpoly.simplify(tolerance=0.001, preserve_topology=True)


class LocationType(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', max_length=255, unique=True)
    type = models.ForeignKey(LocationType)
    zone = models.ForeignKey(Zone)

    point = models.PointField()

    description = models.TextField(blank=True, null=True)

    url = models.URLField(max_length=255, verify_exists=True, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    twitter = models.CharField(max_length=15, blank=True, null=True)

    street_address = models.CharField(max_length=255, blank=True, null=True)
    locality = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile_phone = models.CharField(max_length=20, blank=True, null=True)

    tags = TaggableManager(blank=True)

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('world_location_detail', kwargs={'slug': self.slug})

    @property
    def map_html(self):
        return render_to_string('world/map_box.html', {
                'name': self.name,
                'url': self.get_absolute_url,
                })
