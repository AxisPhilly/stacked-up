# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Cohort2012To2013'
        db.delete_table('school_data_cohort2012to2013')

        # Deleting model 'CurriculumSet'
        db.delete_table('school_data_curriculumset')

        # Removing M2M table for field books on 'CurriculumSet'
        db.delete_table('school_data_curriculumset_books')

        # Adding model 'GradeCurriculum'
        db.create_table('school_data_gradecurriculum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('curriculum', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.Curriculum'])),
            ('grade_level_start', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('grade_level_end', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('is_approved_empowerment', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_approved_general', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('approved_year', self.gf('django.db.models.fields.CharField')(default='2012_2013', max_length=10, null=True)),
        ))
        db.send_create_signal('school_data', ['GradeCurriculum'])

        # Adding field 'Textbook.material_type'
        db.add_column('school_data_textbook', 'material_type',
                      self.gf('django.db.models.fields.CharField')(default='Textbook', max_length=20),
                      keep_default=False)

        # Deleting field 'Curriculum.is_empowerment'
        db.delete_column('school_data_curriculum', 'is_empowerment')

        # Adding field 'Curriculum.secondary_subject_area'
        db.add_column('school_data_curriculum', 'secondary_subject_area',
                      self.gf('django.db.models.fields.CharField')(max_length=25, null=True),
                      keep_default=False)


        # Changing field 'Curriculum.subject_area'
        db.alter_column('school_data_curriculum', 'subject_area', self.gf('django.db.models.fields.CharField')(max_length=25))
        # Adding field 'Cohort.number_of_students'
        db.add_column('school_data_cohort', 'number_of_students',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True),
                      keep_default=False)


        # Changing field 'Cohort.math_combined_percent'
        db.alter_column('school_data_cohort', 'math_combined_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1))

        # Changing field 'Cohort.math_proficient_percent'
        db.alter_column('school_data_cohort', 'math_proficient_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1))

        # Changing field 'Cohort.read_advanced_percent'
        db.alter_column('school_data_cohort', 'read_advanced_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1))

        # Changing field 'Cohort.math_basic_percent'
        db.alter_column('school_data_cohort', 'math_basic_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1))

        # Changing field 'Cohort.math_advanced_percent'
        db.alter_column('school_data_cohort', 'math_advanced_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1))

        # Changing field 'Cohort.read_combined_percent'
        db.alter_column('school_data_cohort', 'read_combined_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1))

        # Changing field 'Cohort.read_proficient_percent'
        db.alter_column('school_data_cohort', 'read_proficient_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1))

        # Changing field 'Cohort.math_below_basic_percent'
        db.alter_column('school_data_cohort', 'math_below_basic_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1))

        # Changing field 'Cohort.read_basic_percent'
        db.alter_column('school_data_cohort', 'read_basic_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1))

        # Changing field 'Cohort.read_below_basic_percent'
        db.alter_column('school_data_cohort', 'read_below_basic_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1))

    def backwards(self, orm):
        # Adding model 'Cohort2012To2013'
        db.create_table('school_data_cohort2012to2013', (
            ('grade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.Grade'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('size', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('school_data', ['Cohort2012To2013'])

        # Adding model 'CurriculumSet'
        db.create_table('school_data_curriculumset', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('curriculum', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.Curriculum'])),
            ('grade_level_start', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
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

        # Deleting model 'GradeCurriculum'
        db.delete_table('school_data_gradecurriculum')

        # Deleting field 'Textbook.material_type'
        db.delete_column('school_data_textbook', 'material_type')

        # Adding field 'Curriculum.is_empowerment'
        db.add_column('school_data_curriculum', 'is_empowerment',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Curriculum.secondary_subject_area'
        db.delete_column('school_data_curriculum', 'secondary_subject_area')


        # Changing field 'Curriculum.subject_area'
        db.alter_column('school_data_curriculum', 'subject_area', self.gf('django.db.models.fields.CharField')(max_length=100))
        # Deleting field 'Cohort.number_of_students'
        db.delete_column('school_data_cohort', 'number_of_students')


        # Changing field 'Cohort.math_combined_percent'
        db.alter_column('school_data_cohort', 'math_combined_percent', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=1))

        # Changing field 'Cohort.math_proficient_percent'
        db.alter_column('school_data_cohort', 'math_proficient_percent', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=1))

        # Changing field 'Cohort.read_advanced_percent'
        db.alter_column('school_data_cohort', 'read_advanced_percent', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=1))

        # Changing field 'Cohort.math_basic_percent'
        db.alter_column('school_data_cohort', 'math_basic_percent', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=1))

        # Changing field 'Cohort.math_advanced_percent'
        db.alter_column('school_data_cohort', 'math_advanced_percent', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=1))

        # Changing field 'Cohort.read_combined_percent'
        db.alter_column('school_data_cohort', 'read_combined_percent', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=1))

        # Changing field 'Cohort.read_proficient_percent'
        db.alter_column('school_data_cohort', 'read_proficient_percent', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=1))

        # Changing field 'Cohort.math_below_basic_percent'
        db.alter_column('school_data_cohort', 'math_below_basic_percent', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=1))

        # Changing field 'Cohort.read_basic_percent'
        db.alter_column('school_data_cohort', 'read_basic_percent', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=1))

        # Changing field 'Cohort.read_below_basic_percent'
        db.alter_column('school_data_cohort', 'read_below_basic_percent', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=1))

    models = {
        'school_data.cohort': {
            'Meta': {'object_name': 'Cohort'},
            'grade': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.Grade']"}),
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
            'year_end': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'year_start': ('django.db.models.fields.IntegerField', [], {'max_length': '2'})
        },
        'school_data.curriculum': {
            'Meta': {'object_name': 'Curriculum'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.PublisherGroup']"}),
            'secondary_subject_area': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'subject_area': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'school_data.grade': {
            'Meta': {'object_name': 'Grade'},
            'grade_level': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.School']"})
        },
        'school_data.gradecurriculum': {
            'Meta': {'object_name': 'GradeCurriculum'},
            'approved_year': ('django.db.models.fields.CharField', [], {'default': "'2012_2013'", 'max_length': '10', 'null': 'True'}),
            'curriculum': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.Curriculum']"}),
            'grade_level_end': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'grade_level_start': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved_empowerment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_approved_general': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
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
            'material_type': ('django.db.models.fields.CharField', [], {'default': "'Textbook'", 'max_length': '20'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['school_data']