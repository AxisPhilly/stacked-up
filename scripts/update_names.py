import csv
import os
from os.path import abspath, dirname
import sys

# Set up django path to run in the VM
project_dir = abspath(dirname(dirname(__file__)))
sys.path.insert(0, project_dir)
os.environ["DJANGO_SETTINGS_MODULE"] = "sdp_curricula.settings"

from schools.models import School

with open('scripts/school_names.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    reader.next()  # skip header

    for row in reader:
        s = School.objects.get(school_code=int(row[0]))
        s.name = row[1]
        s.save()
