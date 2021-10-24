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
csv_loc = config['file_locations']['raw_nourish_7and7']

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


def get_sat_fat(s):
  m = get_thing(s, '(\\d+[\\d,\\.]+)[\\sa-zA-Z]*?saturated fat')
  return m if not pd.isna(m)\
      else get_thing(s, 'saturated fat[\\sa-zA-Z]\\((\\d+[\\d,\\.]+)[\\sa-zA-Z]*?\\)')


def get_fat(s):
  m = get_thing(s, '(\\d+[\\d,\\.]+)[\\sa-zA-Z]*?fat')
  return m if not pd.isna(m)\
      else get_thing(s, 'fat \\((\\d+[\\d,\\.]+)[\\sa-zA-Z]*?\\)')


def get_calories(s):
  m = get_thing(s, '(\\d+[\\d,\\.]+)[\\sa-zA-Z]*?calories')
  return m if not pd.isna(m)\
      else get_thing(s, 'calories[\\sa-zA-Z]\\((\\d+[\\d,\\.]+)[\\sa-zA-Z]*?\\)')


def get_sugar(s):
  m = get_thing(s, '(\\d+[\\d,\\.]+)[\\sa-zA-Z]*?sugar')
  return m if not pd.isna(m)\
      else get_thing(s, 'sugar[\\sa-zA-Z]\\((\\d+[\\d,\\.]+)[\\sa-zA-Z]*?\\)')


def get_company(s):
  m = re.search('^(.*?):', s, re.I)
  if m is not None:
    return m.group(1)
  return np.nan


for (label, fn) in [
  ('calories', get_calories),
  ('sodium_in_milligrams', get_sodium),
  ('sat_fat_in_grams', get_sat_fat),
  ('fat_in_grams', get_fat)
]:
  df[label] = df.descr.apply(fn).str.replace(',', '')

df['company'] = df.name.apply(get_company).str.replace('\'', '').str.replace('’', '')
df.name = df.other_name_from_body

df.drop(['other_name_from_body', 'web-scraper-order', 'web-scraper-start-url'], inplace=True, axis=1)

pd.set_option('display.max_rows', df.shape[0] + 1)
pd.set_option('display.max_columns', df.shape[1] + 1)

df['sodium_units'] = 'mg'
df['fat_units'] = 'g'
df['sat_fat_units'] = 'g'
df.columns = df.columns.str.replace('_in_(?:milli)?grams', '', regex=True)

pdf = df
ps = Enumerable([
  lambda: pdf.columns,
  lambda: pdf,
])
u.foreach(lambda f: print(f()), ps)

df.to_csv(config['file_locations']['clean_nourish_7and7'], index=False)
