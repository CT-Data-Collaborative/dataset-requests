# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DatasetRequest.response'
        db.add_column(u'djangocms_dataset_requests_datasetrequest', 'response',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DatasetRequest.response'
        db.delete_column(u'djangocms_dataset_requests_datasetrequest', 'response')


    models = {
        u'djangocms_dataset_requests.datasetrequest': {
            'Meta': {'ordering': "['-created_date']", 'object_name': 'DatasetRequest'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dataset_description': ('django.db.models.fields.TextField', [], {}),
            'dataset_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'dataset_source': ('adminsortable.fields.SortableForeignKey', [], {'to': u"orm['djangocms_dataset_requests.Source']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'response': ('django.db.models.fields.TextField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'PN'", 'max_length': '2'}),
            'trello_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'user_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'user_first_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'user_last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'user_notified': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'djangocms_dataset_requests.source': {
            'Meta': {'ordering': "['order']", 'object_name': 'Source'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'source_name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }
