import os
from os.path import abspath, dirname
import sys
import re

# Set up django path to run in the VM
project_dir = abspath(dirname(dirname(__file__)))
sys.path.insert(0, project_dir)
os.environ["DJANGO_SETTINGS_MODULE"] = "sdp_curricula.settings"

from schools.models import School
from students.models import Grade, Cohort


def find_school_by_id(id):
    school = School.objects.get(school_id=id)
    return school

f = open('scripts/enrollment.txt', 'r')
for line in f:
    if ("School") in line:
        school_and_school_number = re.findall(r'School ([0-9][0-9][0-9][0-9])', line)
        school_number = int(school_and_school_number[0])
    elif ("RSB") in line:
        grades = line.split()
    elif ("TOTR") in line:
        grade_values = line.split()
        for item in grades:
            if not(item == "RSB" or item == "LE79" or item == "GE80" or item == "T" or item == "UG"):
                try:
                    school = School.objects.get(school_id=school_number)
                    grade = Grade.objects.get(school=school, grade_level=int(item))
                    c = Cohort(grade=grade, year_start=2012, year_end=2013, number_of_students=grade_values[grades.index(item)])
                    c.save()
                except Grade.DoesNotExist:
                    print "The current database does not have have a grade entry for:\n", school, "\nSchool Number:", school_number, "\nGrade:", int(item), "\nA 2012 to 2013 cohort will not be added for this grade.\n"
