# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Source'
        db.create_table(u'djangocms_dataset_requests_source', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True)),
            ('source_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'djangocms_dataset_requests', ['Source'])

        # Adding model 'DatasetRequest'
        db.create_table(u'djangocms_dataset_requests_datasetrequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, db_index=True)),
            ('dataset_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('dataset_description', self.gf('django.db.models.fields.TextField')()),
            ('dataset_source', self.gf('adminsortable.fields.SortableForeignKey')(to=orm['djangocms_dataset_requests.Source'])),
            ('user_first_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('user_last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('user_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('user_notified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('status', self.gf('django.db.models.fields.CharField')(default='PN', max_length=2)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('trello_id', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
        ))
        db.send_create_signal(u'djangocms_dataset_requests', ['DatasetRequest'])


    def backwards(self, orm):
        # Deleting model 'Source'
        db.delete_table(u'djangocms_dataset_requests_source')

        # Deleting model 'DatasetRequest'
        db.delete_table(u'djangocms_dataset_requests_datasetrequest')


    models = {
        u'djangocms_dataset_requests.datasetrequest': {
            'Meta': {'ordering': "['-created_date']", 'object_name': 'DatasetRequest'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dataset_description': ('django.db.models.fields.TextField', [], {}),
            'dataset_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'dataset_source': ('adminsortable.fields.SortableForeignKey', [], {'to': u"orm['djangocms_dataset_requests.Source']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'}),
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

    complete_apps = ['djangocms_dataset_requests']
