#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='saltpad',
    version='0.0.1',
    description='SaltPad is a GUI and CLI tool to manage saltstack deployments + orchestration.',
    long_description=readme + '\n\n' + history,
    author='Boris FELD',
    author_email='boris.feld@novapost.fr',
    url='https://github.com/novapost/saltpad',
    packages=[
        'saltpad',
    ],
    package_dir={'saltpad': 'saltpad'},
    include_package_data=True,
    install_requires=[
    ],
    zip_safe=False,
    keywords='saltpad',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'saltpad = saltpad.saltpad:main'
        ]
    }
)
