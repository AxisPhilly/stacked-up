import os
from os.path import abspath, dirname
import sys
import re

# Set up django path so you can just run this in the VM
project_dir = abspath(dirname(dirname(__file__)))
sys.path.insert(0, project_dir)
os.environ["DJANGO_SETTINGS_MODULE"] = "sdp_curricula.settings"

from curricula.models import LearningMaterial

for material in LearningMaterial.objects.all():
    mysearch = '(?<=package of )[0-9]* students'
    if re.search(mysearch, material.title):
        print 'we have multiples!'
        g = re.search(mysearch, material.title)
        value = g.group(0).split(' ')
        # material.quantity = int(value[0])
        # material.save()
        print material.title
        print material.quantity

# (?<=W/ )
