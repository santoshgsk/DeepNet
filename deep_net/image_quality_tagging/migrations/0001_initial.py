# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FlatImages'
        db.create_table(u'image_quality_tagging_flatimages', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flat_id', self.gf('django.db.models.fields.IntegerField')()),
            ('service', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image_encoded', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('image_quality_tagging', ['FlatImages'])

        # Adding unique constraint on 'FlatImages', fields ['flat_id', 'image_encoded']
        db.create_unique(u'image_quality_tagging_flatimages', ['flat_id', 'image_encoded'])

        # Adding model 'FlatImageTag'
        db.create_table(u'image_quality_tagging_flatimagetag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('flat_id', self.gf('django.db.models.fields.IntegerField')()),
            ('image_encoded', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('img_wall', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('img_cleanliness', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('img_spacious', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('img_flat_overall', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('img_windows_size', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('image_quality_tagging', ['FlatImageTag'])

        # Adding unique constraint on 'FlatImageTag', fields ['uid', 'image_encoded']
        db.create_unique(u'image_quality_tagging_flatimagetag', ['uid', 'image_encoded'])

        # Adding index on 'FlatImageTag', fields ['uid', 'image_encoded']
        db.create_index(u'image_quality_tagging_flatimagetag', ['uid', 'image_encoded'])


    def backwards(self, orm):
        # Removing index on 'FlatImageTag', fields ['uid', 'image_encoded']
        db.delete_index(u'image_quality_tagging_flatimagetag', ['uid', 'image_encoded'])

        # Removing unique constraint on 'FlatImageTag', fields ['uid', 'image_encoded']
        db.delete_unique(u'image_quality_tagging_flatimagetag', ['uid', 'image_encoded'])

        # Removing unique constraint on 'FlatImages', fields ['flat_id', 'image_encoded']
        db.delete_unique(u'image_quality_tagging_flatimages', ['flat_id', 'image_encoded'])

        # Deleting model 'FlatImages'
        db.delete_table(u'image_quality_tagging_flatimages')

        # Deleting model 'FlatImageTag'
        db.delete_table(u'image_quality_tagging_flatimagetag')


    models = {
        'image_quality_tagging.flatimages': {
            'Meta': {'unique_together': "(('flat_id', 'image_encoded'),)", 'object_name': 'FlatImages'},
            'flat_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_encoded': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'image_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'service': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'image_quality_tagging.flatimagetag': {
            'Meta': {'unique_together': "(('uid', 'image_encoded'),)", 'object_name': 'FlatImageTag', 'index_together': "[['uid', 'image_encoded']]"},
            'flat_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_encoded': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'img_cleanliness': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'img_flat_overall': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'img_spacious': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'img_wall': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'img_windows_size': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['image_quality_tagging']