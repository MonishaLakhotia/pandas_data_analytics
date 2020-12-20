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
csv_loc = config['file_locations']['raw_mens_health_40_worst']

df: pd.DataFrame = pd.read_csv(csv_loc)
df.columns = df.columns.str.lower()

def get_thing(s, phrase):
  m = re.search(phrase,s)
  return m.group(1) if m is not None\
    else np.nan
def get_sodium(s):
  m = get_thing(s, '(\d+[\d,\.]+)[\sa-zA-Z]*?sodium')
  return m if not pd.isna(m)\
    else get_thing(s, 'sodium[\sa-zA-Z]\((\d+[\d,\.]+)[\sa-zA-Z]*?\)')
def get_sat_fat(s):
  m = get_thing(s, '(\d+[\d,\.]+)[\sa-zA-Z]*?saturated fat')
  return m if not pd.isna(m)\
    else get_thing(s, 'saturated fat[\sa-zA-Z]\((\d+[\d,\.]+)[\sa-zA-Z]*?\)')
def get_fat(s):
  m = get_thing(s, '(\d+[\d,\.]+)[\sa-zA-Z]*?fat')
  return m if not pd.isna(m)\
    else get_thing(s, 'fat \((\d+[\d,\.]+)[\sa-zA-Z]*?\)')
def get_calories(s):
  m = get_thing(s, '(\d+[\d,\.]+)[\sa-zA-Z]*?calories')
  return m if not pd.isna(m)\
    else get_thing(s, 'calories[\sa-zA-Z]\((\d+[\d,\.]+)[\sa-zA-Z]*?\)')
def get_sugar(s):
  m = get_thing(s, '(\d+[\d,\.]+)[\sa-zA-Z]*?sugar')
  return m if not pd.isna(m)\
    else get_thing(s, 'sugar[\sa-zA-Z]\((\d+[\d,\.]+)[\sa-zA-Z]*?\)')

def remove_company(s):
  return re.sub('Chili\'s', '', s, flags=re.I) if re.search('Chili\'s', s, re.I)\
    else re.sub('Sonic', '', s, flags=re.I) if re.search('Sonic', s, re.I)\
    else re.sub('AMC Theaters', '', s, flags=re.I) if re.search('AMC Theaters', s, re.I)\
    else re.sub('Wendy\'s', '', s, flags=re.I) if re.search('Wendy\'s', s, re.I)\
    else re.sub('Panera Bread', '', s, flags=re.I) if re.search('Panera Bread', s, re.I)\
    else re.sub('Romano’s', '', s, flags=re.I) if re.search('Romano’s', s, re.I)\
    else re.sub('Checkers\'', '', s, flags=re.I) if re.search('Checkers\'', s, re.I)\
    else re.sub('Jimmy John\'s', '', s, flags=re.I) if re.search('Jimmy John\'s', s, re.I)\
    else re.sub('McDonald\'s', '', s, flags=re.I) if re.search('McDonald\'s', s, re.I)\
    else re.sub('Arby’s', '', s, flags=re.I) if re.search('Arby’s', s, re.I)\
    else re.sub('Outback Steakhouse', '', s, flags=re.I) if re.search('Outback Steakhouse', s, re.I)\
    else re.sub('Applebee\'s', '', s, flags=re.I) if re.search('Applebee\'s', s, re.I)\
    else re.sub('KFC', '', s, flags=re.I) if re.search('KFC', s, re.I)\
    else re.sub('(?: The )?Cheesecake Factory', '', s, flags=re.I) if re.search('Cheesecake Factory', s, re.I)\
    else re.sub('Carl\'s Jr\'s', '', s, flags=re.I) if re.search('Carl\'s Jr\'s', s, re.I)\
    else re.sub('Yard House', '', s, flags=re.I) if re.search('Yard House', s, re.I)\
    else re.sub('BJ\'s Restaurant & Brewhouse', '', s, flags=re.I) if re.search('BJ\'s Restaurant & Brewhouse', s, re.I)\
    else re.sub('El Pollo Loco', '', s, flags=re.I) if re.search('El Pollo Loco', s, re.I)\
    else re.sub('In N\' Out', '', s, flags=re.I) if re.search('In N\' Out', s, re.I)\
    else re.sub('Dunkin Donut\'s', '', s, flags=re.I) if re.search('Dunkin Donut\'s', s, re.I)\
    else re.sub('Corner Bakery', '', s, flags=re.I) if re.search('Corner Bakery', s, re.I)\
    else re.sub('IHOP\'s', '', s, flags=re.I) if re.search('IHOP\'s', s, re.I)\
    else re.sub('Olive Garden(?:\'s)?', '', s, flags=re.I) if re.search('Olive Garden', s, re.I)\
    else re.sub('Uno Pizzeria & Grill', '', s, flags=re.I) if re.search('Uno Pizzeria & Grill', s, re.I)\
    else re.sub('Taco Bell', '', s, flags=re.I) if re.search('Taco Bell', s, re.I)\
    else re.sub('Jack In The Box', '', s, flags=re.I) if re.search('Jack In The Box', s, re.I)\
    else re.sub('Schlotzsky’s', '', s, flags=re.I) if re.search('Schlotzsky’s', s, re.I)\
    else re.sub('Subway', '', s, flags=re.I) if re.search('Subway', s, re.I)\
    else re.sub('Burger King', '', s, flags=re.I) if re.search('Burger King', s, re.I)\
    else re.sub('Shake Shack', '', s, flags=re.I) if re.search('Shake Shack', s, re.I)\
    else np.nan

