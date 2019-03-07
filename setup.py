from distutils.core import setup
from setuptools import  find_packages


setup(
    name='unit_testing',
    version='0.1dev',
    packages=find_packages(),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    scripts=['example3/manage.py'],
    install_requires=['django']
)