# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Textbook.grade_level_start'
        db.delete_column('school_data_textbook', 'grade_level_start')

        # Deleting field 'Textbook.grade_level_end'
        db.delete_column('school_data_textbook', 'grade_level_end')

        # Adding field 'Publisher.publisher_id'
        db.add_column('school_data_publisher', 'publisher_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Textbook.grade_level_start'
        db.add_column('school_data_textbook', 'grade_level_start',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Textbook.grade_level_end'
        db.add_column('school_data_textbook', 'grade_level_end',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Publisher.publisher_id'
        db.delete_column('school_data_publisher', 'publisher_id')


    models = {
        'school_data.cohort': {
            'Meta': {'object_name': 'Cohort'},
            'grade': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.Grade']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'math_advanced_percent': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'math_basic_percent': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'math_below_basic_percent': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'math_combined_percent': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'math_proficient_percent': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'read_advanced_percent': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'read_basic_percent': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'read_below_basic_percent': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'read_combined_percent': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'read_proficient_percent': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'year_end': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'year_start': ('django.db.models.fields.IntegerField', [], {'max_length': '2'})
        },
        'school_data.curriculum': {
            'Meta': {'object_name': 'Curriculum'},
            'books': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['school_data.Textbook']", 'symmetrical': 'False'}),
            'grade_level_end': ('django.db.models.fields.IntegerField', [], {}),
            'grade_level_start': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_empowerment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.Publisher']"}),
            'subject_area': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'school_data.grade': {
            'Meta': {'object_name': 'Grade'},
            'grade_level': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.School']"})
        },
        'school_data.inventoryrecord': {
            'Meta': {'object_name': 'InventoryRecord'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'qty_lost_stolen': ('django.db.models.fields.IntegerField', [], {}),
            'qty_onsite': ('django.db.models.fields.IntegerField', [], {}),
            'qty_reallocated': ('django.db.models.fields.IntegerField', [], {}),
            'qty_to_student_class': ('django.db.models.fields.IntegerField', [], {}),
            'qty_to_student_home': ('django.db.models.fields.IntegerField', [], {}),
            'qty_unusable': ('django.db.models.fields.IntegerField', [], {}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.School']"}),
            'textbook': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.Textbook']"})
        },
        'school_data.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'publisher_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'school_data.school': {
            'Meta': {'object_name': 'School'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'grade_end': ('django.db.models.fields.IntegerField', [], {}),
            'grade_start': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'school_id': ('django.db.models.fields.IntegerField', [], {}),
            'school_level': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'street_addr': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        },
        'school_data.textbook': {
            'Meta': {'object_name': 'Textbook'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['school_data']