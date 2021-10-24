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
csv_loc = config['file_locations']['data']

df: pd.DataFrame = pd.read_csv(csv_loc)
df.columns = df.columns.str.lower()
nums = ['protein', 'carbs', 'fat', 'sat.fat', 'grams', 'calories', 'fiber']
for c in nums:
  df[c] = df[c]\
    .str.replace('[a-zA-Z,\']', '', regex=True)
df = df.replace(r'^\s*$', np.nan, regex=True)
# df = df.convert_dtypes()

for c in nums:
  df[c] = df[c].astype('float')

df['cal_per_gram'] = df.calories / df.grams

pd.set_option('display.max_rows', df.shape[0] + 1)
pd.set_option('display.max_columns', df.shape[1] + 1)


ps = (lambda pdf: Enumerable([
  lambda: pdf.sample(5),
  lambda: pdf.columns,
  lambda: pdf[['food', 'cal_per_gram', 'category']].groupby('category').food.agg(list),
]))(df)

u.foreach(lambda f: print(f()), ps)

# df.to_csv(config['file_locations']['clean_data'])

# Apply the default theme
sns.set_theme()

# aplot = sns.boxplot(x='category', y='cal_per_gram', data=df)
# General plot stuff
# aplot.set_xticklabels(aplot.get_xticklabels(), rotation=30)
# plt.show()
