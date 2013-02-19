# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Cohort.MATH_COMBINED_PERCENT'
        db.delete_column('school_data_cohort', 'MATH_COMBINED_PERCENT')

        # Deleting field 'Cohort.MATH_PROFICIENT_PERCENT'
        db.delete_column('school_data_cohort', 'MATH_PROFICIENT_PERCENT')

        # Deleting field 'Cohort.MATH_BASIC_PERCENT'
        db.delete_column('school_data_cohort', 'MATH_BASIC_PERCENT')

        # Deleting field 'Cohort.READ_ADVANCED_PERCENT'
        db.delete_column('school_data_cohort', 'READ_ADVANCED_PERCENT')

        # Deleting field 'Cohort.MATH_BELOW_BASIC_PERCENT'
        db.delete_column('school_data_cohort', 'MATH_BELOW_BASIC_PERCENT')

        # Deleting field 'Cohort.MATH_ADVANCED_PERCENT'
        db.delete_column('school_data_cohort', 'MATH_ADVANCED_PERCENT')

        # Deleting field 'Cohort.READ_COMBINED_PERCENT'
        db.delete_column('school_data_cohort', 'READ_COMBINED_PERCENT')

        # Deleting field 'Cohort.READ_PROFICIENT_PERCENT'
        db.delete_column('school_data_cohort', 'READ_PROFICIENT_PERCENT')

        # Deleting field 'Cohort.READ_BASIC_PERCENT'
        db.delete_column('school_data_cohort', 'READ_BASIC_PERCENT')

        # Deleting field 'Cohort.READ_BELOW_BASIC_PERCENT'
        db.delete_column('school_data_cohort', 'READ_BELOW_BASIC_PERCENT')

        # Adding field 'Cohort.math_advanced_percent'
        db.add_column('school_data_cohort', 'math_advanced_percent',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Cohort.math_proficient_percent'
        db.add_column('school_data_cohort', 'math_proficient_percent',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Cohort.math_basic_percent'
        db.add_column('school_data_cohort', 'math_basic_percent',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Cohort.math_below_basic_percent'
        db.add_column('school_data_cohort', 'math_below_basic_percent',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Cohort.read_advanced_percent'
        db.add_column('school_data_cohort', 'read_advanced_percent',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Cohort.read_proficient_percent'
        db.add_column('school_data_cohort', 'read_proficient_percent',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Cohort.read_basic_percent'
        db.add_column('school_data_cohort', 'read_basic_percent',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Cohort.read_below_basic_percent'
        db.add_column('school_data_cohort', 'read_below_basic_percent',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Cohort.math_combined_percent'
        db.add_column('school_data_cohort', 'math_combined_percent',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Cohort.read_combined_percent'
        db.add_column('school_data_cohort', 'read_combined_percent',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Deleting field 'Grade.MATH_ADVANCED_PERCENT'
        db.delete_column('school_data_grade', 'MATH_ADVANCED_PERCENT')

        # Deleting field 'Grade.grade_name'
        db.delete_column('school_data_grade', 'grade_name')

        # Adding field 'Grade.grade_level'
        db.add_column('school_data_grade', 'grade_level',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Cohort.MATH_COMBINED_PERCENT'
        raise RuntimeError("Cannot reverse this migration. 'Cohort.MATH_COMBINED_PERCENT' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Cohort.MATH_PROFICIENT_PERCENT'
        raise RuntimeError("Cannot reverse this migration. 'Cohort.MATH_PROFICIENT_PERCENT' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Cohort.MATH_BASIC_PERCENT'
        raise RuntimeError("Cannot reverse this migration. 'Cohort.MATH_BASIC_PERCENT' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Cohort.READ_ADVANCED_PERCENT'
        raise RuntimeError("Cannot reverse this migration. 'Cohort.READ_ADVANCED_PERCENT' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Cohort.MATH_BELOW_BASIC_PERCENT'
        raise RuntimeError("Cannot reverse this migration. 'Cohort.MATH_BELOW_BASIC_PERCENT' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Cohort.MATH_ADVANCED_PERCENT'
        raise RuntimeError("Cannot reverse this migration. 'Cohort.MATH_ADVANCED_PERCENT' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Cohort.READ_COMBINED_PERCENT'
        raise RuntimeError("Cannot reverse this migration. 'Cohort.READ_COMBINED_PERCENT' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Cohort.READ_PROFICIENT_PERCENT'
        raise RuntimeError("Cannot reverse this migration. 'Cohort.READ_PROFICIENT_PERCENT' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Cohort.READ_BASIC_PERCENT'
        raise RuntimeError("Cannot reverse this migration. 'Cohort.READ_BASIC_PERCENT' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Cohort.READ_BELOW_BASIC_PERCENT'
        raise RuntimeError("Cannot reverse this migration. 'Cohort.READ_BELOW_BASIC_PERCENT' and its values cannot be restored.")
        # Deleting field 'Cohort.math_advanced_percent'
        db.delete_column('school_data_cohort', 'math_advanced_percent')

        # Deleting field 'Cohort.math_proficient_percent'
        db.delete_column('school_data_cohort', 'math_proficient_percent')

        # Deleting field 'Cohort.math_basic_percent'
        db.delete_column('school_data_cohort', 'math_basic_percent')

        # Deleting field 'Cohort.math_below_basic_percent'
        db.delete_column('school_data_cohort', 'math_below_basic_percent')

        # Deleting field 'Cohort.read_advanced_percent'
        db.delete_column('school_data_cohort', 'read_advanced_percent')

        # Deleting field 'Cohort.read_proficient_percent'
        db.delete_column('school_data_cohort', 'read_proficient_percent')

        # Deleting field 'Cohort.read_basic_percent'
        db.delete_column('school_data_cohort', 'read_basic_percent')

        # Deleting field 'Cohort.read_below_basic_percent'
        db.delete_column('school_data_cohort', 'read_below_basic_percent')

        # Deleting field 'Cohort.math_combined_percent'
        db.delete_column('school_data_cohort', 'math_combined_percent')

        # Deleting field 'Cohort.read_combined_percent'
        db.delete_column('school_data_cohort', 'read_combined_percent')


        # User chose to not deal with backwards NULL issues for 'Grade.MATH_ADVANCED_PERCENT'
        raise RuntimeError("Cannot reverse this migration. 'Grade.MATH_ADVANCED_PERCENT' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Grade.grade_name'
        raise RuntimeError("Cannot reverse this migration. 'Grade.grade_name' and its values cannot be restored.")
        # Deleting field 'Grade.grade_level'
        db.delete_column('school_data_grade', 'grade_level')


    models = {
        'school_data.cohort': {
            'Meta': {'object_name': 'Cohort'},
            'grade': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.Grade']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'math_advanced_percent': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'math_basic_percent': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'math_below_basic_percent': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'math_combined_percent': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'math_proficient_percent': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'read_advanced_percent': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'read_basic_percent': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'read_below_basic_percent': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'read_combined_percent': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'read_proficient_percent': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'students': ('django.db.models.fields.IntegerField', [], {}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
            'grade_level_end': ('django.db.models.fields.IntegerField', [], {}),
            'grade_level_start': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['school_data']