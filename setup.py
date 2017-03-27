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
      package_data={
            'plus1s': ['resources/*.txt', 'resources/images/*.jpg']
      },
      url='https://github.com/ChannelOne/plus1s',
      license='LGPL-3.0',
      )
