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
### To Create a new virtual environment for this project
> python3 -m venv /path/to/new/virtual/environment

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
