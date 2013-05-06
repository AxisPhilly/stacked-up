from django.db import models
from schools.models import School


class SchoolAggregate(models.Model):
    school = models.ForeignKey(School)
    number_of_common_materials = models.IntegerField()
    number_of_students = models.IntegerField()

    def books_for_students(self):
        return self.number_of_common_materials - (self.number_of_students * 2)
