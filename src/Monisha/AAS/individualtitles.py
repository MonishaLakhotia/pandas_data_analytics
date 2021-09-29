from glob import glob
import os
import pandas as pd
import src.utils as u
import re
import toml

#pd.set_option('display.max_rows', None)
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
book_data[['Title', 2]] = book_data.Products.str.split(':', expand=True)
book_data[['Additional_Info', 'Book_Series']] = book_data[2].str.split('(', expand=True)
book_data['Title'] = book_data.Title.str.split('(', expand=True)
book_data['Book_Series'] = book_data.Book_Series.str.replace(')', '')

book_data.drop(columns=['Products', 2], inplace=True)

#print(book_data.loc[book_data.Products.str.contains('Must Love Cowboys'), :])

"""
TO DO:
-Drop Series Products and 2
-Figure out how to split series so book # is it's own series
-Figure out next steps - 
  -add format
  -figure out how to add author names and pub dates
  -probably merging all duplicates together... actually wait to do this? 
    -create a different dataframe for it so I can see difference between ebook and print numbers
    -can do this but remember that this data frame's creation needs to be after the original df
    -then make sure everthing that should merge did, 
  -try to figure out subgenres as well

"""



print(book_data)