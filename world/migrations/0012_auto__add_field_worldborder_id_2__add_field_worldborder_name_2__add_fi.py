# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WorldBorder.id_2'
        db.add_column('world_worldborder', 'id_2',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'WorldBorder.name_2'
        db.add_column('world_worldborder', 'name_2',
                      self.gf('django.db.models.fields.CharField')(max_length=75, null=True, blank=True),
                      keep_default=False)

        # Adding field 'WorldBorder.varname_2'
        db.add_column('world_worldborder', 'varname_2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'WorldBorder.nl_name_2'
        db.add_column('world_worldborder', 'nl_name_2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'WorldBorder.hasc_2'
        db.add_column('world_worldborder', 'hasc_2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=15, null=True, blank=True),
                      keep_default=False)

        # Adding field 'WorldBorder.cc_2'
        db.add_column('world_worldborder', 'cc_2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=15, null=True, blank=True),
                      keep_default=False)

        # Adding field 'WorldBorder.type_2'
        db.add_column('world_worldborder', 'type_2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'WorldBorder.engtype_2'
        db.add_column('world_worldborder', 'engtype_2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'WorldBorder.validfr_2'
        db.add_column('world_worldborder', 'validfr_2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=25, null=True, blank=True),
                      keep_default=False)

        # Adding field 'WorldBorder.validto_2'
        db.add_column('world_worldborder', 'validto_2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=25, null=True, blank=True),
                      keep_default=False)

        # Adding field 'WorldBorder.remarks_2'
        db.add_column('world_worldborder', 'remarks_2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=125, null=True, blank=True),
                      keep_default=False)

        # Adding field 'WorldBorder.id_3'
        db.add_column('world_worldborder', 'id_3',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'WorldBorder.name_3'
        db.add_column('world_worldborder', 'name_3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=75, null=True, blank=True),
                      keep_default=False)

        # Adding field 'WorldBorder.varname_3'
        db.add_column('world_worldborder', 'varname_3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'WorldBorder.nl_name_3'
        db.add_column('world_worldborder', 'nl_name_3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'WorldBorder.hasc_3'
        db.add_column('world_worldborder', 'hasc_3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=15, null=True, blank=True),
                      keep_default=False)

        # Adding field 'WorldBorder.type_3'
        db.add_column('world_worldborder', 'type_3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'WorldBorder.engtype_3'
        db.add_column('world_worldborder', 'engtype_3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'WorldBorder.validfr_3'
        db.add_column('world_worldborder', 'validfr_3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=25, null=True, blank=True),
                      keep_default=False)

        # Adding field 'WorldBorder.validto_3'
        db.add_column('world_worldborder', 'validto_3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=25, null=True, blank=True),
                      keep_default=False)

        # Adding field 'WorldBorder.remarks_3'
        db.add_column('world_worldborder', 'remarks_3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=125, null=True, blank=True),
                      keep_default=False)


        # Changing field 'WorldBorder.varname_1'
        db.alter_column('world_worldborder', 'varname_1', self.gf('django.db.models.fields.CharField')(max_length=150, null=True))

        # Changing field 'WorldBorder.nl_name_1'
        db.alter_column('world_worldborder', 'nl_name_1', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'WorldBorder.validfr_1'
        db.alter_column('world_worldborder', 'validfr_1', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))

        # Changing field 'WorldBorder.hasc_1'
        db.alter_column('world_worldborder', 'hasc_1', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'WorldBorder.type_1'
        db.alter_column('world_worldborder', 'type_1', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'WorldBorder.validto_1'
        db.alter_column('world_worldborder', 'validto_1', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))

        # Changing field 'WorldBorder.cc_1'
        db.alter_column('world_worldborder', 'cc_1', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'WorldBorder.engtype_1'
        db.alter_column('world_worldborder', 'engtype_1', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'WorldBorder.remarks_1'
        db.alter_column('world_worldborder', 'remarks_1', self.gf('django.db.models.fields.CharField')(max_length=125, null=True))

    def backwards(self, orm):
        # Deleting field 'WorldBorder.id_2'
        db.delete_column('world_worldborder', 'id_2')

        # Deleting field 'WorldBorder.name_2'
        db.delete_column('world_worldborder', 'name_2')

        # Deleting field 'WorldBorder.varname_2'
        db.delete_column('world_worldborder', 'varname_2')

        # Deleting field 'WorldBorder.nl_name_2'
        db.delete_column('world_worldborder', 'nl_name_2')

        # Deleting field 'WorldBorder.hasc_2'
        db.delete_column('world_worldborder', 'hasc_2')

        # Deleting field 'WorldBorder.cc_2'
        db.delete_column('world_worldborder', 'cc_2')

        # Deleting field 'WorldBorder.type_2'
        db.delete_column('world_worldborder', 'type_2')

        # Deleting field 'WorldBorder.engtype_2'
        db.delete_column('world_worldborder', 'engtype_2')

        # Deleting field 'WorldBorder.validfr_2'
        db.delete_column('world_worldborder', 'validfr_2')

        # Deleting field 'WorldBorder.validto_2'
        db.delete_column('world_worldborder', 'validto_2')

        # Deleting field 'WorldBorder.remarks_2'
        db.delete_column('world_worldborder', 'remarks_2')

        # Deleting field 'WorldBorder.id_3'
        db.delete_column('world_worldborder', 'id_3')

        # Deleting field 'WorldBorder.name_3'
        db.delete_column('world_worldborder', 'name_3')

        # Deleting field 'WorldBorder.varname_3'
        db.delete_column('world_worldborder', 'varname_3')

        # Deleting field 'WorldBorder.nl_name_3'
        db.delete_column('world_worldborder', 'nl_name_3')

        # Deleting field 'WorldBorder.hasc_3'
        db.delete_column('world_worldborder', 'hasc_3')

        # Deleting field 'WorldBorder.type_3'
        db.delete_column('world_worldborder', 'type_3')

        # Deleting field 'WorldBorder.engtype_3'
        db.delete_column('world_worldborder', 'engtype_3')

        # Deleting field 'WorldBorder.validfr_3'
        db.delete_column('world_worldborder', 'validfr_3')

        # Deleting field 'WorldBorder.validto_3'
        db.delete_column('world_worldborder', 'validto_3')

        # Deleting field 'WorldBorder.remarks_3'
        db.delete_column('world_worldborder', 'remarks_3')


        # Changing field 'WorldBorder.varname_1'
        db.alter_column('world_worldborder', 'varname_1', self.gf('django.db.models.fields.CharField')(default='', max_length=150))

        # Changing field 'WorldBorder.nl_name_1'
        db.alter_column('world_worldborder', 'nl_name_1', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'WorldBorder.validfr_1'
        db.alter_column('world_worldborder', 'validfr_1', self.gf('django.db.models.fields.CharField')(default='', max_length=25))

        # Changing field 'WorldBorder.hasc_1'
        db.alter_column('world_worldborder', 'hasc_1', self.gf('django.db.models.fields.CharField')(default='', max_length=15))

        # Changing field 'WorldBorder.type_1'
        db.alter_column('world_worldborder', 'type_1', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'WorldBorder.validto_1'
        db.alter_column('world_worldborder', 'validto_1', self.gf('django.db.models.fields.CharField')(default='', max_length=25))

        # Changing field 'WorldBorder.cc_1'
        db.alter_column('world_worldborder', 'cc_1', self.gf('django.db.models.fields.CharField')(default='', max_length=15))

        # Changing field 'WorldBorder.engtype_1'
        db.alter_column('world_worldborder', 'engtype_1', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'WorldBorder.remarks_1'
        db.alter_column('world_worldborder', 'remarks_1', self.gf('django.db.models.fields.CharField')(default='', max_length=125))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_tagged_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_items'", 'to': "orm['taggit.Tag']"})
        },
        'world.location': {
            'Meta': {'object_name': 'Location'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locality': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '255', 'populate_from': "'name'", 'unique_with': '()'}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.LocationType']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'validated_by': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'validated_locations'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['world.Zone']"})
        },
        'world.locationtype': {
            'Meta': {'object_name': 'LocationType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'world.worldborder': {
            'Meta': {'ordering': "('name_1',)", 'object_name': 'WorldBorder'},
            'cc_1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'cc_2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'engtype_1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'engtype_2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'engtype_3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'hasc_1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'hasc_2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'hasc_3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_0': ('django.db.models.fields.IntegerField', [], {}),
            'id_1': ('django.db.models.fields.IntegerField', [], {}),
            'id_2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id_3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'mpoly': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'name_0': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'name_1': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'name_2': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'name_3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'nl_name_1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'nl_name_2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'nl_name_3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'remarks_1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'remarks_2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'remarks_3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'shape_area': ('django.db.models.fields.FloatField', [], {}),
            'shape_leng': ('django.db.models.fields.FloatField', [], {}),
            'type_1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'type_2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'type_3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'validfr_1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'validfr_2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'validfr_3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'validto_1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'validto_2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'validto_3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'varname_1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'varname_2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'varname_3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'null': 'True', 'blank': 'True'}),
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