from django.db import models
from schools.models import School
from curricula.models import Curriculum


class SchoolAggregate(models.Model):
    school = models.ForeignKey(School)
    likely_math_curriculum = models.ForeignKey(Curriculum, blank=True, null=True, related_name='school_math')
    likely_reading_curriculum = models.ForeignKey(Curriculum, blank=True, null=True, related_name='school_reading')
    likely_math_shortfall = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    likely_reading_shortfall = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __unicode__(self):
        return self.school.name
