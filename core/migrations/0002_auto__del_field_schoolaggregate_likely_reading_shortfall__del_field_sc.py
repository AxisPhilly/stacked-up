# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SchoolAggregate.likely_reading_shortfall'
        db.delete_column('core_schoolaggregate', 'likely_reading_shortfall')

        # Deleting field 'SchoolAggregate.likely_math_shortfall'
        db.delete_column('core_schoolaggregate', 'likely_math_shortfall')


    def backwards(self, orm):
        # Adding field 'SchoolAggregate.likely_reading_shortfall'
        db.add_column('core_schoolaggregate', 'likely_reading_shortfall',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2),
                      keep_default=False)

        # Adding field 'SchoolAggregate.likely_math_shortfall'
        db.add_column('core_schoolaggregate', 'likely_math_shortfall',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2),
                      keep_default=False)


    models = {
        'core.schoolaggregate': {
            'Meta': {'object_name': 'SchoolAggregate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likely_math_curriculum': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'school_math'", 'null': 'True', 'to': "orm['curricula.Curriculum']"}),
            'likely_reading_curriculum': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'school_reading'", 'null': 'True', 'to': "orm['curricula.Curriculum']"}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.School']"})
        },
        'curricula.curriculum': {
            'Meta': {'object_name': 'Curriculum'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['curricula.PublisherGroup']"}),
            'secondary_subject_area': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'subject_area': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'curricula.gradecurriculum': {
            'Meta': {'ordering': "['curriculum', 'grade_level_start']", 'object_name': 'GradeCurriculum'},
            'curriculum': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['curricula.Curriculum']"}),
            'grade_level_end': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'grade_level_start': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materials': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'curricula'", 'symmetrical': 'False', 'to': "orm['curricula.LearningMaterial']"}),
            'necessary_materials': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'required_in'", 'blank': 'True', 'to': "orm['curricula.LearningMaterial']"})
        },
        'curricula.learningmaterial': {
            'Meta': {'object_name': 'LearningMaterial'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isTeacherEdition': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'material_type': ('django.db.models.fields.CharField', [], {'default': "'Book'", 'max_length': '20'}),
            'ordering_code': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['curricula.Publisher']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'curricula.publisher': {
            'Meta': {'ordering': "['name']", 'object_name': 'Publisher'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['curricula.PublisherGroup']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'publisher_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'curricula.publishergroup': {
            'Meta': {'object_name': 'PublisherGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'schools.district': {
            'Meta': {'object_name': 'District'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'schools.school': {
            'Meta': {'ordering': "['school_level', 'name']", 'object_name': 'School'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'curricula_in_use': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['curricula.Curriculum']", 'symmetrical': 'False', 'blank': 'True'}),
            'grade_end': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grade_start': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'school_code': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'school_level': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'school_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.SchoolType']", 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'street_addr': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        },
        'schools.schooltype': {
            'Meta': {'object_name': 'SchoolType'},
            'approved_curricula': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['curricula.GradeCurriculum']", 'symmetrical': 'False'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['core']