from django.db import models
from datetime import datetime

class District(models.Model):
    name = models.CharField(max_length=100)

class SchoolType(models.Model):
    name = models.CharField(max_length=20)
    district = models.ForeignKey(District)

    def __unicode__(self):
        return self.name

class School(models.Model):
    school_type = models.ForeignKey(SchoolType, null=True)
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
    year_start = models.IntegerField(max_length=4, choices=YEARS)
    year_end = models.IntegerField(max_length=4, choices=YEARS)

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

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    district = models.ManyToManyField(District, related_name='districts')

class Price(models.Model):
    YEARS = []
    for r in range(2012, (datetime.now().year + 1)):
        YEARS.append((r, r))

    vendor = models.ForeignKey(Vendor, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    negotiated_for_school_type = models.ManyToManyField(SchoolType, related_name='school_types')
    negotiated_year = models.PositiveIntegerField(max_length=4, choices=YEARS, default=2012)

class Textbook(models.Model):
    """ Learning material has an ISBN and/or an order code.
        this allows us to store data on things without ISBNs, and to
        also keep track of ordering information"""
    isbn = models.CharField(max_length=13, null=True)
    ordering_code = models.CharField(max_length=30, null=True)

    title = models.CharField(max_length=200)

    publisher = models.ForeignKey(Publisher)

    MATERIALS = [('Book', 'Book'),
                ('Set','Set'),
                ('Kit','Kit'),
                ('Visual', 'Visual'),
                ('Manipulative', 'Manipulative'),
                ('CD', 'CD'),
                ('CD-ROM', 'CD-ROM'),
                ('DVD', 'DVD'),
                ('Testing','Testing')]
    material_type = models.CharField(max_length=20, default='Book', choices=MATERIALS)

    prices = models.ManyToManyField(Price, related_name='prices')
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

    materials = models.ManyToManyField(Textbook, related_name='materials')
    necessary_materials = models.ManyToManyField(Textbook, related_name='necessary_materials') # comprised of members of materials

    grade_level_start = models.IntegerField(null=True)
    grade_level_end = models.IntegerField(null=True)

    approved_for_type = models.ManyToManyField(SchoolType, related_name="approved_school_types")
    approved_year = models.CharField(null=True,max_length=10, default='2012_2013')

    class Meta:
        verbose_name_plural = "grade curricula"

    def __unicode__(self):
        return "%s, grades %s-%s" % (self.curriculum.name, str(self.grade_level_start), str(self.grade_level_end))
