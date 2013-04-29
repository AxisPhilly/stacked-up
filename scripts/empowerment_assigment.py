import os
from os.path import abspath, dirname
import sys
import re

# Set up django path to run in the VM
project_dir = abspath(dirname(dirname(__file__)))
sys.path.insert(0, project_dir)
os.environ["DJANGO_SETTINGS_MODULE"] = "sdp_curricula.settings"

from schools.models import School, SchoolType


def find_school_by_name(name):
    school = School.objects.get(name__regex=name)
    return school

empowerment = SchoolType.objects.get(name="Empowerment")

with open('scripts/empowerment.txt', 'r') as f:
    for line in f:
        # print line.replace('\n', '')
        school = find_school_by_name(line.strip().replace('*', '').replace('\n', '').upper())
        print school
        school.school_type = empowerment
        school.save()
        print school.school_type
