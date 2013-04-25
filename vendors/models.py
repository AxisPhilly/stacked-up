from django.db import models
from datetime import datetime
from schools.models import District, SchoolType, School
from curricula.models import LearningMaterial


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    districts = models.ManyToManyField(District, related_name='districts')

    def __unicode__(self):
        return self.name


class NegotiatedPrice(models.Model):
    YEARS = []
    for r in range(2012, (datetime.now().year + 1)):
        YEARS.append((r, r))

    vendor = models.ForeignKey(Vendor, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    material = models.ForeignKey(LearningMaterial)
    negotiated_for_school_type = models.ManyToManyField(SchoolType, related_name='school_types')
    negotiated_year = models.PositiveIntegerField(max_length=4, choices=YEARS, default=2012)

    def __unicode__(self):
        return "%s, %s, %s" % (self.vendor.name, self.value, self.material.title)


class InventoryRecord(models.Model):
    school = models.ForeignKey(School)
    material = models.ForeignKey(LearningMaterial)
    qty_onsite = models.IntegerField()
    qty_to_student_home = models.IntegerField()
    qty_to_student_class = models.IntegerField()
    qty_lost_stolen = models.IntegerField()
    qty_unusable = models.IntegerField()
    qty_reallocated = models.IntegerField()

    def __unicode__(self):
        return "%s, %s" % (self.school.name, self.material.title)

    def get_inventory_total(self):
        return (self.qty_onsite + self.qty_to_student_class + self.qty_to_student_home)
