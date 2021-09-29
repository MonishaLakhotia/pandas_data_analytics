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




#dropping Products and 2
#book_data.drop(columns=['Products', 2], inplace=True)

#print(book_data.Products.str.split())
#print(book_data['Title'])
#print(book_data.Test)
#print(book_data[2].value_counts(dropna=False))
#print(book_data.Additional_Info)
#print(book_data.Book_Series)
#print(book_data.loc[book_data.Book_Series.isna(), 'Products'])
#print(book_data.Products)


"""
TO DO:

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
#print(book_data.loc[book_data.Title.str.contains('Must Love Cowboys'), :])