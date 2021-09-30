from glob import glob
import os
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

individual_titles = config['file_locations']['individual_titles']
files = sorted(glob(individual_titles))
# reads every csv file that matches a text pattern and puts them all into 1 dataframe
book_data: pd.DataFrame = pd.concat((pd.read_csv(file) for file in files), ignore_index=True)

#separating Products into Title, Additional_Info, and Book_Series
book_data['Products'] = book_data.Products.str.replace('\(with bonus novel\)', '')
book_data[['Title', 'Series']] = book_data.Products.str.split('\(', expand=True)
book_data[['To_Drop', 'Additional_Info']] = book_data.Products.str.split('.*:', expand=True)

#dropping To_Drop and Products and formatting Title/Series/Additional Info
book_data.drop(['To_Drop', 'Products'], 1, inplace=True)
book_data['Title'] = book_data.Title.str.replace(':.*', '')
book_data['Series'] = book_data.Series.str.replace('\)', '')
book_data['Additional_Info'] = book_data.Additional_Info.str.replace('\(.*\)', '')

to_strip = ['Title', 'Series', 'Additional_Info']
for col in to_strip:
  book_data[col] = book_data[col].str.strip()

#separates Series from Series_Number
book_data['Series_Number'] = book_data.Series.str.replace('.*(?<!\d)', '')
book_data['Series'] = book_data.Series.str.replace(',\s\d|\sBook\s\d', '')




#to merge duplicates (allows NaN) - KEEP THIS AFTER THE REST OF THE CLEANING
merge_titles = book_data.groupby(['Title'], dropna=False).sum()

"""
NOTE on merge: will have to add Author to the list when you have it 
Decide on whether to include any other non-int information to this one 
Or if you just want to create a new df for that info as well
"""

"""
TO DO:
-Figure out next steps - 
  -figure out how to add author names and pub dates
  -probably merging all duplicates together... actually wait to do this? 
    -create a different dataframe for it so I can see difference between ebook and print numbers
    -can do this but remember that this data frame's creation needs to be after the original df
    -then make sure everthing that should merge did, 
  -try to figure out subgenres as well
  -try to figure out what to do about books missing the Series_Number

"""


#print(book_data.Series_Number)
#print(book_data)
#print(book_data.loc[book_data.Title.str.contains('Must Love Cowboys'), :])