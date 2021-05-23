from setuptools import setup, find_packages
# -*- coding: utf-8 -*-

# from distutils.core import setup


try:
  long_description = open("README.rst").read()
except IOError:
  long_description = ""

setup(
    name="pandas_data_analytics",
    version="0.1.0",
    description="A pip package",
    license="MIT",
    author="manyu",
    packages=find_packages(
        include=['pandas_data_analytics', 'pandas_data_analytics.*']),
    install_requires=[
        "numpy==1.19.3",
        "pandas_data_analytics",
        "toml",
        "pandas",
        "seaborn",
        "py-linq",
        "pdfplumber",
        "openpyxl",
        "pyodbc",
        "qtconsole",
        "jupyter",
        "jupyter-contrib-nbextensions",
        "pyqt5",
        "autopep8"
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ]
)
