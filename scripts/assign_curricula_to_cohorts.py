import os
from os.path import abspath, dirname
import sys

# Set up django path so you can just run this in the VM
project_dir = abspath(dirname(dirname(__file__)))
sys.path.insert(0, project_dir)
os.environ["DJANGO_SETTINGS_MODULE"] = "sdp_curricula.settings"

#from curricula.models import Curriculum, GradeCurriculum
from schools.models import School
from students.models import Grade, Cohort
from vendors.models import InventoryRecord

for school in School.objects.all():
    for grade in Grade.objects.filter(school=school):
        try:
            cohort = Cohort.objects.get(grade=grade, year_start=2012)
            for c in school.curricula_in_use.all():
                #print c
                for g in c.gradecurriculum_set.all():
                    has_materials = False
                    grade_in_set = g.grade_level_start <= grade.grade_level <= g.grade_level_end
                    if grade_in_set:
                        for m in g.materials.all():
                            if (len(InventoryRecord.objects.filter(material=m, school=school)) > 0):
                                has_materials = True
                                break
                    if has_materials:
                        #print 'this curriculum has records for that grade ', school.name, str(grade.grade_level)
                        if g.curriculum.subject_area == "Reading" or g.curriculum.secondary_subject_area == "Reading":
                            cohort.associated_reading_curriculum.add(g)
                        if g.curriculum.subject_area == "Math" or g.curriculum.secondary_subject_area == "Math":
                            cohort.associated_math_curriculum.add(g)
        except Cohort.DoesNotExist:
            print grade, school.name
        # print cohort.associated_math_curriculum.all()
        # print cohort.associated_reading_curriculum.all()
