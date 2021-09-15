from setuptools import setup, find_packages
from os.path import join, dirname


setup(
    name='helloworld',
    version='1.0',
    description='Setuptools example project',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    packages=find_packages(where="test_package"),
    package_dir={'test_package': 'test_package'},
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',
)
