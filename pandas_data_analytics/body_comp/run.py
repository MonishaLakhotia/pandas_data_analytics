from pandas_data_analytics import *
from py_linq import Enumerable
import datetime
import functools as ft
import json
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pandas_data_analytics.utils as u
import re
import seaborn as sns
import toml

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

date_bins = pd.interval_range\
  (start=pd.Timestamp('2020-07-01'),\
  periods=7, freq='MS')
df['date_range'] = pd.cut(df.date, date_bins)
recentdf = df#[(df['date']>pd.Timestamp(2020,11,24)) & (df['date']<pd.Timestamp(2021,1,23))]

# diffdf = recentdf.iloc[-1] - recentdf.iloc[0]
pdf: pd.DataFrame = recentdf
ps = Enumerable([
  lambda: pdf.columns,
  # lambda: date_bins,
  # lambda: pdf.dtypes,
  # lambda: pdf.describe(include='all', datetime_is_numeric=True),
  # lambda: pdf.sample(5),
  # lambda: monthly_summaries_df,
  # lambda: pdf.sort_values(['name', 'generation', 'moves_learnt_by_level_up_lvl']).drop([], axis=1).sample(5),
  # lambda: pdf.sort_values(['name', 'generation', 'moves_learnt_by_level_up_lvl']).sample(5),
  # lambda: pdf[movesdf.duplicated()].sort_values(['name', 'generation'])
  # lambda: pdf.sort_values('calories')
])
u.foreach(lambda f: print(f()),ps)

# write out monthly summaries of stats
monthly_summaries_df: pd.DataFrame = pdf.groupby(by='date_range').agg(['mean', 'std', 'min', 'max']).unstack().reset_index()
monthly_summaries_df.columns = monthly_summaries_df.columns.astype(str)
monthly_summaries_df.rename(columns={'level_0':'metric', 'level_1':'stat', '0': 'num'}, inplace=True)
monthly_summaries_df.to_csv(config['file_locations']['monthly_summaries'], index=False)

# Apply the default theme
sns.set_theme()

# aplot = sns.lineplot(x='date', y='morning_weight', data=df)
# General plot stuff
# aplot.set_xticklabels(aplot.get_xticklabels(), rotation=30)
# plt.show()