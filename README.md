# Purpose
An area for exploratory data science; to clean, analyze, and visualize data. 

Data sources vary from kaggle.com and personally web scrapped. Formats vary from csv, excel, json, and sql.

# To build project:

requires pipenv(or pip), python 3.8

## In project root (All of these package manager commands):

## With pipenv
### startup
> pipenv shell
### install dependencies
> pipenv install -e .

### tear down
> deactivate

## With pip
### install wheel with pip 
pip install wheel
### To Create a new virtual environment for this project
> python -m venv ~/.virtualenvs/pandas_data_analytics

### startup
> source $HOME/.virtualenvs/pandas_data_analytics/Scripts/activate

### install dependencies
> pip install -e .

### tear down
> deactivate

## Run some code
> python <filename>

setup.py with the follow line of code is required for references project files in other project files for import statements
packages=find_packages(include=['pandas_data_analytics', 'pandas_data_analytics.*']),


# Interactive qtconsole shell
> $ jupyter qtconsole
## loading a python file into the interactive
>> in qtconsole ---> %run <path/to/pythonfile>

# Cool Packages
pipenv:
[packages]
scikit-mdr = "*"
skrebate = "*"
scikit-learn = "*"
joblib = "*"
pandas_data_analytics = {editable = true, path = "."}
toml = "*"
pdpipe = "*"
numpy = "==1.19.3"
pandas = "*"
seaborn = "*"
scipy = "*"
nltk = "*"
xgboost = "==1.1.0"
plotly = "*"
cufflinks = "*"
py-linq = "*"
jupyter = "*"
jupyter-contrib-nbextensions = "*"
qtconsole = "*"
pyqt5 = "*"
pdfplumber = "*"
dask = {extras = ["complete"], version = "*"}
openpyxl = "*"

pip:
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
        "dask",
        "openpyxl"
    ],
