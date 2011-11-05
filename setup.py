from setuptools import setup, find_packages
import sys, os

version = '1.0'
name = 'usin.skin'

setup(name=name,
      version=version,
      description="usinasite basic Django skin",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='usinasite style CSS',
      author='Olivier Larchev\xe1\xbb\xc3\xc3\xaaque',
      author_email='olivier.larcheveque@gmail.com',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
