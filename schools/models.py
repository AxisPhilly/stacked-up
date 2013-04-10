from django.db import models


class District(models.Model):
    name = models.CharField(max_length=100)


class SchoolType(models.Model):
    name = models.CharField(max_length=20)
    district = models.ForeignKey(District)

    def __unicode__(self):
        return self.name


class School(models.Model):
    school_type = models.ForeignKey(SchoolType, null=True)
    school_id = models.IntegerField(null=True)
    school_code = models.CharField(max_length=4, null=True)
    name = models.CharField(max_length=200, blank=True)
    grade_start = models.IntegerField()
    grade_end = models.IntegerField()
    street_addr = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    website = models.CharField(max_length=100, blank=True)
    school_level = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["school_level", "name"]
