#!/usr/bin/env python

import os
from distutils.core import setup

version = '1.0'

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.4",
    "Programming Language :: Python :: 2.5",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.0",
    "Programming Language :: Python :: 3.1",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries",
]

root_dir = os.path.dirname(__file__)
if not root_dir:
    root_dir = '.'
long_desc = open(root_dir + '/README.md').read()

setup(
    name='python-meli',
    version=version,
    url='https://bitbucket.org/mathiasbc/python-meli',
    download_url='https://mathiasbc@bitbucket.org/mathiasbc/python-meli.git',
    author='Mathias Bustamante',
    author_email='mathias@worldrat.com',
    license='BSD License',
    install_requires=[
        'requests',
    ],
    py_modules=['meli'],
    description='Mercado Libre API wrapper',
    classifiers=classifiers,
    long_description=long_desc,
    keywords='Mercado Libre API',
)