from setuptools import setup, find_packages
from os.path import join, dirname


setup(
    name='test_package',
    version='1.0',
    packages=find_packages(where="test_package"),
    package_dir={'': 'test_package'},
    test_suite='tests',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
)
