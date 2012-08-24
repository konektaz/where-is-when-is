# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LocationType'
        db.create_table('world_locationtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('world', ['LocationType'])

        # Adding model 'Location'
        db.create_table('world_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['world.LocationType'])),
            ('zone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['world.Zone'])),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('street_address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('locality', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal('world', ['Location'])


    def backwards(self, orm):
        # Deleting model 'LocationType'
        db.delete_table('world_locationtype')

        # Deleting model 'Location'
        db.delete_table('world_location')


    models = {
        'world.location': {
            'Meta': {'object_name': 'Location'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locality': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.LocationType']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.Zone']"})
        },
        'world.locationtype': {
            'Meta': {'object_name': 'LocationType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'world.worldborder': {
            'Meta': {'ordering': "('name_1',)", 'object_name': 'WorldBorder'},
            'cc_1': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'engtype_1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hasc_1': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_0': ('django.db.models.fields.IntegerField', [], {}),
            'id_1': ('django.db.models.fields.IntegerField', [], {}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'mpoly': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'name_0': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'name_1': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'nl_name_1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'remarks_1': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'shape_area': ('django.db.models.fields.FloatField', [], {}),
            'shape_leng': ('django.db.models.fields.FloatField', [], {}),
            'type_1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'validfr_1': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'validto_1': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'varname_1': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.Zone']", 'null': 'True', 'blank': 'True'})
        },
        'world.zone': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Zone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['world']