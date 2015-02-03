#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
        'kppy',
        'clint'
]

test_requirements = [
]

setup(
    name='keepass_dbcheck',
    version='0.1.0',
    description="Check your keepass-stored passwords against a list passwords",
    long_description=readme + '\n\n' + history,
    author="Justin Fargione",
    author_email='oss@lexicalbits.com',
    url='https://github.com/justif/keepass_dbcheck',
    packages=[
        'keepass_dbcheck',
    ],
    package_dir={'keepass_dbcheck':
                 'keepass_dbcheck'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=True,
    keywords='security passwords keepass',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    # test_suite='tests',
    #tests_require=test_requirements
)
