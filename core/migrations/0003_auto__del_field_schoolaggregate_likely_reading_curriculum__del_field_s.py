# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SchoolAggregate.likely_reading_curriculum'
        db.delete_column('core_schoolaggregate', 'likely_reading_curriculum_id')

        # Deleting field 'SchoolAggregate.likely_math_curriculum'
        db.delete_column('core_schoolaggregate', 'likely_math_curriculum_id')

        # Deleting field 'SchoolAggregate.school'
        db.delete_column('core_schoolaggregate', 'school_id')


    def backwards(self, orm):
        # Adding field 'SchoolAggregate.likely_reading_curriculum'
        db.add_column('core_schoolaggregate', 'likely_reading_curriculum',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='school_reading', null=True, to=orm['curricula.Curriculum'], blank=True),
                      keep_default=False)

        # Adding field 'SchoolAggregate.likely_math_curriculum'
        db.add_column('core_schoolaggregate', 'likely_math_curriculum',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='school_math', null=True, to=orm['curricula.Curriculum'], blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'SchoolAggregate.school'
        raise RuntimeError("Cannot reverse this migration. 'SchoolAggregate.school' and its values cannot be restored.")

    models = {
        'core.schoolaggregate': {
            'Meta': {'object_name': 'SchoolAggregate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['core']