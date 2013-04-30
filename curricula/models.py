from django.db import models


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

    class Meta:
        ordering = ["name"]


class LearningMaterial(models.Model):
    """ Learning material has an ISBN and/or an order code.
        this allows us to store data on things without ISBNs, and to
        also keep track of ordering information"""
    isbn = models.CharField(max_length=13, null=True, blank=True)
    ordering_code = models.CharField(max_length=30, null=True, blank=True)

    title = models.CharField(max_length=300)

    publisher = models.ForeignKey(Publisher)

    MATERIALS = [('Book', 'Book'),
                ('Set', 'Set'),
                ('Kit', 'Kit'),
                ('Visual', 'Visual'),
                ('Manipulative', 'Manipulative'),
                ('CD', 'CD'),
                ('CD-ROM', 'CD-ROM'),
                ('DVD', 'DVD'),
                ('Software', 'Software'),
                ('Subscription', 'Subscription'),
                ('VHS', 'VHS'),
                ('Testing', 'Testing')]
    material_type = models.CharField(max_length=20, default='Book', choices=MATERIALS)
    """
        This quantity is the quantity a material is per student, only changed
        when we find a package of materials and can deduce such a thing.
    """
    quantity = models.IntegerField(default=1)
    isTeacherEdition = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s, %s" % (self.isbn, self.title)


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
    secondary_subject_area = models.CharField(max_length=25, null=True, blank=True, choices=SUBJECTS)  # if necessary

    class Meta:
        verbose_name_plural = "curricula"

    def __unicode__(self):
        return self.name


class GradeCurriculum(models.Model):
    curriculum = models.ForeignKey(Curriculum)

    materials = models.ManyToManyField(LearningMaterial, related_name='curricula')
    necessary_materials = models.ManyToManyField(LearningMaterial, related_name='required_in', blank=True)  # comprised of members of materials

    grade_level_start = models.IntegerField(null=True)
    grade_level_end = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = "grade curricula"
        ordering = ["curriculum", "grade_level_start"]

    def __unicode__(self):
        if self.grade_level_start < self.grade_level_end:
            return "%s, grades %s-%s" % (self.curriculum.name, str(self.grade_level_start), str(self.grade_level_end))
        else:
            return "%s, grade %s" % (self.curriculum.name, str(self.grade_level_start))

    def has_necessary_materials_defined(self):
        return self.necessary_materials.count() > 0

    def materials_count(self):
        return self.materials.count()
