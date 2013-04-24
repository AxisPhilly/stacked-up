import os
from os.path import abspath, dirname
import sys

# Set up django path so you can just run this in the VM
project_dir = abspath(dirname(dirname(__file__)))
sys.path.insert(0, project_dir)
os.environ["DJANGO_SETTINGS_MODULE"] = "sdp_curricula.settings"

from vendors.models import InventoryRecord
from schools.models import School

for school in School.objects.all():
    print school.name
    for record in InventoryRecord.objects.filter(school=school):
        for grade_curriculum in record.material.curricula.all():
            if not grade_curriculum.curriculum in school.curricula_in_use.all():
                school.curricula_in_use.add(grade_curriculum.curriculum)
                print grade_curriculum.curriculum.name
    print school.curricula_in_use.all()
