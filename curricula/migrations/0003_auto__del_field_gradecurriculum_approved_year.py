# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'GradeCurriculum.approved_year'
        db.delete_column('curricula_gradecurriculum', 'approved_year')

        # Removing M2M table for field approved_for_type on 'GradeCurriculum'
        db.delete_table('curricula_gradecurriculum_approved_for_type')


    def backwards(self, orm):
        # Adding field 'GradeCurriculum.approved_year'
        db.add_column('curricula_gradecurriculum', 'approved_year',
                      self.gf('django.db.models.fields.CharField')(default='2012_2013', max_length=10, null=True),
                      keep_default=False)

        # Adding M2M table for field approved_for_type on 'GradeCurriculum'
        db.create_table('curricula_gradecurriculum_approved_for_type', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gradecurriculum', models.ForeignKey(orm['curricula.gradecurriculum'], null=False)),
            ('schooltype', models.ForeignKey(orm['schools.schooltype'], null=False))
        ))
        db.create_unique('curricula_gradecurriculum_approved_for_type', ['gradecurriculum_id', 'schooltype_id'])


    models = {
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
            'materials': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'materials'", 'symmetrical': 'False', 'to': "orm['curricula.LearningMaterial']"}),
            'necessary_materials': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'required_in'", 'blank': 'True', 'to': "orm['curricula.LearningMaterial']"})
        },
        'curricula.learningmaterial': {
            'Meta': {'ordering': "['title']", 'object_name': 'LearningMaterial'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isTeacherEdition': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True'}),
            'material_type': ('django.db.models.fields.CharField', [], {'default': "'Book'", 'max_length': '20'}),
            'ordering_code': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['curricula.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'curricula.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['curricula.PublisherGroup']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'publisher_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'curricula.publishergroup': {
            'Meta': {'object_name': 'PublisherGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['curricula']