import os
from os.path import abspath, dirname
import sys

# Set up django path so you can just run this in the VM
project_dir = abspath(dirname(dirname(__file__)))
sys.path.insert(0, project_dir)
os.environ["DJANGO_SETTINGS_MODULE"] = "sdp_curricula.settings"

from curricula.models import LearningMaterial
from vendors.models import InventoryRecord

for m in LearningMaterial.objects.all():
    search = LearningMaterial.objects.filter(isbn=m.isbn)
    if len(search) > 1:
        print len(search)
        keeper = search[0]
        print keeper.title
        for o in search:
            for r in InventoryRecord.objects.filter(material=o):
                r.material = keeper
                r.save()
            if o != keeper:
                o.delete()
                print 'deleted ' + o.title
