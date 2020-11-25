from setuptools import setup
from os.path import join, dirname


setup(
    name='test_package',
    version='1.0',
    packages=['test_package'],
    test_suite='tests',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
)
