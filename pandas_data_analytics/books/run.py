from pandas_data_analytics import *
from py_linq import Enumerable
import datetime
import functools as ft
import json
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pandas_data_analytics.utils as u
import re
import seaborn as sns
import toml
from glob import glob

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))
u.set_full_paths(config, this_dir)

partitioned_book_data_pattern = config['partitioned_book_data_pattern']
files = sorted(glob(partitioned_book_data_pattern))
book_refs_csv_loc = config['file_locations']['book_refs']

book_refs: pd.DataFrame = pd.read_csv(book_refs_csv_loc)
book_data: pd.DataFrame = pd.concat((pd.read_csv(file) for file in files), ignore_index=True)
def parse_products(r):
  m = re.search('(.+)\((.*)(?:Book|,)(.*?)\)', r['Products'], re.I)
  if m:
    r['book_title'] = m.group(1).strip()
    r['book_series'] = m.group(2).strip()
    r['book_number'] = m.group(3).strip()
  else:
    m = re.search('(.+)(Box Set Books 1-3(.*))', r['Products'], re.I)
    if m:
      r['book_title'] = m.group(1)
      r['book_series'] = m.group(2)
    else:
    r['book_title'] = None
    r['book_series'] = None
    r['book_number'] = None
  return r


  # food_cat = "salad" if re.search('salad', r['Products'], re.I) else\
  #   r['food_cat']
  # r['food_cat'] = food_cat
  # return r
book_data = book_data.apply(parse_products, axis=1)
# df = df.convert_dtypes()

pd.set_option('display.max_rows', book_data.shape[0]+1)
pd.set_option('display.max_columns', 10000)
pd.set_option('display.max_colwidth', 200)
# State,Products,Status,SKU,ASIN,Impressions,Clicks,CTR,Spend(USD),CPC(USD),Orders,Sales(USD),ACOS,ROAS
# State,Products,Status,SKU,ASIN,Impressions,Clicks,CTR,Spend(USD),CPC(USD),Orders,Sales(USD),ACOS,ROAS
# State,Products,Status,SKU,ASIN,Impressions,Clicks,CTR,Spend(USD),CPC(USD),Orders,Sales(USD),ACOS,ROAS

# g1 = book title
# g2 = book series
# g3 = the number that this book is in the book series
# Only works for entries like:
# (.+)\((.*?)(?:Book|,)(.*?)\)
# A Good Duke Is Hard to Find (Isle of Synne Book 1)
# A Good Duke Is Hard to Find (Isle of Synne, 1)
# not books like:
# A Christmas to Remember
# The O'Malleys Box Set Books 1-3

pdf: pd.DataFrame = book_data
ps = Enumerable([
  # lambda: book_refs,
  # lambda: pdf.columns,
  # lambda: pdf['Products'],
  lambda: pdf.sample(5)
  # lambda: pdf.Products.sort_values()
  # lambda: pdf.dtypes,
])
u.foreach(lambda f: print(f()),ps)

# Apply the default theme
sns.set_theme()

# aplot = sns.barplot(x='date_range', y='lbs', hue='weight_category', data=mdf)
# aplot = sns.boxplot(x='date_range', y='calories', data=df)

# General plot stuff
# aplot.set_xticklabels(aplot.get_xticklabels(), rotation=30)
# plt.show()
