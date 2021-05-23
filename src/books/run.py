from glob import glob
import os
import pandas as pd
import pandas_data_analytics.utils as u
import re
import toml

# get the directory path where this script is
this_dir = os.path.dirname(os.path.realpath(__file__))
# grab the config file from this directory
config = toml.load(os.path.join(this_dir, 'config.toml'))
# prefix partial file paths found in the config.toml with the full path
u.set_full_paths(config, this_dir)

# Currently not using the book references
# book_refs_csv_loc = config['file_locations']['book_refs']
# book_refs: pd.DataFrame = pd.read_csv(book_refs_csv_loc)

partitioned_book_data_pattern = config['file_locations']['partitioned_book_data_pattern']
files = sorted(glob(partitioned_book_data_pattern))
# reads every csv file that matches a text pattern and puts them all into 1 dataframe
book_data: pd.DataFrame = pd.concat((pd.read_csv(file) for file in files), ignore_index=True)

# function to parse the product field
# parse_products : row -> row
def parse_products(r):
  m = re.search('(.+)\((.*)(?:Book|,)(.*?)\)', r['Products'], re.I)
  if m:
    r['book_title'] = m.group(1).strip()
    r['book_series'] = m.group(2).strip()
    r['book_number'] = m.group(3).strip()
  else:
    m = re.search('(.+)(Box Set Books (.*):(.*))', r['Products'], re.I)
    if m:
      r['book_title'] = m.group(1).strip()
      r['book_series'] = m.group(4).strip()
      r['book_number'] = m.group(3).strip()
    else:
      r['book_title'] = r['Products']
      r['book_series'] = None
      r['book_number'] = None
  return r

# non pandas way
# book_data = book_data.apply(parse_products, axis=1)

# pandas way
book_data[['book_title', 'book_series', 'book_number']] = book_data.Products\
  .str.replace('(.+)\((.*)(?:Book|,)(.*?)\)', r'\1<:>\2<:>\3', regex=True, flags=re.I)\
  .str.replace('(.+)(Box Set Books (.*):(.*))', r'\1<:>\4<:>\3', regex=True, flags=re.I)\
  .str.split('<:>', expand=True)

book_data[book_data['book_title'].isna()] = book_data['Products']
for c in ['book_title', 'book_series', 'book_number']:
  book_data[c] = book_data[c].str.strip()

# sets display options for the dataframe
pd.set_option('display.max_rows', book_data.shape[0]+1)
pd.set_option('display.max_columns', 10000)
pd.set_option('display.max_colwidth', 200)

# display metrics/data
pdf: pd.DataFrame = book_data
ps = [
  lambda: pdf.sample(5)
  # lambda: pdf.Products.sort_values()
  # lambda: pdf.dtypes,
]
u.foreach(lambda f: print(f()),ps)

# Write the cleaned data to a file
book_data.to_csv(config['file_locations']['cleaned_data'], index=False)
