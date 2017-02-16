"""Setup for the rotten needles library."""

#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import warnings
from setuptools import (find_packages, setup)

import versioneer


# Require Python 3.5 or higher
if sys.version_info.major < 3 or sys.version_info.minor < 5:
    warnings.warn("Rotten needles requires Python 3.5 or higher!")
    sys.exit(1)


with open('README.rst') as f:
    README = f.read()

setup(
    author="Daniel, Adam, Shay",
    author_email="shaypal5@gmail.com",
    name='rotten_needles',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    long_description=README,
    url='https://github.com/shaypal5/rotten_needles',
    packages=find_packages(),
    include_package_data=True,
    entry_points='''
        [console_scripts]
        rotten-saveprof=rotten_needles.imdb_crawl.imdb_crawl:save_cli
        rotten-byfile=rotten_needles.imdb_crawl.imdb_crawl:crawl_by_file
        rotten-unite=rotten_needles.imdb_crawl.imdb_crawl:unite_profiles
        rotten-clear=rotten_needles.imdb_crawl.imdb_crawl:clear_empty_profiles
    ''',
    install_requires=[
        'beautifulsoup4', 'click'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
