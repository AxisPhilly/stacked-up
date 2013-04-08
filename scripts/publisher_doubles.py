import os
from os.path import abspath, dirname
import sys

# Set up django path so you can just run this in the VM
project_dir = abspath(dirname(dirname(__file__)))
sys.path.insert(0, project_dir)
os.environ["DJANGO_SETTINGS_MODULE"] = "sdp_curricula.settings"

from curricula.models import Publisher, LearningMaterial

for g in Publisher.objects.all():
    search = Publisher.objects.filter(name=g.name)
    if len(search) > 1:
        print len(search)
        keeper = search[0]
        for o in search:
            for p in LearningMaterial.objects.filter(publisher=o):
                p.publisher = keeper
                p.save()
            if o != keeper:
                o.delete()
                print 'deleted ' + o.name
