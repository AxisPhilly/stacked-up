# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Grade'
        db.create_table('school_data_grade', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.School'])),
            ('grade_name', self.gf('django.db.models.fields.IntegerField')()),
            ('MATH_ADVANCED_PERCENT', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('school_data', ['Grade'])


    def backwards(self, orm):
        # Deleting model 'Grade'
        db.delete_table('school_data_grade')


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
        'school_data.grade': {
            'MATH_ADVANCED_PERCENT': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'Meta': {'object_name': 'Grade'},
            'grade_name': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.School']"})
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