import os
from os.path import abspath, dirname
import sys

# Set up django path so you can just run this in the VM
project_dir = abspath(dirname(dirname(__file__)))
sys.path.insert(0, project_dir)
os.environ["DJANGO_SETTINGS_MODULE"] = "sdp_curricula.settings"

from students.models import Cohort, Grade
from schools.models import School
from vendors.models import InventoryRecord
from curricula.models import GradeCurriculum

for school in School.objects.all():
    #print school.name
    for grade in Grade.objects.filter(school=school):
        cohort = Cohort.objects.get(year_start=2012, grade=grade)
        comparison = {}
        for curriculum in school.curricula_in_use.all():
            print curriculum.name
            for grade_curriculum in GradeCurriculum.objects.filter(curriculum=curriculum):
                comparison[grade_curriculum] = 0
                for material in grade_curriculum.materials.all():
                    for record in InventoryRecord.objects.filter(school=school, material=material):
                        #print material.title
                        comparison[grade_curriculum] = comparison[grade_curriculum] + 1
                print comparison
