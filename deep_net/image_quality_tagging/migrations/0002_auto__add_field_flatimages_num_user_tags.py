# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FlatImages.num_user_tags'
        db.add_column(u'image_quality_tagging_flatimages', 'num_user_tags',
                      self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FlatImages.num_user_tags'
        db.delete_column(u'image_quality_tagging_flatimages', 'num_user_tags')


    models = {
        'image_quality_tagging.flatimages': {
            'Meta': {'unique_together': "(('flat_id', 'image_encoded'),)", 'object_name': 'FlatImages'},
            'flat_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_encoded': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'image_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'num_user_tags': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
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