# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'District'
        db.create_table('school_data_district', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('school_data', ['District'])

        # Adding model 'Vendor'
        db.create_table('school_data_vendor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('school_data', ['Vendor'])

        # Adding M2M table for field district on 'Vendor'
        db.create_table('school_data_vendor_district', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('vendor', models.ForeignKey(orm['school_data.vendor'], null=False)),
            ('district', models.ForeignKey(orm['school_data.district'], null=False))
        ))
        db.create_unique('school_data_vendor_district', ['vendor_id', 'district_id'])

        # Adding model 'SchoolType'
        db.create_table('school_data_schooltype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.District'])),
        ))
        db.send_create_signal('school_data', ['SchoolType'])

        # Adding model 'Price'
        db.create_table('school_data_price', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2)),
            ('negotiated_year', self.gf('django.db.models.fields.PositiveIntegerField')(default=2012, max_length=4)),
        ))
        db.send_create_signal('school_data', ['Price'])

        # Adding M2M table for field negotiated_for_school_type on 'Price'
        db.create_table('school_data_price_negotiated_for_school_type', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('price', models.ForeignKey(orm['school_data.price'], null=False)),
            ('schooltype', models.ForeignKey(orm['school_data.schooltype'], null=False))
        ))
        db.create_unique('school_data_price_negotiated_for_school_type', ['price_id', 'schooltype_id'])

        # Deleting field 'Textbook.cost'
        db.delete_column('school_data_textbook', 'cost')

        # Deleting field 'GradeCurriculum.is_approved_general'
        db.delete_column('school_data_gradecurriculum', 'is_approved_general')

        # Deleting field 'GradeCurriculum.is_approved_empowerment'
        db.delete_column('school_data_gradecurriculum', 'is_approved_empowerment')

        # Adding M2M table for field approved_for_type on 'GradeCurriculum'
        db.create_table('school_data_gradecurriculum_approved_for_type', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gradecurriculum', models.ForeignKey(orm['school_data.gradecurriculum'], null=False)),
            ('schooltype', models.ForeignKey(orm['school_data.schooltype'], null=False))
        ))
        db.create_unique('school_data_gradecurriculum_approved_for_type', ['gradecurriculum_id', 'schooltype_id'])


        # Changing field 'Cohort.year_start'
        db.alter_column('school_data_cohort', 'year_start', self.gf('django.db.models.fields.IntegerField')(max_length=4))

        # Changing field 'Cohort.year_end'
        db.alter_column('school_data_cohort', 'year_end', self.gf('django.db.models.fields.IntegerField')(max_length=4))

    def backwards(self, orm):
        # Deleting model 'District'
        db.delete_table('school_data_district')

        # Deleting model 'Vendor'
        db.delete_table('school_data_vendor')

        # Removing M2M table for field district on 'Vendor'
        db.delete_table('school_data_vendor_district')

        # Deleting model 'SchoolType'
        db.delete_table('school_data_schooltype')

        # Deleting model 'Price'
        db.delete_table('school_data_price')

        # Removing M2M table for field negotiated_for_school_type on 'Price'
        db.delete_table('school_data_price_negotiated_for_school_type')

        # Adding field 'Textbook.cost'
        db.add_column('school_data_textbook', 'cost',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2),
                      keep_default=False)

        # Adding field 'GradeCurriculum.is_approved_general'
        db.add_column('school_data_gradecurriculum', 'is_approved_general',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GradeCurriculum.is_approved_empowerment'
        db.add_column('school_data_gradecurriculum', 'is_approved_empowerment',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Removing M2M table for field approved_for_type on 'GradeCurriculum'
        db.delete_table('school_data_gradecurriculum_approved_for_type')


        # Changing field 'Cohort.year_start'
        db.alter_column('school_data_cohort', 'year_start', self.gf('django.db.models.fields.IntegerField')(max_length=2))

        # Changing field 'Cohort.year_end'
        db.alter_column('school_data_cohort', 'year_end', self.gf('django.db.models.fields.IntegerField')(max_length=2))

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
            'year_end': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'year_start': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        },
        'school_data.curriculum': {
            'Meta': {'object_name': 'Curriculum'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.PublisherGroup']"}),
            'secondary_subject_area': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'subject_area': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'school_data.district': {
            'Meta': {'object_name': 'District'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'school_data.grade': {
            'Meta': {'object_name': 'Grade'},
            'grade_level': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.School']"})
        },
        'school_data.gradecurriculum': {
            'Meta': {'object_name': 'GradeCurriculum'},
            'approved_for_type': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'approved_school_types'", 'symmetrical': 'False', 'to': "orm['school_data.SchoolType']"}),
            'approved_year': ('django.db.models.fields.CharField', [], {'default': "'2012_2013'", 'max_length': '10', 'null': 'True'}),
            'curriculum': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.Curriculum']"}),
            'grade_level_end': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'grade_level_start': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materials': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'materials'", 'symmetrical': 'False', 'to': "orm['school_data.Textbook']"}),
            'necessary_materials': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'necessary_materials'", 'symmetrical': 'False', 'to': "orm['school_data.Textbook']"})
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
        'school_data.price': {
            'Meta': {'object_name': 'Price'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'negotiated_for_school_type': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'school_types'", 'symmetrical': 'False', 'to': "orm['school_data.SchoolType']"}),
            'negotiated_year': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2012', 'max_length': '4'}),
            'value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'})
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
        'school_data.schooltype': {
            'Meta': {'object_name': 'SchoolType'},
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'school_data.textbook': {
            'Meta': {'object_name': 'Textbook'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isTeacherEdition': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'material_type': ('django.db.models.fields.CharField', [], {'default': "'Book'", 'max_length': '20'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'school_data.vendor': {
            'Meta': {'object_name': 'Vendor'},
            'district': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'districts'", 'symmetrical': 'False', 'to': "orm['school_data.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['school_data']