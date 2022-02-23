 from setuptools import setup

 setup(
   name='zenity',
   version='0.1.0',
   author='Zbomb2000',
   author_email='hxl5900@gmail.com',
   packages=['math'],
   scripts=['bin/script1','bin/script2'],
   url='http://pypi.python.org/pypi/PackageName/',
   license='LICENSE.txt',
   description='Zenity support for Python 3 on Linux.',
   long_description=open('README.txt').read(),
   install_requires=[
       "Django >= 1.1.1",
       "pytest",
   ],
)
