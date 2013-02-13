from django.db import models

class School(models.Model):
    school_id = models.IntegerField()
    name = models.CharField(max_length = 200)
    grade_start = models.IntegerField()
    grade_end = models.IntegerField()
    def __unicode__(self):
        return self.name

class Address(models.Model):
    school = models.ForeignKey(School)
    street_line1 = models.CharField(max_length = 100, blank = True)
    street_line2 = models.CharField(max_length = 100, blank = True)
    zipcode = models.CharField(max_length = 5, blank = True)
    city = models.CharField(max_length = 100, blank = True)
    state = models.CharField(max_length = 100, blank = True)