def get_company(s):
  return 'Chilis' if re.search('Chili\'s', s, re.I)\
    else 'Sonic' if re.search('Sonic', s, re.I)\
    else 'AMC Theaters' if re.search('AMC Theaters', s, re.I)\
    else 'Wendys' if re.search('Wendy\'s', s, re.I)\
    else 'Panera Bread' if re.search('Panera Bread', s, re.I)\
    else 'Romanos' if re.search('Romano’s', s, re.I)\
    else 'Checkers' if re.search('Checkers\'', s, re.I)\
    else 'Jimmy Johns' if re.search('Jimmy John\'s', s, re.I)\
    else 'McDonalds' if re.search('McDonald\'s', s, re.I)\
    else 'Arbys' if re.search('Arby’s', s, re.I)\
    else 'Outback Steakhouse' if re.search('Outback Steakhouse', s, re.I)\
    else 'Applebees' if re.search('Applebee\'s', s, re.I)\
    else 'KFC' if re.search('KFC', s, re.I)\
    else 'Cheesecake Factory' if re.search('Cheesecake Factory', s, re.I)\
    else 'Carls Jrs' if re.search('Carl\'s Jr\'s', s, re.I)\
    else 'Yard House' if re.search('Yard House', s, re.I)\
    else 'BJs Restaurant & Brewhouse' if re.search('BJ\'s Restaurant & Brewhouse', s, re.I)\
    else 'El Pollo Loco' if re.search('El Pollo Loco', s, re.I)\
    else 'In N Out' if re.search('In N\' Out', s, re.I)\
    else 'Dunkin Donuts' if re.search('Dunkin Donut\'s', s, re.I)\
    else 'Corner Bakery' if re.search('Corner Bakery', s, re.I)\
    else 'IHOPs' if re.search('IHOP\'s', s, re.I)\
    else 'Olive Garden' if re.search('Olive Garden', s, re.I)\
    else 'Uno Pizzeria & Grill' if re.search('Uno Pizzeria & Grill', s, re.I)\
    else 'Taco Bell' if re.search('Taco Bell', s, re.I)\
    else 'Jack In The Box' if re.search('Jack In The Box', s, re.I)\
    else 'Schlotzskys' if re.search('Schlotzsky’s', s, re.I)\
    else 'Subway' if re.search('Subway', s, re.I)\
    else 'Burger King' if re.search('Burger King', s, re.I)\
    else 'Shake Shack' if re.search('Shake Shack', s, re.I)\
    else np.nan

for (label, fn) in [\
  ('calories', get_calories),\
  ('sodium_in_milligrams', get_sodium),\
  ('sat_fat_in_grams', get_sat_fat),\
  ('sugar_in_grams', get_sugar),\
  ('fat_in_grams', get_fat)\
    ]:
  df[label] = df.descr.apply(fn).str.replace(',', '')

df['company'] = df.name.apply(get_company)
df.name = df.name.apply(remove_company).str.strip()

df.drop(['web-scraper-order', 'web-scraper-start-url'], inplace=True, axis=1)
df['rank_out_of'] = len(df)

pd.set_option('display.max_rows', df.shape[0]+1)
pd.set_option('display.max_columns', df.shape[1]+1)

df['sodium_units'] = 'mg'
df['fat_units'] = 'g'
df['sat_fat_units'] = 'g'
df['sugar_units'] = 'g'
df.columns = df.columns.str.replace('_in_(?:milli)?grams', '', regex=True)

pdf = df
ps = Enumerable([
  # lambda: pdf[['name']],
  lambda: pdf.columns,
  lambda: pdf,
  # lambda: pdf[['food', 'cal_per_gram', 'category']].groupby('category').food.agg(list),
  # lambda: pdf.category.value_counts(),
])
u.foreach(lambda f: print(f()),ps)

# df.to_csv(config['file_locations']['clean_mens_health_40_worst'], index=False)
