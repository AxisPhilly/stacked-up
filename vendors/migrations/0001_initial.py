# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Vendor'
        db.create_table('vendors_vendor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('vendors', ['Vendor'])

        # Adding M2M table for field district on 'Vendor'
        db.create_table('vendors_vendor_district', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('vendor', models.ForeignKey(orm['vendors.vendor'], null=False)),
            ('district', models.ForeignKey(orm['schools.district'], null=False))
        ))
        db.create_unique('vendors_vendor_district', ['vendor_id', 'district_id'])

        # Adding model 'NegotiatedPrice'
        db.create_table('vendors_negotiatedprice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vendor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vendors.Vendor'], null=True)),
            ('value', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2)),
            ('negotiated_year', self.gf('django.db.models.fields.PositiveIntegerField')(default=2012, max_length=4)),
        ))
        db.send_create_signal('vendors', ['NegotiatedPrice'])

        # Adding M2M table for field negotiated_for_school_type on 'NegotiatedPrice'
        db.create_table('vendors_negotiatedprice_negotiated_for_school_type', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('negotiatedprice', models.ForeignKey(orm['vendors.negotiatedprice'], null=False)),
            ('schooltype', models.ForeignKey(orm['schools.schooltype'], null=False))
        ))
        db.create_unique('vendors_negotiatedprice_negotiated_for_school_type', ['negotiatedprice_id', 'schooltype_id'])

        # Adding model 'InventoryRecord'
        db.create_table('vendors_inventoryrecord', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schools.School'])),
            ('qty_onsite', self.gf('django.db.models.fields.IntegerField')()),
            ('qty_to_student_home', self.gf('django.db.models.fields.IntegerField')()),
            ('qty_to_student_class', self.gf('django.db.models.fields.IntegerField')()),
            ('qty_lost_stolen', self.gf('django.db.models.fields.IntegerField')()),
            ('qty_unusable', self.gf('django.db.models.fields.IntegerField')()),
            ('qty_reallocated', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('vendors', ['InventoryRecord'])


    def backwards(self, orm):
        # Deleting model 'Vendor'
        db.delete_table('vendors_vendor')

        # Removing M2M table for field district on 'Vendor'
        db.delete_table('vendors_vendor_district')

        # Deleting model 'NegotiatedPrice'
        db.delete_table('vendors_negotiatedprice')

        # Removing M2M table for field negotiated_for_school_type on 'NegotiatedPrice'
        db.delete_table('vendors_negotiatedprice_negotiated_for_school_type')

        # Deleting model 'InventoryRecord'
        db.delete_table('vendors_inventoryrecord')


    models = {
        'schools.district': {
            'Meta': {'object_name': 'District'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'schools.school': {
            'Meta': {'object_name': 'School'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'grade_end': ('django.db.models.fields.IntegerField', [], {}),
            'grade_start': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'school_id': ('django.db.models.fields.IntegerField', [], {}),
            'school_level': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'school_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.SchoolType']", 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'street_addr': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        },
        'schools.schooltype': {
            'Meta': {'object_name': 'SchoolType'},
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'vendors.inventoryrecord': {
            'Meta': {'object_name': 'InventoryRecord'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'qty_lost_stolen': ('django.db.models.fields.IntegerField', [], {}),
            'qty_onsite': ('django.db.models.fields.IntegerField', [], {}),
            'qty_reallocated': ('django.db.models.fields.IntegerField', [], {}),
            'qty_to_student_class': ('django.db.models.fields.IntegerField', [], {}),
            'qty_to_student_home': ('django.db.models.fields.IntegerField', [], {}),
            'qty_unusable': ('django.db.models.fields.IntegerField', [], {}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.School']"})
        },
        'vendors.negotiatedprice': {
            'Meta': {'object_name': 'NegotiatedPrice'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'negotiated_for_school_type': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'school_types'", 'symmetrical': 'False', 'to': "orm['schools.SchoolType']"}),
            'negotiated_year': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2012', 'max_length': '4'}),
            'value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vendors.Vendor']", 'null': 'True'})
        },
        'vendors.vendor': {
            'Meta': {'object_name': 'Vendor'},
            'district': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'districts'", 'symmetrical': 'False', 'to': "orm['schools.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['vendors']