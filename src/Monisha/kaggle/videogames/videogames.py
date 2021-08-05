from numpy.core.numeric import NaN
import pandas as pd
import numpy as np
import re
import os
import toml
import src.utils as u

# get the directory path where this script is
this_dir = os.path.dirname(os.path.realpath(__file__))
# grab the config file from this directory
config = toml.load(os.path.join(this_dir, 'config.toml'))
# prefix partial file paths found in the config.toml with the full path
u.set_full_paths(config, this_dir)
#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 200)

vg_df = pd.read_csv(config['file_locations']['vg'])

#filling nan year and publisher
#assuming any repeat copies were published in same year or have same publisher
years_df = vg_df.loc[vg_df.Year.notna(), ['Name', 'Year']]
years_df.drop_duplicates(subset=['Name'], inplace=True)
year_merge = pd.merge(vg_df, years_df, on='Name', how='outer') 
year_merge.drop(columns='Year_x', inplace=True)
year_merge.rename(columns={'Year_y': 'Year'}, inplace=True)

publisher_df = vg_df.loc[vg_df.Publisher.notna(), ['Name', 'Publisher']]
publisher_df.drop_duplicates(subset=['Name'], inplace=True)
publisher_merge = pd.merge(year_merge, publisher_df, on='Name', how='outer')
publisher_merge.drop(columns='Publisher_x', inplace=True)
publisher_merge.rename(columns={'Publisher_y': 'Publisher'}, inplace=True)

#dropping nan values
publisher_merge.dropna(how='any', inplace=True)

#dropping value at 2020 and 2017 - incorrect publication year
publisher_merge.drop(publisher_merge.loc[publisher_merge.Year == 2020, :].index, axis=0, inplace=True)
publisher_merge.drop(publisher_merge.loc[publisher_merge.Year == 2017, :].index, axis=0, inplace=True)

publisher_merge['Year'] = publisher_merge.Year.astype(int)

#total global sales
global_sales_total = publisher_merge.Global_Sales.sum().round(2)
global_sales_total *= 1000000
print('The total global sales are ${}.'.format(global_sales_total))

#best by publisher, genre, platform - based on global sales
list_of_best = ['Publisher', 'Genre', 'Platform']
for value in list_of_best:
  best = publisher_merge.groupby(value).Global_Sales.sum()
  top_five = best.head()
  top_five_index = ', '.join(top_five.index)
  category = value.lower()
  print('The five {}s with the highest global sales are {}.'.format(category, top_five_index))



print(publisher_merge.info())
