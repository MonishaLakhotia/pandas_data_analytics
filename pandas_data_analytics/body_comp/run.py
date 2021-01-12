import pandas_data_analytics.utils as u
import json
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
import datetime

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))
u.set_full_paths(config, this_dir)
csv_loc = config['file_locations']['data']

df: pd.DataFrame = pd.read_csv(csv_loc)
df.drop('should_delete', axis=1, inplace=True)
df = df.convert_dtypes()
df.date = pd.to_datetime(df.date)

pd.set_option('display.max_rows', df.shape[0]+1)
pd.set_option('display.max_columns', 175)

df = df[(df['date']>pd.Timestamp(2020,11,24)) & (df['date']<pd.Timestamp(2021,1,23))]

diffdf = df.iloc[-1] - df.iloc[0]
pdf = df
ps = Enumerable([
  lambda: pdf.columns,
  lambda: pdf.dtypes,
  lambda: diffdf,
  lambda: pdf.describe(include='all', datetime_is_numeric=True),
  lambda: pdf,
  # lambda: pdf.sort_values(['name', 'generation', 'moves_learnt_by_level_up_lvl']).drop([], axis=1).sample(5),
  # lambda: pdf.sort_values(['name', 'generation', 'moves_learnt_by_level_up_lvl']).sample(5),
  # lambda: pdf[movesdf.duplicated()].sort_values(['name', 'generation'])
  # lambda: pdf.sort_values('calories')
])
u.foreach(lambda f: print(f()),ps)

# df.to_csv(config['file_locations']['clean_data'])


# Apply the default theme
sns.set_theme()

# aplot = sns.boxplot(x='food_cat', y='carbs_marco_ratio', data=df)
# General plot stuff
# aplot.set_xticklabels(aplot.get_xticklabels(), rotation=30)
# plt.show()