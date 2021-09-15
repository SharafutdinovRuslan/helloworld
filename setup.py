# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os.path import join, dirname


setup(
    name='helloworld-package',
    author='Sharafutdinov Ruslan',
    author_email='shar.rus72@gmail.com',
    url='https://github.com/SharafutdinovRuslan/helloworld',
    version='1.0.1',
    description='Setuptools example project',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type='text/markdown',
    packages=find_packages(where="."),
    package_dir={'src': 'src'},
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',
    python_requires=">=3.6",
    classifiers=[
            "Programming Language :: Python :: 3",
        ],
)
