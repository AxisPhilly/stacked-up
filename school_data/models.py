from django.db import models
from datetime import datetime


class School(models.Model):
    school_id = models.IntegerField()
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
    year_start = models.IntegerField(max_length=2, choices=YEARS)
    year_end = models.IntegerField(max_length=2, choices=YEARS)

    # PSSA Scores
    math_advanced_percent = models.DecimalField(null=True, max_digits=5, decimal_places=1)
    math_proficient_percent = models.DecimalField(null=True, max_digits=5, decimal_places=1)
    math_basic_percent = models.DecimalField(null=True, max_digits=5, decimal_places=1)
    math_below_basic_percent = models.DecimalField(null=True, max_digits=5, decimal_places=1)
    read_advanced_percent = models.DecimalField(null=True, max_digits=5, decimal_places=1)
    read_proficient_percent = models.DecimalField(null=True, max_digits=5, decimal_places=1)
    read_basic_percent = models.DecimalField(null=True, max_digits=5, decimal_places=1)
    read_below_basic_percent = models.DecimalField(null=True, max_digits=5, decimal_places=1)
    math_combined_percent = models.DecimalField(null=True, max_digits=5, decimal_places=1)
    read_combined_percent = models.DecimalField(null=True, max_digits=5, decimal_places=1)
    
    # Number of students in the grade for that year
    number_of_students = models.PositiveIntegerField(null=True)

class PublisherGroup(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    publisher_id = models.CharField(max_length=50, blank=True)
    group = models.ForeignKey(PublisherGroup, blank=True)

    def __unicode__(self):
        return "%s, part of %s" % (self.name, self.group.name)

class Textbook(models.Model):
    isbn = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey(Publisher)

    MATERIALS = [('Textbook', 'Textbook'),
                ('Manipulative', 'Manipulative'),
                ('CD', 'CD'),
                ('CD-ROM', 'CD-ROM'),
                ('DVD', 'DVD')]
    material_type = models.CharField(max_length=20, default='Textbook', choices=MATERIALS)
    # Cost only loaded for books associated with a state curricula
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    isTeacherEdition = models.BooleanField(default=False)

    class Meta:
        verbose_name = "learning material"

    def __unicode__(self):
        return "%s, %s" % (self.isbn, self.title)

class InventoryRecord(models.Model):
    school = models.ForeignKey(School)
    textbook = models.ForeignKey(Textbook)
    qty_onsite = models.IntegerField()
    qty_to_student_home = models.IntegerField()
    qty_to_student_class = models.IntegerField()
    qty_lost_stolen = models.IntegerField()
    qty_unusable = models.IntegerField()
    qty_reallocated = models.IntegerField()
    def __unicode__(self):
        return "%s, %s" % (self.school.name, self.textbook.title)

class Curriculum(models.Model):
    """ 
    The superset of curriculum, may include many 
    curriculum sets for multiple grades 
    """
    name = models.CharField(max_length=100)
    SUBJECTS = [('Reading', 'Reading'),
                ('Mathematics', 'Mathematics'),
                ('Language Arts', 'Language Arts'),
                ('Science', 'Science'),
                ('Social Studies', 'Social Studies')]
    publisher = models.ForeignKey(PublisherGroup)
    subject_area = models.CharField(max_length=25, choices=SUBJECTS)
    secondary_subject_area = models.CharField(max_length=25, null=True, choices=SUBJECTS) # if necessary

    class Meta:
        verbose_name_plural = "curricula"

class GradeCurriculum(models.Model):
    curriculum = models.ForeignKey(Curriculum)

    # TODO specify related_name so we can have these
    # materials = models.ManyToManyField(Textbook)
    # necessary_materials = models.ManyToManyField(Textbook) # comprised of members of materials

    grade_level_start = models.IntegerField(null=True)
    grade_level_end = models.IntegerField(null=True)

    is_approved_empowerment = models.BooleanField(default=False)
    is_approved_general = models.BooleanField(default=True)
    approved_year = models.CharField(null=True,max_length=10, default='2012_2013')

