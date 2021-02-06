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
        "sklearn",
        "numpy==1.19.3",
        "xgboost==1.1.0",
        "scikit-mdr",
        "skrebate",
        "scikit-learn",
        "joblib",
        "pandas_data_analytics",
        "toml",
        "pdpipe",
        "pandas",
        "seaborn",
        "scipy",
        "nltk",
        "plotly",
        "cufflinks",
        "py-linq",
        "jupyter",
        "jupyter-contrib-nbextensions",
        "qtconsole",
        "pyqt5",
        "pdfplumber",
        "dask"
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ]
)
