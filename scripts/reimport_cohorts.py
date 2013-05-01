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


def find_school_by_id(code):
    try:
        school = School.objects.get(school_code=code)
        return school
    except School.DoesNotExist:
        return False

with open('PSSA.csv', 'r') as csvfile:
    for line in csvfile:
        record = line.split(',')
        if record[3] != '' and record[3] != 'MATH_ADVANCED_PERCENT':
            school = find_school_by_id(record[0].replace('"', ''))
            if school != False:
                # print school.name
                try:
                    grade = Grade.objects.get(school=school,
                        grade_level=record[2].replace('"', ''))
                    cohort = Cohort.objects.get(grade=grade,
                        year_start=record[1].replace('"', '').split('-')[0],
                        year_end=record[1].replace('"', '').split('-')[1])
                    cohort.math_advanced_percent = record[3]
                    cohort.math_proficient_percent = record[4]
                    cohort.math_basic_percent = record[5]
                    cohort.math_below_basic_percent = record[6]
                    cohort.read_advanced_percent = record[7]
                    cohort.read_proficient_percent = record[8]
                    cohort.read_basic_percent = record[9]
                    cohort.read_below_basic_percent = record[10]
                    cohort.math_combined_percent = record[11]
                    cohort.read_combined_percent = record[12].replace('\r\n', '')
                    cohort.save()
                    print 'Cohort saved!'
                    # print record[3]
                    # print record[4]
                    # print record[5]
                    # print record[6]
                    # print record[7]
                    # print record[8]
                    # print record[9]
                    # print record[10]
                    # print record[11]
                    # print record[12].replace('\r\n', '')
                except Grade.DoesNotExist:
                    print school.name + ' is missing grade ' + record[2].replace('"', '')
