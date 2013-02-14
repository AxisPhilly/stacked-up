# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'School'
        db.create_table('school_data_school', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('grade_start', self.gf('django.db.models.fields.IntegerField')()),
            ('grade_end', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('school_data', ['School'])

        # Adding model 'Address'
        db.create_table('school_data_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.School'])),
            ('street_line1', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('street_line2', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('school_data', ['Address'])


    def backwards(self, orm):
        # Deleting model 'School'
        db.delete_table('school_data_school')

        # Deleting model 'Address'
        db.delete_table('school_data_address')


    models = {
        'school_data.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.School']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'street_line1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'street_line2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        },
        'school_data.school': {
            'Meta': {'object_name': 'School'},
            'grade_end': ('django.db.models.fields.IntegerField', [], {}),
            'grade_start': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'school_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['school_data']