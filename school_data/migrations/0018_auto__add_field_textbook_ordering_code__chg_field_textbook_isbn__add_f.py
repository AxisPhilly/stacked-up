# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Textbook.ordering_code'
        db.add_column('school_data_textbook', 'ordering_code',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)

        # Adding M2M table for field prices on 'Textbook'
        db.create_table('school_data_textbook_prices', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('textbook', models.ForeignKey(orm['school_data.textbook'], null=False)),
            ('price', models.ForeignKey(orm['school_data.price'], null=False))
        ))
        db.create_unique('school_data_textbook_prices', ['textbook_id', 'price_id'])


        # Changing field 'Textbook.isbn'
        db.alter_column('school_data_textbook', 'isbn', self.gf('django.db.models.fields.CharField')(max_length=13, null=True))
        # Adding field 'Price.vendor'
        db.add_column('school_data_price', 'vendor',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.Vendor'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Textbook.ordering_code'
        db.delete_column('school_data_textbook', 'ordering_code')

        # Removing M2M table for field prices on 'Textbook'
        db.delete_table('school_data_textbook_prices')


        # Changing field 'Textbook.isbn'
        db.alter_column('school_data_textbook', 'isbn', self.gf('django.db.models.fields.CharField')(default=0, max_length=13))
        # Deleting field 'Price.vendor'
        db.delete_column('school_data_price', 'vendor_id')


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
            'value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.Vendor']", 'null': 'True'})
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
            'school_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school_data.SchoolType']", 'null': 'True'}),
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
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True'}),
            'material_type': ('django.db.models.fields.CharField', [], {'default': "'Book'", 'max_length': '20'}),
            'ordering_code': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'prices': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'prices'", 'symmetrical': 'False', 'to': "orm['school_data.Price']"}),
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