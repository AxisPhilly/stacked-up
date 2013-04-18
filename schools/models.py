from django.db import models
from curricula.models import Curriculum, GradeCurriculum


class District(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class SchoolType(models.Model):
    name = models.CharField(max_length=20)
    district = models.ForeignKey(District)
    approved_curricula = models.ManyToManyField(GradeCurriculum)

    def __unicode__(self):
        return self.name


class School(models.Model):
    school_type = models.ForeignKey(SchoolType, null=True, blank=True)
    school_code = models.CharField(max_length=4, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True)
    grade_start = models.IntegerField(null=True, blank=True)
    grade_end = models.IntegerField(null=True, blank=True)
    street_addr = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    website = models.CharField(max_length=100, blank=True)
    school_level = models.CharField(max_length=100, blank=True)
    curricula_in_use = models.ManyToManyField(Curriculum, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["school_level", "name"]
