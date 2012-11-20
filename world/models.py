# -*- coding: utf-8 -*-

import datetime
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse

from django.contrib.gis import geos

from autoslug import AutoSlugField
import mptt
from mptt.models import TreeForeignKey
from taggit.managers import TaggableManager


class Area(models.Model):

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    name = models.CharField('name', max_length=75)
    slug = AutoSlugField(populate_from='name', max_length=255, unique=True)
    varname = models.CharField('var name', max_length=150)
    type = models.CharField('type', max_length=50)
    path = models.CharField('path', max_length=255, db_index=True, null=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.update_path()
        super(Area, self).save(*args, **kwargs)

    @property
    def geom_simplify(self):
        return self.geom.simplify

    def update_path(self):
        self.path = u'%s' % self.slug

        if self.parent:
            self.path = u'%s/%s' % ('/'.join([z.slug for z in self.get_ancestors()]), self.path)


mptt.register(Area, order_insertion_by=['name'])


class Geom(models.Model):
    area = models.OneToOneField(Area)
    geom = models.MultiPolygonField()
    geom_simplified = models.MultiPolygonField(null=True, blank=True)
    simplified = models.BooleanField(default=False)

    objects = models.GeoManager()

    def __unicode__(self):
        return self.area.name

    @property
    def simplify(self):
        if not self.simplified:
            geom_simplified = self.geom.simplify(tolerance=0.001, preserve_topology=False)
            if isinstance(geom_simplified, geos.Polygon):
                geom_simplified = geos.MultiPolygon(geom_simplified)
            self.geom_simplified = geom_simplified
            self.simplified = True
            self.save()

        return self.geom_simplified


class LocationType(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', max_length=255, unique=True)
    type = models.ForeignKey(LocationType)

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

    validated_by = models.ManyToManyField(User, related_name='validated_locations', blank=True, null=True)

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

    def is_validated_by(self, user):
        return user == self.created_by or user in self.validated_by.all()
