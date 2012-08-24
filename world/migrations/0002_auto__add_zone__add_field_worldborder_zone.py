# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Zone'
        db.create_table('world_zone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('world', ['Zone'])

        # Adding field 'WorldBorder.zone'
        db.add_column('world_worldborder', 'zone',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['world.Zone'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Zone'
        db.delete_table('world_zone')

        # Deleting field 'WorldBorder.zone'
        db.delete_column('world_worldborder', 'zone_id')


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
            'varname_1': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.Zone']", 'null': 'True', 'blank': 'True'})
        },
        'world.zone': {
            'Meta': {'object_name': 'Zone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['world']