# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Textbook'
        db.create_table('school_data_textbook', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.Publisher'])),
            ('grade_level_start', self.gf('django.db.models.fields.IntegerField')()),
            ('grade_level_end', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('school_data', ['Textbook'])

        # Adding model 'Curriculum'
        db.create_table('school_data_curriculum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.Publisher'])),
            ('grade_level_start', self.gf('django.db.models.fields.IntegerField')()),
            ('grade_level_end', self.gf('django.db.models.fields.IntegerField')()),
            ('is_empowerment', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('subject_area', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('school_data', ['Curriculum'])

        # Adding M2M table for field books on 'Curriculum'
        db.create_table('school_data_curriculum_books', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('curriculum', models.ForeignKey(orm['school_data.curriculum'], null=False)),
            ('textbook', models.ForeignKey(orm['school_data.textbook'], null=False))
        ))
        db.create_unique('school_data_curriculum_books', ['curriculum_id', 'textbook_id'])

        # Adding model 'Publisher'
        db.create_table('school_data_publisher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('school_data', ['Publisher'])

        # Adding model 'InventoryRecord'
        db.create_table('school_data_inventoryrecord', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.School'])),
            ('textbook', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.Textbook'])),
            ('qty_onsite', self.gf('django.db.models.fields.IntegerField')()),
            ('qty_to_student_home', self.gf('django.db.models.fields.IntegerField')()),
            ('qty_to_student_class', self.gf('django.db.models.fields.IntegerField')()),
            ('qty_lost_stolen', self.gf('django.db.models.fields.IntegerField')()),
            ('qty_unusable', self.gf('django.db.models.fields.IntegerField')()),
            ('qty_reallocated', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('school_data', ['InventoryRecord'])

        # Adding model 'Cohort'
        db.create_table('school_data_cohort', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('grade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.Grade'])),
            ('students', self.gf('django.db.models.fields.IntegerField')()),
            ('year_start', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('year_end', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('MATH_ADVANCED_PERCENT', self.gf('django.db.models.fields.IntegerField')()),
            ('MATH_PROFICIENT_PERCENT', self.gf('django.db.models.fields.IntegerField')()),
            ('MATH_BASIC_PERCENT', self.gf('django.db.models.fields.IntegerField')()),
            ('MATH_BELOW_BASIC_PERCENT', self.gf('django.db.models.fields.IntegerField')()),
            ('READ_ADVANCED_PERCENT', self.gf('django.db.models.fields.IntegerField')()),
            ('READ_PROFICIENT_PERCENT', self.gf('django.db.models.fields.IntegerField')()),
            ('READ_BASIC_PERCENT', self.gf('django.db.models.fields.IntegerField')()),
            ('READ_BELOW_BASIC_PERCENT', self.gf('django.db.models.fields.IntegerField')()),
            ('MATH_COMBINED_PERCENT', self.gf('django.db.models.fields.IntegerField')()),
            ('READ_COMBINED_PERCENT', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('school_data', ['Cohort'])


    def backwards(self, orm):
        # Deleting model 'Textbook'
        db.delete_table('school_data_textbook')

        # Deleting model 'Curriculum'
        db.delete_table('school_data_curriculum')

        # Removing M2M table for field books on 'Curriculum'
        db.delete_table('school_data_curriculum_books')

        # Deleting model 'Publisher'
        db.delete_table('school_data_publisher')

        # Deleting model 'InventoryRecord'
        db.delete_table('school_data_inventoryrecord')

        # Deleting model 'Cohort'
        db.delete_table('school_data_cohort')


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
        'school_data.cohort': {
            'MATH_ADVANCED_PERCENT': ('django.db.models.fields.IntegerField', [], {}),
            'MATH_BASIC_PERCENT': ('django.db.models.fields.IntegerField', [], {}),
            'MATH_BELOW_BASIC_PERCENT': ('django.db.models.fields.IntegerField', [], {}),
            'MATH_COMBINED_PERCENT': ('django.db.models.fields.IntegerField', [], {}),
            'MATH_PROFICIENT_PERCENT': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'Cohort'},
            'READ_ADVANCED_PERCENT': ('django.db.models.fields.IntegerField', [], {}),
            'READ_BASIC_PERCENT': ('django.db.models.fields.IntegerField', [], {}),
            'READ_BELOW_BASIC_PERCENT': ('django.db.models.fields.IntegerField', [], {}),
            'READ_COMBINED_PERCENT': ('django.db.models.fields.IntegerField', [], {}),
            'READ_PROFICIENT_PERCENT': ('django.db.models.fields.IntegerField', [], {}),
            'grade': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.Grade']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'MATH_ADVANCED_PERCENT': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'Meta': {'object_name': 'Grade'},
            'grade_name': ('django.db.models.fields.IntegerField', [], {}),
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
            'grade_end': ('django.db.models.fields.IntegerField', [], {}),
            'grade_start': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'school_id': ('django.db.models.fields.IntegerField', [], {})
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