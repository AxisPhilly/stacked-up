import os
from os.path import abspath, dirname
import sys

# Set up django path so you can just run this in the VM
project_dir = abspath(dirname(dirname(__file__)))
sys.path.insert(0, project_dir)
os.environ["DJANGO_SETTINGS_MODULE"] = "sdp_curricula.settings"

from vendors.models import NegotiatedPrice

for n in NegotiatedPrice.objects.all():
    for m in n.negotiated_for_school_type.all():
        search = NegotiatedPrice.objects.filter(value=n.value, material=n.material, negotiated_for_school_type=m)
        if len(search) > 1:
            print len(search)
            keeper = search[0], search[0].negotiated_for_school_type.all()
            print keeper
            for o in search:
                # print o, o.negotiated_for_school_type.all()
                if len(o.negotiated_for_school_type.all()) == 2:
                    keeper = o
            for o in search:
                if o != keeper:
                    o.delete()
                    print 'deleted', o
        print len(search)
        print n, n.material.isbn
            #     for r in InventoryRecord.objects.filter(material=o):
            #         r.material = keeper
            #         r.save()
            #     if o != keeper:
            #         o.delete()
            #         print 'deleted ' + o.title
