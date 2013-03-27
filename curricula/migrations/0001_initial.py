# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PublisherGroup'
        db.create_table('curricula_publishergroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('curricula', ['PublisherGroup'])

        # Adding model 'Publisher'
        db.create_table('curricula_publisher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('publisher_id', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['curricula.PublisherGroup'], blank=True)),
        ))
        db.send_create_signal('curricula', ['Publisher'])

        # Adding model 'LearningMaterial'
        db.create_table('curricula_learningmaterial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=13, null=True)),
            ('ordering_code', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['curricula.Publisher'])),
            ('material_type', self.gf('django.db.models.fields.CharField')(default='Book', max_length=20)),
            ('isTeacherEdition', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('curricula', ['LearningMaterial'])

        # Adding model 'Curriculum'
        db.create_table('curricula_curriculum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['curricula.PublisherGroup'])),
            ('subject_area', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('secondary_subject_area', self.gf('django.db.models.fields.CharField')(max_length=25, null=True)),
        ))
        db.send_create_signal('curricula', ['Curriculum'])

        # Adding model 'GradeCurriculum'
        db.create_table('curricula_gradecurriculum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('curriculum', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['curricula.Curriculum'])),
            ('grade_level_start', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('grade_level_end', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('approved_year', self.gf('django.db.models.fields.CharField')(default='2012_2013', max_length=10, null=True)),
        ))
        db.send_create_signal('curricula', ['GradeCurriculum'])

        # Adding M2M table for field materials on 'GradeCurriculum'
        db.create_table('curricula_gradecurriculum_materials', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gradecurriculum', models.ForeignKey(orm['curricula.gradecurriculum'], null=False)),
            ('learningmaterial', models.ForeignKey(orm['curricula.learningmaterial'], null=False))
        ))
        db.create_unique('curricula_gradecurriculum_materials', ['gradecurriculum_id', 'learningmaterial_id'])

        # Adding M2M table for field necessary_materials on 'GradeCurriculum'
        db.create_table('curricula_gradecurriculum_necessary_materials', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gradecurriculum', models.ForeignKey(orm['curricula.gradecurriculum'], null=False)),
            ('learningmaterial', models.ForeignKey(orm['curricula.learningmaterial'], null=False))
        ))
        db.create_unique('curricula_gradecurriculum_necessary_materials', ['gradecurriculum_id', 'learningmaterial_id'])

        # Adding M2M table for field approved_for_type on 'GradeCurriculum'
        db.create_table('curricula_gradecurriculum_approved_for_type', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gradecurriculum', models.ForeignKey(orm['curricula.gradecurriculum'], null=False)),
            ('schooltype', models.ForeignKey(orm['schools.schooltype'], null=False))
        ))
        db.create_unique('curricula_gradecurriculum_approved_for_type', ['gradecurriculum_id', 'schooltype_id'])


    def backwards(self, orm):
        # Deleting model 'PublisherGroup'
        db.delete_table('curricula_publishergroup')

        # Deleting model 'Publisher'
        db.delete_table('curricula_publisher')

        # Deleting model 'LearningMaterial'
        db.delete_table('curricula_learningmaterial')

        # Deleting model 'Curriculum'
        db.delete_table('curricula_curriculum')

        # Deleting model 'GradeCurriculum'
        db.delete_table('curricula_gradecurriculum')

        # Removing M2M table for field materials on 'GradeCurriculum'
        db.delete_table('curricula_gradecurriculum_materials')

        # Removing M2M table for field necessary_materials on 'GradeCurriculum'
        db.delete_table('curricula_gradecurriculum_necessary_materials')

        # Removing M2M table for field approved_for_type on 'GradeCurriculum'
        db.delete_table('curricula_gradecurriculum_approved_for_type')


    models = {
        'curricula.curriculum': {
            'Meta': {'object_name': 'Curriculum'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['curricula.PublisherGroup']"}),
            'secondary_subject_area': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'subject_area': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'curricula.gradecurriculum': {
            'Meta': {'object_name': 'GradeCurriculum'},
            'approved_for_type': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'approved_school_types'", 'symmetrical': 'False', 'to': "orm['schools.SchoolType']"}),
            'approved_year': ('django.db.models.fields.CharField', [], {'default': "'2012_2013'", 'max_length': '10', 'null': 'True'}),
            'curriculum': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['curricula.Curriculum']"}),
            'grade_level_end': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'grade_level_start': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materials': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'materials'", 'symmetrical': 'False', 'to': "orm['curricula.LearningMaterial']"}),
            'necessary_materials': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'necessary_materials'", 'symmetrical': 'False', 'to': "orm['curricula.LearningMaterial']"})
        },
        'curricula.learningmaterial': {
            'Meta': {'object_name': 'LearningMaterial'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isTeacherEdition': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True'}),
            'material_type': ('django.db.models.fields.CharField', [], {'default': "'Book'", 'max_length': '20'}),
            'ordering_code': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['curricula.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
        },
        'schools.district': {
            'Meta': {'object_name': 'District'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'schools.schooltype': {
            'Meta': {'object_name': 'SchoolType'},
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['curricula']