# -*- coding: utf-8 -*-

# from distutils.core import setup

from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="python01",
    version="0.1.0",
    description="A pip package",
    license="MIT",
    author="manyu",
    packages=find_packages(include=['python01', 'python01.*']),
    install_requires=[
        "tpot",
        "sklearn"
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ]
)
