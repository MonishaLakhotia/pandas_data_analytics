import src.utils as u
import re
import toml
from src import *
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
csv_loc = config['file_locations']['raw_nourish_worst_rest']

df: pd.DataFrame = pd.read_csv(csv_loc)
df.columns = df.columns.str.lower()


def get_thing(s, phrase):
  m = re.search(phrase, s)
  return m.group(1) if m is not None\
      else np.nan


def get_sodium(s):
  m = get_thing(s, '(\\d+[\\d,\\.]+)[\\sa-zA-Z]*?sodium')
  return m if not pd.isna(m)\
      else get_thing(s, 'sodium[\\sa-zA-Z]\\((\\d+[\\d,\\.]+)[\\sa-zA-Z]*?\\)')


def get_fat(s):
  m = get_thing(s, '(\\d+[\\d,\\.]+)[\\sa-zA-Z]*?fat')
  return m if not pd.isna(m)\
      else get_thing(s, 'fat \\((\\d+[\\d,\\.]+)[\\sa-zA-Z]*?\\)')


def get_calories(s):
  m = get_thing(s, '(\\d+[\\d,\\.]+)[\\sa-zA-Z]*?calories')
  return m if not pd.isna(m)\
      else get_thing(s, 'calories[\\sa-zA-Z]\\((\\d+[\\d,\\.]+)[\\sa-zA-Z]*?\\)')


for (label, fn) in [
  ('calories', get_calories),
  ('sodium_in_milligrams', get_sodium),
  ('fat_in_grams', get_fat)
]:
  df[label] = df.nutrition.apply(fn).str.replace(',', '')

df.drop(['web-scraper-order', 'web-scraper-start-url'], inplace=True, axis=1)

pd.set_option('display.max_rows', df.shape[0] + 1)
pd.set_option('display.max_columns', df.shape[1] + 1)

df['sodium_units'] = 'mg'
df['fat_units'] = 'g'
df.columns = df.columns.str.replace('_in_(?:milli)?grams', '', regex=True)

pdf = df
ps = Enumerable([
  lambda: pdf.columns,
  lambda: pdf,
])
u.foreach(lambda f: print(f()), ps)

# df.to_csv(config['file_locations']['clean_nourish_worst_rest'], index=False)
