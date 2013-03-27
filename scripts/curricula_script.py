import os
from os.path import abspath, dirname
import sys
import csv
import re

# Set up django
project_dir = abspath(dirname(dirname(__file__)))
sys.path.insert(0, project_dir)
os.environ["DJANGO_SETTINGS_MODULE"] = "sdp_curricula.settings"

from curricula.models import LearningMaterial, Publisher, Curriculum, GradeCurriculum
from vendors.models import Vendor, NegotiatedPrice
from schools.models import SchoolType

csv_filepathname = "11_everyday_math_preK.csv"  # Change to the CSV
data = csv.reader(open(csv_filepathname, 'rU'), delimiter=',', quotechar='"')
data.next()
info = data.next()
c_name = info[0]
c_pub = Publisher.objects.get(name=info[3])
try:
    c = Curriculum.objects.get(name=c_name, publisher=c_pub.group)
except Curriculum.DoesNotExist:
    subject = info[4]
    c = Curriculum(name=c_name, publisher=c_pub.group, subject_area=subject)
    c.save()

try:
    g = GradeCurriculum.objects.get(curriculum=c, grade_level_start=info[6], grade_level_end=info[7])
except GradeCurriculum.DoesNotExist:
    g = GradeCurriculum(curriculum=c, grade_level_start=info[6], grade_level_end=info[7])
    g.save()

empowerment = SchoolType.objects.all()[0]  # we only have the one
if info[5] == True:
    g.approved_for_type.add(empowerment)
    g.save()

data.next()
v = Vendor.objects.get(name='McGraw-Hill')
for row in data:
    isbn = row[1].strip().replace('-', '')
    if len(row[1]) > 4:
        title = row[0].strip().replace('*', '')
        try:
            material = LearningMaterial.objects.get(title=title)
            # if row[4] == 'TRUE':
            #     material.isTeacherEdition = True
            #     material.save()
        except LearningMaterial.DoesNotExist:
            m_type = row[3]
            if row[4] == 'TRUE':
                teachers = True
            else:
                teachers = False
            material = LearningMaterial(isbn=isbn,
                title=title, publisher=c_pub,
                material_type=m_type, isTeacherEdition=teachers)
            material.save()

        if '$' in row[2]:
            price = float(re.sub('[\$,]', '', row[2]))
            n = NegotiatedPrice(value=price, vendor=v, material=material)
            n.save()
        # g.materials.add(material)
        # g.save()
