To build project:

requires pipenv, python 3.8

With pip:
Create the virutal env:
> python -m venv ~/.virtual/pandas_data_analytics
Launch the virual env:
> source ~/.virtual/pandas_data_analytics/Scripts/activate
One time:
> pip install wheel
Install packages:
> pip install -e .

In project root:

> pipenv shell
> pipenv install -e .
> python <filename>

setup.py with the follow line of code is required for references project files in other project files for import statements
packages=find_packages(include=['python01', 'python01.*']),


# Interactive qtconsole shell
> $ jupyter qtconsole
## loading a python file into the interactive
>> in qtconsole ---> %run <path/to/pythonfile>
