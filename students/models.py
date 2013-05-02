from django.db import models
from datetime import datetime
from schools.models import School
from curricula.models import GradeCurriculum
from vendors.models import InventoryRecord


class Grade(models.Model):
    school = models.ForeignKey(School)
    grade_level = models.IntegerField()
    likely_math_curriculum = models.ForeignKey(GradeCurriculum, blank=True, null=True, related_name='school_math')
    likely_reading_curriculum = models.ForeignKey(GradeCurriculum, blank=True, null=True, related_name='school_reading')

    def __unicode__(self):
        return "%s, Grade %s" % (self.school.name, self.grade_level)

    def human_grade(self):
        if self.grade_level == 0:
            return 'K'
        elif self.grade_level == -1:
            return 'Pre-K'
        else:
            return self.grade_level

    """
        Define shortfalls as dynamic methods so they update
        when inventory is updated
    """
    def math_material_count(self):
        count = 0
        for m in self.likely_math_curriculum.necessary_materials.all():
            try:
                r = InventoryRecord.objects.get(material=m, school=self.school)
                count += r.get_inventory_total()
            except InventoryRecord.DoesNotExist:
                pass

    def reading_material_count(self):
        count = 0
        for m in self.likely_reading_curriculum.necessary_materials.all():
            try:
                r = InventoryRecord.objects.get(material=m, school=self.school)
                count += r.get_inventory_total()
            except InventoryRecord.DoesNotExist:
                pass


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

    # Associated grade curriculum for the cohort
    associated_reading_curriculum = models.ManyToManyField(GradeCurriculum, related_name="reading_cohort", null=True)
    associated_math_curriculum = models.ManyToManyField(GradeCurriculum, related_name="math_cohort", null=True)

    def math_shortfall(self):
        return self.grade.math_material_count() - self.number_of_students

    def reading_shortfall(self):
        return self.grade.reading_material_count() - self.number_of_students
