from setuptools import setup

import os

# Put here required packages
packages = ['Django<=1.6',
	'psycopg2',
	'django-tastypie',
  'django-guardian',
  'South',
  'python-mimeparse==0.1.4',
  'python-dateutil==2.1',
  'simplejson==3.3.0',]

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='Bitcoindir',
      version='1.0',
      description='Web app for locating bitcoin related businesses.',
      author='Tomas Castro',
      author_email='tomas.caslo90.web@gmail.com',
      url='https://pypi.python.org/pypi',
      install_requires=packages,
)

