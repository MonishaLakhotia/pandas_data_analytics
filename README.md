To build project:

requires pipenv(or pip), python 3.8

In project root:

With pipenv:
> pipenv shell
> pipenv install -e .

With pip:
Create the virutal env:
> python -m venv ~/.virtual/pandas_data_analytics
Launch the virual env:
> source ~/.virtual/pandas_data_analytics/Scripts/activate
One time:
> pip install wheel
Install packages:
> pip install -e .

Run code:
> python <filename>
setup.py with the follow line of code is required for references project files in other project files for import statements
packages=find_packages(include=['python01', 'python01.*']),


# Interactive qtconsole shell
> $ jupyter qtconsole
## loading a python file into the interactive
>> in qtconsole ---> %run <path/to/pythonfile>
