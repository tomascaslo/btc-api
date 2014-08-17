from setuptools import setup

import os

# Put here required packages
packages = ['Django<=1.6',
	'psycopg2',
	'django-tastypie',]

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='Foodtruckie',
      version='1.0',
      description='Web and mobile app for updating foodtruck location status.',
      author='Tomas Castro',
      author_email='tomas.caslo90.web@gmail.com',
      url='https://pypi.python.org/pypi',
      install_requires=packages,
)

