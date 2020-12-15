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
pd.set_option('display.max_rows', df.shape[0]+1)
pd.set_option('display.max_columns', df.shape[1]+1)
df.dropna(how='any', inplace=True)

# def f(s):
#   print(s)
#   if(s == np.nan):
#     return s
#   return np.nan if(re.match('Loading...',s,re.I))\
#     else s
# df.name = df.name.apply(f)
df = df[['food_cat', 'name', 'calories','fat','protein','carbs']]

def salad_bin(r):
  food_cat = "salad" if re.search('salad', r['name'], re.I) else\
    r['food_cat']
  r['food_cat'] = food_cat
  return r
df = df.apply(salad_bin, axis=1)
df['carbs_marco_ratio'] = df.carbs / (df.carbs + df.protein + df.fat)

ps = (lambda pdf, field: Enumerable([
  # lambda: pdf[~(pdf.year_added == pdf.release_year)].sample(5),
  # lambda: pdf.isna().mean().sort_values(ascending=False),
  # lambda: df[['director', 'title']],
  # lambda: pdf[pdf.name.str.contains('Salad', flags = re.I)].name,
  # lambda: pdf.groupby('food_cat').carbs_marco_ratio.count(),
  # lambda: pdf.sample(5),
  # lambda: pdf.sort_values('calories')
]))(df, 'country')

# u.foreach(lambda f: print(f()),ps)

# df.to_csv(config['file_locations']['data'])

# Apply the default theme
sns.set_theme()

# aplot = sns.boxplot(x='food_cat', y='carbs_marco_ratio', data=df)
# General plot stuff
# aplot.set_xticklabels(aplot.get_xticklabels(), rotation=30)
# plt.show()