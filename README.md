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
### install wheel with pip - still unsure how to get wheel message during install to go away
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
Data Science
- pandas # dataframe
- dask # chunks pandas dataframes for scaling. async utils aswell
- sklearn
- scikit-learn # sklearn helper
- scikit-mdr # sklearn helper
- skrebate # sklearn helper
- numpy==1.19.3
- scipy
- xgboost==1.1.0 # gpu
- nltk # Natural Language Toolkit

Data Visualization
- seaborn # charting
- plotly # charting
- cufflinks # charting

Utilities
- joblib # Pickling python Objects
- toml # Config files
- pdpipe # ml pipeline helper
- openpyxl # read excel
- py-linq # LINQ in python
- pdfplumber # pdf reader

Interactive (all required for launching an interactive shell)
- jupyter
- jupyter-contrib-nbextensions
- qtconsole
- pyqt5
