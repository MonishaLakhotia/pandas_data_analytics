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
df.columns = df.columns.str.lower()
for c in ['protein', 'carbs', 'fat', 'sat.fat']:
  df[c] = df[c]\
    .str.replace('[a-zA-Z]', '', regex=True)
df[c] = df[c].replace(r'^\s*$', np.nan, regex=True)
df = df.convert_dtypes()

pd.set_option('display.max_rows', df.shape[0]+1)
pd.set_option('display.max_columns', df.shape[1]+1)

ps = (lambda pdf, field: Enumerable([
  lambda: pdf.sample(5),
  lambda: pdf.columns,
  lambda: pdf.dtypes,
]))(df, 'country')

u.foreach(lambda f: print(f()),ps)

# df.to_csv(config['file_locations']['clean_data'])

# Apply the default theme
sns.set_theme()

# aplot = sns.boxplot(x='food_cat', y='carbs_marco_ratio', data=df)
# General plot stuff
# aplot.set_xticklabels(aplot.get_xticklabels(), rotation=30)
# plt.show()