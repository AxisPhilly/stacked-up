from django.db import models
from datetime import datetime
from schools.models import District, School, SchoolType
from curricula.models import LearningMaterial

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    district = models.ManyToManyField(District, related_name='districts')

class NegotiatedPrice(models.Model):
    YEARS = []
    for r in range(2012, (datetime.now().year + 1)):
        YEARS.append((r, r))

    vendor = models.ForeignKey(Vendor, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    negotiated_for_school_type = models.ManyToManyField(SchoolType, related_name='school_types')
    negotiated_year = models.PositiveIntegerField(max_length=4, choices=YEARS, default=2012)
    material = models.ForeignKey(LearningMaterial)

class InventoryRecord(models.Model):
    school = models.ForeignKey(School)
    material = models.ForeignKey(LearningMaterial, null=True)
    qty_onsite = models.IntegerField()
    qty_to_student_home = models.IntegerField()
    qty_to_student_class = models.IntegerField()
    qty_lost_stolen = models.IntegerField()
    qty_unusable = models.IntegerField()
    qty_reallocated = models.IntegerField()
    def __unicode__(self):
        return "%s, %s" % (self.school.name, self.textbook.title)

