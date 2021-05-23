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
csv_loc = config['file_locations']['data']

df: pd.DataFrame = pd.read_csv(csv_loc)
# df.dropna(how='any', inplace=True)
df = df.convert_dtypes()
# for c in ['carbs', 'fat', 'protein']:

#   df[c] = df[c].str.replace('g','')
#   df[c] = df[c].astype('Float64')
# df.fat = df.fat.str.replace('g','')
# df.fat = pd.to_numeric(df.fat)
# df.fat = df.fat.astype(float)
df.fat = df.fat.astype('Int64')
df.protein = df.protein.astype('Int64')
df.carbs = df.carbs.astype('Int64')
pd.set_option('display.max_rows', df.shape[0] + 1)
pd.set_option('display.max_columns', df.shape[1] + 1)
df.dropna(how='any', inplace=True)

df = df[['food_cat', 'name', 'calories', 'fat', 'protein', 'carbs']]


def salad_bin(r):
  food_cat = "salad" if re.search('salad', r['name'], re.I) else\
    r['food_cat']
  r['food_cat'] = food_cat
  return r


# df = df.apply(salad_bin, axis=1)
df['carbs_marco_ratio'] = df.carbs / (df.carbs + df.protein + df.fat)

mdf = pd.melt(
  df,
  id_vars=[
    'food_cat',
    'name'],
    value_vars=[
      'protein',
      'carbs',
      'fat'],
    value_name='grams',
    var_name='gram_category')

pdf = df
ps = Enumerable([
  # lambda: pdf[pdf.name.str.contains('Salad', flags = re.I)].name,
  # lambda: pdf.groupby('food_cat').carbs_marco_ratio.count(),
  lambda: pdf.columns,
  # lambda: pdf.sort_values('calories')
])

u.foreach(lambda f: print(f()), ps)
# df.to_csv(config['file_locations']['data'])

# Apply the default theme
sns.set_theme()

# aplot = sns.boxplot(y='food_cat', x='carbs_marco_ratio', data=df)
aplot = sns.boxplot(y='food_cat', x='calories', data=df)
# aplot = sns.barplot(y='food_cat', x='grams', hue='gram_category', data=mdf)
# General plot stuff
# aplot.set_xticklabels(aplot.get_xticklabels(), rotation=30)
plt.show()

# El Pollo Loco Menu Analysis
# Data scraped from https://www.elpolloloco.com/ using webscraper.io
# Data figures created using pandas in python
# Thread will be populated with more metrics
