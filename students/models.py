from django.db import models
from datetime import datetime
from schools.models import School

class Grade(models.Model):
    school = models.ForeignKey(School)
    grade_level = models.IntegerField()

    def __unicode__(self):
        return "%s, Grade %s" % (self.school.name, self.grade_level)


class Cohort(models.Model):
    YEARS = []

    for r in range(2008, (datetime.now().year + 1)):
        YEARS.append((r, r))

    grade = models.ForeignKey(Grade)
    # Cohort year, ex. 2008-2009
    year_start = models.IntegerField(max_length=4, choices=YEARS)
    year_end = models.IntegerField(max_length=4, choices=YEARS)

    # PSSA Scores
    math_advanced_percent = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
    math_proficient_percent = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
    math_basic_percent = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
    math_below_basic_percent = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
    read_advanced_percent = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
    read_proficient_percent = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
    read_basic_percent = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
    read_below_basic_percent = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
    math_combined_percent = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
    read_combined_percent = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)

    # Number of students in the grade for that year
    number_of_students = models.PositiveIntegerField(blank=True, null=True)
