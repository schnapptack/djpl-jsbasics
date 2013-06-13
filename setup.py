#! /usr/bin/env python
import os
from setuptools import setup, find_packages

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name='djpl-jsbasics',
    version='0.1',
    description='feature for django productline that provides some basic javascript libraries',
    long_description=read('README.rst'),
    license='The MIT License',
    keywords='django, django-productline, javascript libraries',
    author='Toni Michel',
    author_email='toni@schnapptack.de',
    url="https://github.com/schnapptack/djpl-jsbasics",
    packages=find_packages(),
    package_dir={'jsbasics': 'jsbasics'},
    include_package_data=True,
    scripts=[],
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],
    install_requires=[
        'django-productline',
    ]
)
