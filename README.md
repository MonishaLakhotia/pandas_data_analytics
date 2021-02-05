To build project:

requires pipenv(or pip), python 3.8

In project root:

startup
> pipenv shell
> pipenv install -e .

tear down
> deactivate

or with pip

startup
> source C:/Users/abhimanyu.lakhotia/.virtualenvs/pandas_data_analytics-T_4TRt4A/Scripts/activate
> pip install -e .
> python <filename>

tear down
> deactivate

setup.py with the follow line of code is required for references project files in other project files for import statements
packages=find_packages(include=['python01', 'python01.*']),


# Interactive qtconsole shell
> $ jupyter qtconsole
## loading a python file into the interactive
>> in qtconsole ---> %run <path/to/pythonfile>
