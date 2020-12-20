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
csv_loc = config['file_locations']['raw_el_pollo_loco']

df: pd.DataFrame = pd.read_csv(csv_loc)
df.columns = df.columns.str.lower()

for label in ['fat', 'protein', 'carbs']:
  df[label] = df[label].str.split('g', expand=True)[0]

df['calories'] = df.calories.astype('Int64')
df['category'] = df.main_food_link
df.drop(['web-scraper-order', 'web-scraper-start-url', 'main_food_link', 'main_food_link-href'], inplace=True, axis=1)
df['company'] = 'El Pollo Loco'
df.dropna(inplace=True, axis=0, subset=['calories'])
df['serving_size_unit'] = df.serving_size.str.split(' ', expand=True)[1]
df['serving_size'] = df.serving_size.str.split(' ', expand=True)[0]

pd.set_option('display.max_rows', df.shape[0]+1)
pd.set_option('display.max_columns', df.shape[1]+1)

df['fat_units'] = 'g'
df['protein_units'] = 'g'
df['carb_units'] = 'g'

ps = (lambda pdf: Enumerable([
  # lambda: pdf[['name']],
  lambda: pdf.columns,
  lambda: pdf.serving_size_unit.value_counts(dropna=False),
  lambda: pdf.sample(10),
  # lambda: pdf[['food', 'cal_per_gram', 'category']].groupby('category').food.agg(list),
  # lambda: pdf.category.value_counts(),
]))(df)
u.foreach(lambda f: print(f()),ps)

# df.to_csv(config['file_locations']['clean_el_pollo_loco'], index=False)
