import os
from os.path import abspath, dirname
import sys
import operator
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
            reading_counts = {}
            reading = {}
            for c in cohort.associated_reading_curriculum.all():
                reading_counts[c.curriculum.name] = 0
                reading[c.curriculum.name] = c
                for m in c.necessary_materials.all():
                    try:
                        r = InventoryRecord.objects.get(material=m, school=school)
                        reading_counts[c.curriculum.name] += r.get_inventory_total()
                    except:
                        pass  # print 'no record'
            if len(reading_counts) > 0:
                winner = max(reading_counts.iteritems(), key=operator.itemgetter(1))[0]
                grade.likely_reading_curriculum = reading[winner]
                grade.save()

            math_counts = {}
            math ={}
            for c in cohort.associated_math_curriculum.all():
                math_counts[c.curriculum.name] = 0
                math[c.curriculum.name] = c
                for m in c.necessary_materials.all():
                    try:
                        r = InventoryRecord.objects.get(material=m, school=school)
                        math_counts[c.curriculum.name] += r.get_inventory_total()
                    except:
                        pass  # print 'no record'
            if len(math_counts) > 0:
                winner = max(math_counts.iteritems(), key=operator.itemgetter(1))[0]
                grade.likely_math_curriculum = math[winner]
                grade.save()

        except Cohort.DoesNotExist:
            print grade, school.name
