from glob import glob
import os
from numpy.core.numeric import NaN
import pandas as pd
import numpy as np
import src.utils as u
import re
import toml
from datetime import date
from dateutil.relativedelta import relativedelta
from pandas import ExcelWriter
import openpyxl

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# get the directory path where this script is
this_dir = os.path.dirname(os.path.realpath(__file__))
# grab the config file from this directory
config = toml.load(os.path.join(this_dir, 'config.toml'))
# prefix partial file paths found in the config.toml with the full path
u.set_full_paths(config, this_dir)

prh_data = pd.read_csv(config['file_locations']['prh_data'])

print(prh_data.columns)
#print(prh_data['What is your age?'].value_counts())
#print(prh_data['Do you have children under the age of 18 living at home with you?'].value_counts(normalize=True))
#print(prh_data['Which of the following best describes where you currently live?'].value_counts(normalize=True))

#print(prh_data['If you had to guess, what is the exact number of books you read in your free time in the past month?'].value_counts(normalize=True))

