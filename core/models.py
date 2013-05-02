from django.db import models
from schools.models import School
from curricula.models import Curriculum


class SchoolAggregate(models.Model):
    school = models.ForeignKey(School)
    likely_math_curriculum = models.ForeignKey(Curriculum, blank=True, null=True, related_name='school_math')
    likely_reading_curriculum = models.ForeignKey(Curriculum, blank=True, null=True, related_name='school_reading')

    def __unicode__(self):
        return self.school.name

    """
        Define shortfalls as dynamic methods so they update
        when inventory is updated
    """
    def math_shortfall(self):
        pass

    def reading_shortfall(self):
        pass
