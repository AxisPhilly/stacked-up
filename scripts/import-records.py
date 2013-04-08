import os
from os.path import abspath, dirname
import sys
import csv
import re

# Set up django path so you can just run this in the VM
project_dir = abspath(dirname(dirname(__file__)))
sys.path.insert(0, project_dir)
os.environ["DJANGO_SETTINGS_MODULE"] = "sdp_curricula.settings"

from curricula.models import LearningMaterial, Publisher
from vendors.models import InventoryRecord
from schools.models import School


def find_school(row, writefile):
    try:
        s = School.objects.get(school_id=row[8])
        return s
    except School.DoesNotExist:
        # print 'DOES NOT EXIST'
        writefile.writerow(row)
        return False
    except ValueError:
        writefile.writerow(row)
        return False


def find_material(row):
    #print row[0]
    new_isbn = convert_10_to_13(row[0])
    try:
        m = LearningMaterial.objects.get(isbn=new_isbn)
        return m
    except LearningMaterial.DoesNotExist:
        m = LearningMaterial(isbn=new_isbn, title=row[1],
            publisher=Publisher.objects.get(name='Unknown'))
        m.save()
        print 'made a new material'
        return m


def iterate_through_data(data):
    count = 0
    for row in data:
        count = count + 1
        if row[0] != '':
            #print row
            school = find_school(row, writefile)
            material = find_material(row)
            # print school, material
            inventory = []
            for x in xrange(2, 8):
                try:
                    inventory.append(int(row[x]))
                except ValueError:
                    inventory.append(0)
            #print inventory
            if school != False:
                r = InventoryRecord(material=material,
                        school=school,
                        qty_onsite=inventory[0],
                        qty_to_student_home=inventory[1],
                        qty_to_student_class=inventory[2],
                        qty_lost_stolen=inventory[3],
                        qty_unusable=inventory[4],
                        qty_reallocated=inventory[5])
                r.save()


def check_digit_10(isbn):
    assert len(isbn) == 9
    sum = 0
    for i in range(len(isbn)):
        c = int(isbn[i])
        w = i + 1
        sum += w * c
    r = sum % 11
    if r == 10:
        return 'X'
    else:
        return str(r)


def check_digit_13(isbn):
    assert len(isbn) == 12
    sum = 0
    for i in range(len(isbn)):
        c = int(isbn[i])
        if i % 2:
            w = 3
        else:
            w = 1
        sum += w * c
    r = 10 - (sum % 10)
    if r == 10:
        return '0'
    else:
        return str(r)


def convert_10_to_13(isbn):
    assert len(isbn) == 10
    prefix = '978' + isbn[:-1]
    check = check_digit_13(prefix)
    return prefix + check


if __name__ == "__main__":
    csv_filepathname = 'curriculum-records.csv'
    writefile = csv.writer(open('school-does-not-exist.csv', 'wb'),
        delimiter=',', quotechar='"')
    data = csv.reader(open(csv_filepathname, 'rU'),
        delimiter=',', quotechar='"')
    data.next()
    iterate_through_data(data)
    print 'done!'
