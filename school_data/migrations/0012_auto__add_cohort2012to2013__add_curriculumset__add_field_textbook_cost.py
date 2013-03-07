# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cohort2012To2013'
        db.create_table('school_data_cohort2012to2013', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('grade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.Grade'])),
            ('size', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('school_data', ['Cohort2012To2013'])

        # Adding model 'CurriculumSet'
        db.create_table('school_data_curriculumset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('curriculum', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.Curriculum'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('grade_level_start', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('grade_level_end', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('school_data', ['CurriculumSet'])

        # Adding M2M table for field books on 'CurriculumSet'
        db.create_table('school_data_curriculumset_books', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('curriculumset', models.ForeignKey(orm['school_data.curriculumset'], null=False)),
            ('textbook', models.ForeignKey(orm['school_data.textbook'], null=False))
        ))
        db.create_unique('school_data_curriculumset_books', ['curriculumset_id', 'textbook_id'])

        # Adding field 'Textbook.cost'
        db.add_column('school_data_textbook', 'cost',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2),
                      keep_default=False)

        # Adding field 'Textbook.isTeacherEdition'
        db.add_column('school_data_textbook', 'isTeacherEdition',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Curriculum.grade_level_start'
        db.delete_column('school_data_curriculum', 'grade_level_start')

        # Deleting field 'Curriculum.grade_level_end'
        db.delete_column('school_data_curriculum', 'grade_level_end')

        # Adding field 'Curriculum.name'
        db.add_column('school_data_curriculum', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Removing M2M table for field books on 'Curriculum'
        db.delete_table('school_data_curriculum_books')


        # Changing field 'Curriculum.publisher'
        db.alter_column('school_data_curriculum', 'publisher_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.PublisherGroup']))

    def backwards(self, orm):
        # Deleting model 'Cohort2012To2013'
        db.delete_table('school_data_cohort2012to2013')

        # Deleting model 'CurriculumSet'
        db.delete_table('school_data_curriculumset')

        # Removing M2M table for field books on 'CurriculumSet'
        db.delete_table('school_data_curriculumset_books')

        # Deleting field 'Textbook.cost'
        db.delete_column('school_data_textbook', 'cost')

        # Deleting field 'Textbook.isTeacherEdition'
        db.delete_column('school_data_textbook', 'isTeacherEdition')

        # Adding field 'Curriculum.grade_level_start'
        db.add_column('school_data_curriculum', 'grade_level_start',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Curriculum.grade_level_end'
        db.add_column('school_data_curriculum', 'grade_level_end',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Curriculum.name'
        db.delete_column('school_data_curriculum', 'name')

        # Adding M2M table for field books on 'Curriculum'
        db.create_table('school_data_curriculum_books', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('curriculum', models.ForeignKey(orm['school_data.curriculum'], null=False)),
            ('textbook', models.ForeignKey(orm['school_data.textbook'], null=False))
        ))
        db.create_unique('school_data_curriculum_books', ['curriculum_id', 'textbook_id'])


        # Changing field 'Curriculum.publisher'
        db.alter_column('school_data_curriculum', 'publisher_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.Publisher']))

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
        'school_data.cohort2012to2013': {
            'Meta': {'object_name': 'Cohort2012To2013'},
            'grade': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.Grade']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'size': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'school_data.curriculum': {
            'Meta': {'object_name': 'Curriculum'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_empowerment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.PublisherGroup']"}),
            'subject_area': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'school_data.curriculumset': {
            'Meta': {'object_name': 'CurriculumSet'},
            'books': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['school_data.Textbook']", 'symmetrical': 'False'}),
            'curriculum': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.Curriculum']"}),
            'grade_level_end': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'grade_level_start': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.PublisherGroup']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'publisher_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'school_data.publishergroup': {
            'Meta': {'object_name': 'PublisherGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isTeacherEdition': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['school_data']