from glob import glob
import os
from numpy.core.numeric import NaN
import pandas as pd
import src.utils as u
import re
import toml

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
book_data_merge['Pub_Date'] = pd.to_datetime(book_data_merge.Pub_Date)

#reorders columns
reordered = book_data_merge[['ASIN', 'Title', 'Author', 'Pub_Date', 
'Format', 'Series', 'Series_Number', 'Additional_Info', 
'Assumed_Subgenre', 'First_BISAC_Subject',
'Impressions', 'Clicks', 'Orders', 'Spend', 'Sales',
'CTR',  'CPC', 'ACOS']]

#creates function to fix CTR, CPC, and ACOS when merging - KEEP THIS AFTER THE REST OF THE CLEANING FOR NOW
def agg_functions(df):
  df['CTR'] = df.Clicks / df.Impressions
  df['CPC'] = df.Spend / df.Clicks
  df['ACOS'] = df.Spend / df.Sales
  df.sort_values(['Orders', 'ACOS'], ascending=False, inplace=True)

#to groupby title and author (allows NaN) - KEEP THIS AFTER THE REST OF THE CLEANING
title_author = reordered.groupby(['Title', 'Author'], dropna=False).sum()
agg_functions(title_author)


"""
NOTE on merge: will have to add Author to the list when you have it 
Decide on whether to include any other non-int information to this one 
Or if you just want to create a new df for that info as well

"""

"""
TO DO:
-Figure out next steps - 
  -need to do the ASIN merge I think too
  -decide if you want to create new dfs for other info like subgenre or ebook v print
  or if you want to merge some of the into the merge df as well
NOTE
the CTR and ACOS are not in % form, need to multiply by 100 and add percent sign

"""