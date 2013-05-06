from django.db import models
from schools.models import School


class SchoolAggregate(models.Model):
    school = models.ForeignKey(School)
    number_of_common_materials = models.IntegerField()
    number_of_students = models.IntegerField()
