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

#to get value counts
#print(prh_data.columns)
#print(prh_data['What is your age?'].value_counts())
#print(prh_data['Do you have children under the age of 18 living at home with you?'].value_counts(normalize=True))
#print(prh_data['Which of the following best describes where you currently live?'].value_counts(normalize=True))
#print(prh_data['If you had to guess, what is the exact number of books you read in your free time in the past month?'].value_counts(normalize=True))
#print(prh_data['Please share with us the title and author of a book you read in the past month: Author'].value_counts())
#print(prh_data['How likely are you to purchase a book in the next month?'].value_counts(normalize=True))
#print(prh_data.loc[:, prh_data.columns.str.contains('What reasons best describe why you read or listened to books in the past month?')].value_counts())

#function to format transposed df
def format_transposed(df):
  df['Yes'] = (df.iloc[:, :] == 'Yes').sum(axis=1)
  df['No'] = (df.iloc[:, :] == 'No').sum(axis=1)
  df.drop(df.loc[:, 0:149], axis=1, inplace=True)
  df['Total'] = df.Yes + df.No
  df['Percent_Yes'] = df.Yes / df.Total
  df.sort_values('Percent_Yes', inplace=True, ascending=False)

#to separate reasons for reading into a new dataframe
reasons_for_reading = prh_data.loc[:, prh_data.columns.str.contains('What reasons best describe why you read or listened to books in the past month?')]
reasons_for_reading.columns = reasons_for_reading.columns.str.replace('What reasons best describe why you read or listened to books in the past month\? Select all that apply: ', '')
reasons_for_reading.fillna('No', inplace=True)

reasons_columns = ['For pleasure/entertainment', 'To keep up with my hobbies/interests',
       'To connect with my favorite authors', 'To relax/unwind',
       'For self-improvement', 'To learn about new subjects/ideas',
       'To read with my child', 'To pass the time',
       'To connect with other people�s experiences',
       'To talk about them with friends/family']

for col in reasons_columns:
  reasons_for_reading.loc[reasons_for_reading[col] != 'No', col] = 'Yes'

reasons_for_reading_t = reasons_for_reading.transpose()

#filters out how did you find out about books
find_out_about_books = prh_data.loc[:, prh_data.columns.str.contains('In the past month, how did you find out about books to read?')]
find_out_about_books.columns = find_out_about_books.columns.str.replace('.*: ', '', regex=True)
find_out_about_books.fillna('No', inplace=True)

find_out_columns = ['Recommendations from family/ friends',
       'Recommendations from a media source (e.g., magazines, newspapers, etc.)',
       'Professional book reviews', 'Customer reviews', 'Bestseller lists',
       'Online author interview',
       'Retailer recommendation based on what I�ve read before',
       'Websites/blogs about books', 'In my bookcase/already had the book',
       'Browsing in person in a physical store',
       'Browsing in person in a library']

for col in find_out_columns:
  find_out_about_books.loc[find_out_about_books[col] != 'No', col] = 'Yes'

find_out_about_books_t = find_out_about_books.transpose()

#filters out acquire books
aquire_books = prh_data.loc[:, prh_data.columns.str.contains('In the past month, where did you acquire books for your household?')]
aquire_books.columns = aquire_books.columns.str.replace('.*: ', '', regex=True)
aquire_books.fillna('No', inplace=True)

aquire_cols = ['Amazon', 'Audible', 'Barnes and Noble', 'Bookbub', 'Books-a-Million',
       'Borrowed from family/friends', 'Costco', 'Kindle/Kindle Unlimited',
       'Library', 'Local independent bookstore', 'Target', 'Walmart']

for col in aquire_cols:
  aquire_books.loc[aquire_books[col] != 'No', col] = 'Yes'

aquire_books_t = aquire_books.transpose()

#filters out after reading
after_reading = prh_data.loc[:, prh_data.columns.str.contains('After reading a book last month, which of the following actions')]
after_reading.columns = after_reading.columns.str.replace('.*: ', '', regex=True)
after_reading.fillna('No', inplace=True)

after_reading_cols = ['None of the above',
       'Wrote a review online (e.g. on Amazon, Goodreads, etc.)',
       'Gave stars/a rating to the book online (e.g. on Amazon, Barnes & Noble, etc.)',
       'Posted on social media about the book',
       'Discussed the book in person with others',
       'Discussed the book in a virtual book club',
       'Discussed the book on a blog or forum',
       'Gave the book to someone else to read']

for col in after_reading_cols:
  after_reading.loc[after_reading[col] != 'No', col] = 'Yes'

after_reading_t = after_reading.transpose()

#types of fiction
fiction = prh_data.loc[:, prh_data.columns.str.contains('What types of fiction are you planning to read next month?')]
fiction.columns = fiction.columns.str.replace('.*: ', '', regex=True)
fiction.fillna('No', inplace=True)

fiction_cols = ['Not planning to read any fiction', 'Espionage/Thriller', 'Mystery',
       'Horror', 'Science Fiction', 'Fantasy', 'Humor', 'Classics', 'Romance',
       'Literary Fiction', 'Young Adult', 'Women\'s Fiction', 'Children�s',
       'Historical Fiction', 'Poetry']

for col in fiction_cols:
  fiction.loc[fiction[col] != 'No', col] = 'Yes'

fiction_t = fiction.transpose()

#types of nonfiction
nonfiction = prh_data.loc[:, prh_data.columns.str.contains('What types of non-fiction are you planning to read next month?')]
nonfiction.columns = nonfiction.columns.str.replace('.*: ', '', regex=True)
nonfiction.fillna('No', inplace=True)

nonfiction_cols = ['Not planning to read any non-fiction', 'Biography/Autobiography',
       'Cooking', 'Diet/Fitness', 'Health & Wellness',
       'Music/Film/Performing Arts', 'Business/Management/Economics',
       'History', 'Politics/Current events', 'Social justice/Antiracism',
       'Self-help/Psychology', 'Study guides/Educational', 'Reference',
       'Religion & Inspirational', 'Arts & Crafts']

for col in nonfiction_cols:
  nonfiction.loc[nonfiction[col] != 'No', col] = 'Yes'

nonfiction_t = nonfiction.transpose()


#print(prh_data.loc[prh_data['What types of fiction are you planning to read next month? Select all that apply: Romance'].notna(), :])
"""
NOTE: Run format_transpose on all at end of thing

reasons_for_reading_t
find_out_about_books_t
aquire_books_t
after_reading
fiction
"""