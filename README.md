To build project:

requires pipenv, python 3.8

In project root:

> pipenv shell
> pipenv install -e .
> python <filename>

setup.py with the follow line of code is required for references project files in other project files for import statements
packages=find_packages(include=['python01', 'python01.*']),
