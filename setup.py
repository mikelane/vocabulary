#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    from os import path
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

from vocabulary.version import VERSION

__version__ = VERSION

try:
    if sys.version_info[:2] <= (2, 7):
        readme = open("README.rst")
    else:
        readme = open("README.rst", encoding="utf8")
    long_description = str(readme.read())
finally:
    readme.close()

setup(
    name="Vocabulary",
    author="Tasdik Rahman",
    version=VERSION,
    author_email="tasdik95@gmail.com",
    description="Module to get meaning, synonym, antonym, part_of_speech, "
    "usage_example, pronunciation and hyphenation for a given word",
    long_description=long_description,
    url="https://github.com/tasdikrahman/vocabulary",
    license="MIT",
    install_requires=["requests==2.21.0", "pytest-mock==1.10.0"],
    # dependency_links=dependency_links,
    # adding package data to it
    packages=find_packages(exclude=["contrib", "docs"]),
    download_url=(
        "https://github.com/tasdikrahman/vocabulary/tarball/" + __version__
    ),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
    ],
    keywords=[
        "Dictionary",
        "Vocabulary",
        "simple dictionary",
        "pydict",
        "dictionary module",
    ],
)
