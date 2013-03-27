# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Grade'
        db.create_table('students_grade', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schools.School'])),
            ('grade_level', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('students', ['Grade'])

        # Adding model 'Cohort'
        db.create_table('students_cohort', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('grade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['students.Grade'])),
            ('year_start', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('year_end', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('math_advanced_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1)),
            ('math_proficient_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1)),
            ('math_basic_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1)),
            ('math_below_basic_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1)),
            ('read_advanced_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1)),
            ('read_proficient_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1)),
            ('read_basic_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1)),
            ('read_below_basic_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1)),
            ('math_combined_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1)),
            ('read_combined_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1)),
            ('number_of_students', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
        ))
        db.send_create_signal('students', ['Cohort'])


    def backwards(self, orm):
        # Deleting model 'Grade'
        db.delete_table('students_grade')

        # Deleting model 'Cohort'
        db.delete_table('students_cohort')


    models = {
        'schools.district': {
            'Meta': {'object_name': 'District'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'schools.school': {
            'Meta': {'object_name': 'School'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'grade_end': ('django.db.models.fields.IntegerField', [], {}),
            'grade_start': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'school_id': ('django.db.models.fields.IntegerField', [], {}),
            'school_level': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'school_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.SchoolType']", 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'street_addr': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        },
        'schools.schooltype': {
            'Meta': {'object_name': 'SchoolType'},
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'students.cohort': {
            'Meta': {'object_name': 'Cohort'},
            'grade': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['students.Grade']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'math_advanced_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1'}),
            'math_basic_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1'}),
            'math_below_basic_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1'}),
            'math_combined_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1'}),
            'math_proficient_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1'}),
            'number_of_students': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'read_advanced_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1'}),
            'read_basic_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1'}),
            'read_below_basic_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1'}),
            'read_combined_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1'}),
            'read_proficient_percent': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1'}),
            'year_end': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'year_start': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        },
        'students.grade': {
            'Meta': {'object_name': 'Grade'},
            'grade_level': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.School']"})
        }
    }

    complete_apps = ['students']