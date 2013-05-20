from .base import *

DEBUG = False
INSTALLED_APPS = list(INSTALLED_APPS) + ['devserver']

try:
	from .local import *
except ImportError:
	pass
