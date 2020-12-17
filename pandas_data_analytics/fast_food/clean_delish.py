import pandas_data_analytics.utils as u
import re
import toml
from pandas_data_analytics import *
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import functools as ft
from py_linq import Enumerable

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))
u.set_full_paths(config, this_dir)
csv_loc = config['file_locations']['raw_delish']

def get_thing(s, phrase):
  m = re.search(phrase,s)
  return m.group(1) if m is not None\
    else np.nan

def get_sodium(s):
  return get_thing(s, '([,\d]+) [a-zA-Z\s]+ sodium')

def get_sat_fat(s):
  return get_thing(s, '([,\d]+) [a-zA-Z\s]+ saturated fat')

def get_trans_fat(s):
  return get_thing(s, '([,\d]+) [a-zA-Z\s]+ trans fat')

def get_calories(s):
  return get_thing(s, '([,\d]+) calories')

df: pd.DataFrame = pd.read_csv(csv_loc)
df.columns = df.columns.str.lower()
df.drop(['web-scraper-order', 'web-scraper-start-url'], inplace=True, axis=1)
df['company'] = df.name.str.split(':', expand=True)[0]
df['name'] = df.name.str.split(':').apply(lambda l: ':'.join(l[1:])).str.strip()
for (label, fn) in [\
  ('calories', get_calories),\
  ('sodium_in_milligrams', get_sodium),\
  ('trans_fat_in_grams', get_trans_fat),\
  ('sat_fat_in_grams', get_sat_fat)\
    ]:
  df[label] = df.nutrition.apply(fn).str.replace(',', '')

pd.set_option('display.max_rows', df.shape[0]+1)
pd.set_option('display.max_columns', df.shape[1]+1)

ps = (lambda pdf: Enumerable([
  lambda: pdf.sample(5),
  lambda: pdf.columns,
  # lambda: pdf.dtypes,
  # lambda: pdf[['food', 'cal_per_gram', 'category']].groupby('category').food.agg(list),
  # lambda: pdf.category.value_counts(),
]))(df)

u.foreach(lambda f: print(f()),ps)

df.drop('nutrition', inplace=True, axis=1)
df.to_csv(config['file_locations']['clean_delish'], index=False)

# Apply the default theme
sns.set_theme()

# aplot = sns.boxplot(x='category', y='cal_per_gram', data=df)
# General plot stuff
# aplot.set_xticklabels(aplot.get_xticklabels(), rotation=30)
# plt.show()
