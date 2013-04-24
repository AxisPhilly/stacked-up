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
    if re.search('Package of [0-999] copies each of [0-999]', material.title):
        print 'we have multiples!'
        g = re.search('Package of [0-9]* copies each of [0-9]*', material.title)
        print g.group(0)
        print material.title
