# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WorldBorder'
        db.create_table('world_worldborder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_0', self.gf('django.db.models.fields.IntegerField')()),
            ('iso', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('name_0', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('id_1', self.gf('django.db.models.fields.IntegerField')()),
            ('name_1', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('varname_1', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('nl_name_1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('hasc_1', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('cc_1', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('type_1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('engtype_1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('validfr_1', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('validto_1', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('remarks_1', self.gf('django.db.models.fields.CharField')(max_length=125)),
            ('shape_leng', self.gf('django.db.models.fields.FloatField')()),
            ('shape_area', self.gf('django.db.models.fields.FloatField')()),
            ('mpoly', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal('world', ['WorldBorder'])


    def backwards(self, orm):
        # Deleting model 'WorldBorder'
        db.delete_table('world_worldborder')


    models = {
        'world.worldborder': {
            'Meta': {'object_name': 'WorldBorder'},
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
            'varname_1': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['world']