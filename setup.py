#!/usr/bin/env python

# Run with python setup.py develop --user

import setuptools
import os
import platform

setup_requires = []
scripts = []

setuptools.setup(
    name='nicole_utils',
    version='0.1.0',
    python_requires='>=3.7',
    author='Nicole',
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy>=1.11',
        'scipy>=1.6.0',
        'pandas>=1.2.2'
    ],
    scripts=scripts,
    description='Some awesome new tools',
    setup_requires=setup_requires,
    platforms=['Linux', 'Mac OS-X', 'Windows'],
    include_package_data=True,
)