from setuptools import setup, find_packages
from os.path import join, dirname


setup(
    name='hello_world',
    version='1.0',
    packages=find_packages(),
    test_suite='tests',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
)
