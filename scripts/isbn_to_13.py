import os
from os.path import abspath, dirname
import sys
import csv
import re

# Set up django path so you can just run this in the VM
project_dir = abspath(dirname(dirname(__file__)))
sys.path.insert(0, project_dir)
os.environ["DJANGO_SETTINGS_MODULE"] = "sdp_curricula.settings"

from curricula.models import LearningMaterial

def check_digit_10(isbn):
    assert len(isbn) == 9
    sum = 0
    for i in range(len(isbn)):
        c = int(isbn[i])
        w = i + 1
        sum += w * c
    r = sum % 11
    if r == 10: return 'X'
    else: return str(r)

def check_digit_13(isbn):
    assert len(isbn) == 12
    sum = 0
    for i in range(len(isbn)):
        c = int(isbn[i])
        if i % 2: w = 3
        else: w = 1
        sum += w * c
    r = 10 - (sum % 10)
    if r == 10: return '0'
    else: return str(r)

def convert_10_to_13(isbn):
    assert len(isbn) == 10
    prefix = '978' + isbn[:-1]
    check = check_digit_13(prefix)
    return prefix + check

for material in LearningMaterial.objects.all():
    if material.isbn != None:
        if len(material.isbn) == 10:
            m = convert_10_to_13(material.isbn)
            material.isbn=m
            material.save()
            print material