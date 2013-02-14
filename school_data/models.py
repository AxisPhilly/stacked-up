from django.db import models
from datetime import datetime

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

class Grade(models.Model):
    school = models.ForeignKey(School)
    grade_name = models.IntegerField()
    MATH_ADVANCED_PERCENT = models.CharField(max_length=3)

class Cohort(models.Model):
    YEARS = []
    for r in range(2008, (datetime.datetime.now().year+1)):
        YEARS.append((r,r))

    grade = models.ForeignKey(Grade)
    students = models.IntegerField()
    # Cohort year, ex. 2008-2009
    year_start = models.IntegerField(max_length=2, choices=YEARS)
    year_end = models.IntegerField(max_length=2, choices=YEARS)
    MATH_ADVANCED_PERCENT = models.IntegerField()
    MATH_PROFICIENT_PERCENT = models.IntegerField()
    MATH_BASIC_PERCENT = models.IntegerField()
    MATH_BELOW_BASIC_PERCENT = models.IntegerField()
    READ_ADVANCED_PERCENT = models.IntegerField()
    READ_PROFICIENT_PERCENT = models.IntegerField()
    READ_BASIC_PERCENT = models.IntegerField()
    READ_BELOW_BASIC_PERCENT = models.IntegerField()
    MATH_COMBINED_PERCENT = models.IntegerField()
    READ_COMBINED_PERCENT = models.IntegerField() 
