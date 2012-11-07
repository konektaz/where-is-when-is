# -*- coding: utf-8 -*-

import datetime
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse

from autoslug import AutoSlugField
from taggit.managers import TaggableManager


class Zone(models.Model):
    """
    A grouping of administrative areas that is commonly referred to, but is
    not reflected in our source data.
    For example, collections of American states may be grouped into "Eastern
    Seaboard", "Midwest", etc.
    """
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
    """
    Accommodates data from the Diva-GIS source.
    [URL]
    """
    id_0 = models.IntegerField()
    iso = models.CharField('ISO', max_length=3)
    name_0 = models.CharField('name 0', max_length=75)
    id_1 = models.IntegerField()
    name_1 = models.CharField('name 1', max_length=75)
    varname_1 = models.CharField('var name 1', max_length=150,
        null=True, blank=True, default='')
    nl_name_1 = models.CharField('nl name 1', max_length=50,
        null=True, blank=True, default='')
    hasc_1 = models.CharField('hasc 1', max_length=15,
        null=True, blank=True, default='')
    cc_1 = models.CharField('cc 1', max_length=15,
        null=True, blank=True, default='')
    type_1 = models.CharField('type 1', max_length=50,
        null=True, blank=True, default='')
    engtype_1 = models.CharField('engtype 1', max_length=50,
        null=True, blank=True, default='')
    validfr_1 = models.CharField('validfr 1', max_length=25,
        null=True, blank=True, default='')
    validto_1 = models.CharField('validto 1', max_length=25,
        null=True, blank=True, default='')
    remarks_1 = models.CharField('remarks 1', max_length=125,
        null=True, blank=True, default='')
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    id_2 = models.IntegerField(null=True, blank=True)
    name_2 = models.CharField('name 1', max_length=75,
        null=True, blank=True)
    varname_2 = models.CharField('var name 1', max_length=150,
        null=True, blank=True, default='')
    nl_name_2 = models.CharField('nl name 1', max_length=50,
        null=True, blank=True, default='')
    hasc_2 = models.CharField('hasc 1', max_length=15,
        null=True, blank=True, default='')
    cc_2 = models.CharField('cc 1', max_length=15,
        null=True, blank=True, default='')
    type_2 = models.CharField('type 1', max_length=50,
        null=True, blank=True, default='')
    engtype_2 = models.CharField('engtype 1', max_length=50,
        null=True, blank=True, default='')
    validfr_2 = models.CharField('validfr 1', max_length=25,
        null=True, blank=True, default='')
    validto_2 = models.CharField('validto 1', max_length=25,
        null=True, blank=True, default='')
    remarks_2 = models.CharField('remarks 1', max_length=125,
        null=True, blank=True, default='')
    id_3 = models.IntegerField(null=True, blank=True)
    name_3 = models.CharField('name 1', max_length=75,
        null=True, blank=True, default='')
    varname_3 = models.CharField('var name 1', max_length=150,
        null=True, blank=True, default='')
    nl_name_3 = models.CharField('nl name 1', max_length=50,
        null=True, blank=True, default='')
    hasc_3 = models.CharField('hasc 1', max_length=15,
        null=True, blank=True, default='')
    type_3 = models.CharField('type 1', max_length=50,
        null=True, blank=True, default='')
    engtype_3 = models.CharField('engtype 1', max_length=50,
        null=True, blank=True, default='')
    validfr_3 = models.CharField('validfr 1', max_length=25,
        null=True, blank=True, default='')
    validto_3 = models.CharField('validto 1', max_length=25,
        null=True, blank=True, default='')
    remarks_3 = models.CharField('remarks 1', max_length=125,
        null=True, blank=True, default='')

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

    created_by = models.ForeignKey(User, blank=True, null=True)
    created_at = models.DateTimeField(editable=False)

    validated_by = models.ManyToManyField(User, related_name='validated_locations')

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('world_location_detail', kwargs={'slug': self.slug})

    def save(self):
        if not self.id:
            self.created_at = datetime.datetime.today()

        super(Location, self).save()

    @property
    def map_html(self):
        return render_to_string('world/map_box.html', {
                'name': self.name,
                'url': self.get_absolute_url,
                })
