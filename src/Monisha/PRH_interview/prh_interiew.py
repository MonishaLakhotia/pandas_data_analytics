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

#print(prh_data.columns)
#print(prh_data['What is your age?'].value_counts())
#print(prh_data['Do you have children under the age of 18 living at home with you?'].value_counts(normalize=True))
#print(prh_data['Which of the following best describes where you currently live?'].value_counts(normalize=True))
#print(prh_data['If you had to guess, what is the exact number of books you read in your free time in the past month?'].value_counts(normalize=True))
#print(prh_data['Please share with us the title and author of a book you read in the past month: Author'].value_counts())

#print(prh_data.loc[:, prh_data.columns.str.contains('What reasons best describe why you read or listened to books in the past month?')].value_counts())

#to separate reasons for reading into a new dataframe
reasons_for_reading = prh_data.loc[:, prh_data.columns.str.contains('What reasons best describe why you read or listened to books in the past month?')]
reasons_for_reading.columns = reasons_for_reading.columns.str.replace('What reasons best describe why you read or listened to books in the past month\? Select all that apply: ', '')
reasons_for_reading.fillna('No', inplace=True)

columns = ['For pleasure/entertainment', 'To keep up with my hobbies/interests',
       'To connect with my favorite authors', 'To relax/unwind',
       'For self-improvement', 'To learn about new subjects/ideas',
       'To read with my child', 'To pass the time',
       'To connect with other people�s experiences',
       'To talk about them with friends/family']

for col in columns:
  reasons_for_reading.loc[reasons_for_reading[col] != 'No', col] = 'Yes'

reasons_for_reading_t = reasons_for_reading.transpose()
reasons_for_reading_t['Yes'] = (reasons_for_reading_t.iloc[:, :] == 'Yes').sum(axis=1)
reasons_for_reading_t['No'] = (reasons_for_reading_t.iloc[:, :] == 'No').sum(axis=1)
reasons_for_reading_t.drop(reasons_for_reading_t.loc[:, 0:149], axis=1, inplace=True)
reasons_for_reading_t['Total'] = reasons_for_reading_t.Yes + reasons_for_reading_t.No
reasons_for_reading_t['Percent_Yes'] = reasons_for_reading_t.Yes / reasons_for_reading_t.Total
reasons_for_reading_t.sort_values('Percent_Yes', inplace=True, ascending=False)

print(reasons_for_reading_t)
