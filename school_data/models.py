from django.db import models
from datetime import datetime

class School(models.Model):
    school_id = models.IntegerField()
    name = models.CharField(max_length = 200, blank = True)
    grade_start = models.IntegerField()
    grade_end = models.IntegerField()
    street_addr = models.CharField(max_length = 100, blank = True)
    zipcode = models.CharField(max_length = 5, blank = True)
    city = models.CharField(max_length = 100, blank = True)
    state = models.CharField(max_length = 100, blank = True)
    def __unicode__(self):
        return self.name

class Grade(models.Model):
    school = models.ForeignKey(School)
    grade_name = models.IntegerField()
    MATH_ADVANCED_PERCENT = models.CharField(max_length=3)

class Cohort(models.Model):
    YEARS = []
    for r in range(2008, (datetime.now().year+1)):
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

class Publisher(models.Model):
    name = models.CharField(max_length=200)

class Textbook(models.Model):
    isbn = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey(Publisher)
    grade_level_start = models.IntegerField()
    grade_level_end = models.IntegerField()

class InventoryRecord(models.Model):
    school = models.ForeignKey(School)
    textbook = models.ForeignKey(Textbook)
    qty_onsite = models.IntegerField()
    qty_to_student_home = models.IntegerField()
    qty_to_student_class = models.IntegerField()
    qty_lost_stolen = models.IntegerField()
    qty_unusable = models.IntegerField()
    qty_reallocated = models.IntegerField()

class Curriculum(models.Model):
    SUBJECTS = [('Reading','Reading'),
                ('Mathematics','Mathematics'),
                ('Language Arts','Language Arts'),
                ('Science','Science'),
                ('Social Studies', 'Social Studies')]
    books = models.ManyToManyField(Textbook)
    publisher = models.ForeignKey(Publisher)
    grade_level_start = models.IntegerField()
    grade_level_end = models.IntegerField()
    is_empowerment = models.BooleanField(default=False)
    subject_area = models.CharField(max_length=100, choices=SUBJECTS)
