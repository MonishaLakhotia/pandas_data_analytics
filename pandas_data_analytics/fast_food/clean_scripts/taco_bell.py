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
csv_loc = config['file_locations']['raw_taco_bell']

df: pd.DataFrame = pd.read_csv(csv_loc)
df.columns = df.columns.str.lower().str.replace('\s+', '', regex=True)
df.drop(['web-scraper-order', 'web-scraper-start-url', 'category-href'], inplace=True, axis=1)

pd.set_option('display.max_rows', df.shape[0]+1)
pd.set_option('display.max_columns', df.shape[1]+1)

pdf = df
ps = Enumerable([
  # lambda: pdf[['name']],
  lambda: pdf.columns,
  lambda: pdf,
  # lambda: pdf[['food', 'cal_per_gram', 'category']].groupby('category').food.agg(list),
  # lambda: pdf.category.value_counts(),
])
u.foreach(lambda f: print(f()),ps)

df.to_csv(config['file_locations']['clean_taco_bell'], index=False)
