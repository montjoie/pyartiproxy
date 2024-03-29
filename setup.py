#!/usr/bin/env python
import os
import sys
from codecs import open

from setuptools import setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 7)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write(
        """
==========================
Unsupported Python version
==========================
This version of pyartyproxy requires at least Python {}.{}, but
you're trying to install it on Python {}.{}. To resolve this,
consider upgrading to a supported Python version.

""".format(
            *(REQUIRED_PYTHON + CURRENT_PYTHON)
        )
    )
    sys.exit(1)


requires = [
    "requests>=2",
]

with open("readme.md", "r", "utf-8") as f:
    readme = f.read()

setup(
    name="pyartiproxy",
    version="0",
    description="pyartiproxy permit to proxy upload of artifact",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Corentin Labbe",
    author_email="clabbe.montjoie@gmail.com",
    url="https://github.com/montjoie/pyartiproxy",
    packages=["pyartiproxy"],
    package_data={"": ["LICENSE"]},
    #package_dir={"pyartiproxy": "pyartiproxy"},
    #entry_points={
    #    'console_scripts': [
    #        "pyartiproxy = pyartiproxy:main"
    #    ],
    #},
    python_requires=">=3.7",
    install_requires=requires,
    classifiers=[
        "Development Status :: 5 - Production",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: Proxy Servers",
    ],
)
