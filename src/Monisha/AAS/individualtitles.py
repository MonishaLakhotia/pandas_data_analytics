from glob import glob
import os
from numpy.core.numeric import NaN
import pandas as pd
import src.utils as u
import re
import toml
from datetime import date
from dateutil.relativedelta import relativedelta

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# get the directory path where this script is
this_dir = os.path.dirname(os.path.realpath(__file__))
# grab the config file from this directory
config = toml.load(os.path.join(this_dir, 'config.toml'))
# prefix partial file paths found in the config.toml with the full path
u.set_full_paths(config, this_dir)

master_doc = pd.read_csv(config['file_locations']['books_master_doc'])
individual_titles = config['file_locations']['individual_titles']
files = sorted(glob(individual_titles))
# reads every csv file that matches a text pattern and puts them all into 1 dataframe
book_data: pd.DataFrame = pd.concat((pd.read_csv(file) for file in files), ignore_index=True)

#separating Products into Title, Additional_Info, and Book_Series
book_data['Products'] = book_data.Products.str.replace('\(with bonus novel\)', '')
book_data[['Title', 'Series']] = book_data.Products.str.split('\(', expand=True)
book_data[['To_Drop', 'Additional_Info']] = book_data.Products.str.split('.*:', expand=True)

#dropping unneeded cols and formatting Title/Series/Additional Info
book_data.drop(['To_Drop', 'Products', 'State', 'SKU', 'ROAS', 'Status'], 1, inplace=True)
book_data['Title'] = book_data.Title.str.replace(':.*', '')
book_data['Series'] = book_data.Series.str.replace('\)', '')
book_data['Additional_Info'] = book_data.Additional_Info.str.replace('\(.*\)', '')

to_strip = ['Title', 'Series', 'Additional_Info']
for col in to_strip:
  book_data[col] = book_data[col].str.strip()

#separates Series from Series_Number
book_data['Series_Number'] = book_data.Series.str.replace('.*(?<!\d)', '')
book_data['Series'] = book_data.Series.str.replace(',\s\d|\sBook\s\d', '')

#renames columns
book_data.rename({'CTR': 'CTR', 
'Spend(USD)': 'Spend', 
'CPC(USD)': 'CPC', 
'Sales(USD)': 'Sales',
'ACOS': 'ACOS'}, axis=1, inplace=True)

#creates Format column
book_data['Format'] = NaN

for index in range(len(book_data.ASIN)):
  if book_data.ASIN[index].startswith('B'):
    book_data.Format[index] = 'eBook'
  elif book_data.ASIN[index].isnumeric() or book_data.ASIN[index].endswith('X'):
    book_data.Format[index] = 'Print'

#merges master doc to fill in missing info
book_data_merge = pd.merge(book_data, master_doc, on=['ASIN', 'Title'])
book_data_merge.drop(columns=['Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8'], inplace=True)

#fixes issue with 44 Chapters//SexLife
book_data_merge.loc[book_data_merge.Title == 'Sex/Life', 'Additional_Info'] = NaN
book_data_merge.loc[book_data_merge.Title == 'Sex/Life', 'Title'] = '44 Chapters About 4 Men'

#changes Pub_Date to datetime
book_data_merge['Pub_Date'] = pd.to_datetime(book_data_merge.Pub_Date).dt.date

#reorders columns
reordered = book_data_merge[['ASIN', 'Title', 'Author', 'Pub_Date', 
'Format', 'Series', 'Series_Number', 'Additional_Info', 
'Assumed_Subgenre', 'First_BISAC_Subject',
'Impressions', 'Clicks', 'Orders', 'Spend', 'Sales',
'CTR',  'CPC', 'ACOS']]

#creates function to fix CTR, CPC, and ACOS when merging and sort by Orders/ACOS - KEEP THIS AFTER THE REST OF THE CLEANING FOR NOW
def agg_functions(df):
  df['CTR'] = df.Clicks / df.Impressions
  df['CPC'] = df.Spend / df.Clicks
  df['ACOS'] = df.Spend / df.Sales
  df.sort_values(['Orders', 'ACOS'], ascending=False, inplace=True)

#to groupby title and author (allows NaN) - KEEP THIS AFTER THE REST OF THE CLEANING
title_author = reordered.groupby(['Title', 'Author'], dropna=False).sum()

d={}
to_groupby = ['Assumed_Subgenre', 'First_BISAC_Subject', 'Format', 'Author']
for series_group in to_groupby:
  df_name = series_group.lower()
  d[df_name] = pd.DataFrame(reordered.groupby(series_group, dropna=False).sum())

"""
NOTE: Delete this red bit once you've successfully saved dataframes, should not need
#to group by subgenre (both assumed and BISAC) (allows NaN)
assumed_subgenre = reordered.groupby('Assumed_Subgenre', dropna=False).sum()
BISAC_subgenre = reordered.groupby('First_BISAC_Subject', dropna=False).sum()

#to group by format (allows NaN)
format = reordered.groupby('Format', dropna=False).sum()

#to group by authors (allows NaN)
authors = reordered.groupby('Author', dropna=False).sum()
"""
#to group by backlist and front list (allows NaN)
six_months = date.today() - relativedelta(months=+6)
backlist = reordered.loc[reordered.Pub_Date < six_months]
backlist_asin_merge = backlist.groupby(['ASIN', 'Title', 'Author', 'Pub_Date'], dropna=False).sum()
frontlist = reordered.loc[reordered.Pub_Date >= six_months]
frontlist_asin_merge = frontlist.groupby(['ASIN', 'Title', 'Author', 'Pub_Date'], dropna=False).sum()

#for loop with agg_functions
dataframes = [reordered, title_author, d['assumed_subgenre'],
d['first_bisac_subject'], d['format'], d['author'], backlist_asin_merge, frontlist_asin_merge]
for df in dataframes:
  agg_functions(df)


""" 
NOTE: Delete this red bit once you've successfully saved dataframes, should not need
#for loop with agg_functions
dataframes = [reordered, title_author, d['assumed_subgenre'],
BISAC_subgenre, format, authors, backlist_asin_merge, frontlist_asin_merge]
for df in dataframes:
  agg_functions(df)
  """





"""
TO DO:
-Figure out next steps - 
  -probably download all and send to self to decide what else is left 
  -didn't do anything with the series numbers
  -issue with the BISAC df - some spacing is off
NOTE
the CTR and ACOS are not in % form, need to multiply by 100 and add percent sign

dfs to print:
reordered (this is the raw data)
title_author (this is best title and author)
assumed_subgenre (this is assumed subgenre)
BISAC_subgenre (this is by BISAC)
format (this is ebook v print)
author (this is authors)

"""