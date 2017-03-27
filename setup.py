#!/usr/bin/env python
from distutils.core import setup

setup(name='plus1s',
      version='1.0',
      description='Are you a real fans?',
      author='DZ Chan',
      author_email='cdzos97@gmail.com',
      packages = ['plus1s'],
      # py_modules=['plus1s'],
      scripts=['bin/plus1s'],
      install_requires=[
            'appdirs==1.4.3',
            'olefile==0.44',
            'packaging==16.8',
            'Pillow==4.0.0',
            'pyparsing==2.2.0',
            'six==1.10.0',
            'xtermcolor==1.3',
      ],
      package_data={
            'plus1s': ['resources/*.txt', 'resources/images/*.jpg']
      },
      )
