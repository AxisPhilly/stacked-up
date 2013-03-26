# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'School'
        db.delete_table('school_data_school')

        # Deleting model 'Vendor'
        db.delete_table('school_data_vendor')

        # Removing M2M table for field district on 'Vendor'
        db.delete_table('school_data_vendor_district')

        # Deleting model 'Textbook'
        db.delete_table('school_data_textbook')

        # Removing M2M table for field prices on 'Textbook'
        db.delete_table('school_data_textbook_prices')

        # Deleting model 'District'
        db.delete_table('school_data_district')

        # Deleting model 'Curriculum'
        db.delete_table('school_data_curriculum')

        # Deleting model 'SchoolType'
        db.delete_table('school_data_schooltype')

        # Deleting model 'GradeCurriculum'
        db.delete_table('school_data_gradecurriculum')

        # Removing M2M table for field materials on 'GradeCurriculum'
        db.delete_table('school_data_gradecurriculum_materials')

        # Removing M2M table for field necessary_materials on 'GradeCurriculum'
        db.delete_table('school_data_gradecurriculum_necessary_materials')

        # Removing M2M table for field approved_for_type on 'GradeCurriculum'
        db.delete_table('school_data_gradecurriculum_approved_for_type')

        # Deleting model 'Publisher'
        db.delete_table('school_data_publisher')

        # Deleting model 'PublisherGroup'
        db.delete_table('school_data_publishergroup')

        # Deleting model 'InventoryRecord'
        db.delete_table('school_data_inventoryrecord')

        # Deleting model 'Cohort'
        db.delete_table('school_data_cohort')

        # Deleting model 'Grade'
        db.delete_table('school_data_grade')

        # Deleting model 'Price'
        db.delete_table('school_data_price')

        # Removing M2M table for field negotiated_for_school_type on 'Price'
        db.delete_table('school_data_price_negotiated_for_school_type')


    def backwards(self, orm):
        # Adding model 'School'
        db.create_table('school_data_school', (
            ('website', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('street_addr', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('school_level', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('school_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.SchoolType'], null=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('grade_end', self.gf('django.db.models.fields.IntegerField')()),
            ('grade_start', self.gf('django.db.models.fields.IntegerField')()),
            ('school_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('school_data', ['School'])

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

        # Adding model 'Textbook'
        db.create_table('school_data_textbook', (
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.Publisher'])),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=13, null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('ordering_code', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('material_type', self.gf('django.db.models.fields.CharField')(default='Book', max_length=20)),
            ('isTeacherEdition', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('school_data', ['Textbook'])

        # Adding M2M table for field prices on 'Textbook'
        db.create_table('school_data_textbook_prices', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('textbook', models.ForeignKey(orm['school_data.textbook'], null=False)),
            ('price', models.ForeignKey(orm['school_data.price'], null=False))
        ))
        db.create_unique('school_data_textbook_prices', ['textbook_id', 'price_id'])

        # Adding model 'District'
        db.create_table('school_data_district', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('school_data', ['District'])

        # Adding model 'Curriculum'
        db.create_table('school_data_curriculum', (
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.PublisherGroup'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('subject_area', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('secondary_subject_area', self.gf('django.db.models.fields.CharField')(max_length=25, null=True)),
        ))
        db.send_create_signal('school_data', ['Curriculum'])

        # Adding model 'SchoolType'
        db.create_table('school_data_schooltype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.District'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('school_data', ['SchoolType'])

        # Adding model 'GradeCurriculum'
        db.create_table('school_data_gradecurriculum', (
            ('grade_level_start', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('curriculum', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.Curriculum'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('approved_year', self.gf('django.db.models.fields.CharField')(default='2012_2013', max_length=10, null=True)),
            ('grade_level_end', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('school_data', ['GradeCurriculum'])

        # Adding M2M table for field materials on 'GradeCurriculum'
        db.create_table('school_data_gradecurriculum_materials', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gradecurriculum', models.ForeignKey(orm['school_data.gradecurriculum'], null=False)),
            ('textbook', models.ForeignKey(orm['school_data.textbook'], null=False))
        ))
        db.create_unique('school_data_gradecurriculum_materials', ['gradecurriculum_id', 'textbook_id'])

        # Adding M2M table for field necessary_materials on 'GradeCurriculum'
        db.create_table('school_data_gradecurriculum_necessary_materials', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gradecurriculum', models.ForeignKey(orm['school_data.gradecurriculum'], null=False)),
            ('textbook', models.ForeignKey(orm['school_data.textbook'], null=False))
        ))
        db.create_unique('school_data_gradecurriculum_necessary_materials', ['gradecurriculum_id', 'textbook_id'])

        # Adding M2M table for field approved_for_type on 'GradeCurriculum'
        db.create_table('school_data_gradecurriculum_approved_for_type', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gradecurriculum', models.ForeignKey(orm['school_data.gradecurriculum'], null=False)),
            ('schooltype', models.ForeignKey(orm['school_data.schooltype'], null=False))
        ))
        db.create_unique('school_data_gradecurriculum_approved_for_type', ['gradecurriculum_id', 'schooltype_id'])

        # Adding model 'Publisher'
        db.create_table('school_data_publisher', (
            ('publisher_id', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.PublisherGroup'], blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('school_data', ['Publisher'])

        # Adding model 'PublisherGroup'
        db.create_table('school_data_publishergroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('school_data', ['PublisherGroup'])

        # Adding model 'InventoryRecord'
        db.create_table('school_data_inventoryrecord', (
            ('qty_to_student_class', self.gf('django.db.models.fields.IntegerField')()),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.School'])),
            ('qty_unusable', self.gf('django.db.models.fields.IntegerField')()),
            ('qty_onsite', self.gf('django.db.models.fields.IntegerField')()),
            ('qty_reallocated', self.gf('django.db.models.fields.IntegerField')()),
            ('qty_to_student_home', self.gf('django.db.models.fields.IntegerField')()),
            ('qty_lost_stolen', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('textbook', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.Textbook'])),
        ))
        db.send_create_signal('school_data', ['InventoryRecord'])

        # Adding model 'Cohort'
        db.create_table('school_data_cohort', (
            ('math_combined_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1)),
            ('year_start', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('math_proficient_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1)),
            ('number_of_students', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('grade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.Grade'])),
            ('math_basic_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1)),
            ('read_advanced_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1)),
            ('math_below_basic_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1)),
            ('math_advanced_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1)),
            ('read_combined_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1)),
            ('read_proficient_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1)),
            ('year_end', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('read_basic_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('read_below_basic_percent', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1)),
        ))
        db.send_create_signal('school_data', ['Cohort'])

        # Adding model 'Grade'
        db.create_table('school_data_grade', (
            ('grade_level', self.gf('django.db.models.fields.IntegerField')()),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.School'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('school_data', ['Grade'])

        # Adding model 'Price'
        db.create_table('school_data_price', (
            ('vendor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school_data.Vendor'], null=True)),
            ('value', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2)),
            ('negotiated_year', self.gf('django.db.models.fields.PositiveIntegerField')(default=2012, max_length=4)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('school_data', ['Price'])

        # Adding M2M table for field negotiated_for_school_type on 'Price'
        db.create_table('school_data_price_negotiated_for_school_type', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('price', models.ForeignKey(orm['school_data.price'], null=False)),
            ('schooltype', models.ForeignKey(orm['school_data.schooltype'], null=False))
        ))
        db.create_unique('school_data_price_negotiated_for_school_type', ['price_id', 'schooltype_id'])


    models = {
        
    }

    complete_apps = ['school_data']