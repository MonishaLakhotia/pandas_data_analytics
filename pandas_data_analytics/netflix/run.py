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
df.type = df.type.astype('category')
df.date_added = pd.to_datetime(df.date_added)
df['year_added'] = df.date_added.dt.year.astype('Int64').astype('category')
df.release_year = df.release_year.astype('category')
df.rating = df.rating.astype('category')
pd.set_option('display.max_rows', df.shape[0]+1)
pd.set_option('display.max_columns', df.shape[0]+1)

# Apply the default theme
def drop_filler(g):
  if(Enumerable(['tv shows', 'movies']).any(lambda e: g.lower() == e)):
    return g
  return re.sub('Movies|TV|Shows|Series|Features', '', g)
sns.set_theme()

def duration_bin(dur):
  if(re.search('season', dur, re.I) is not None):
    return dur
  else:
    return dur + '1'

# creates bins for the durations, does not include season info
# only assigns indices where duration was minute based
df['duration_bin'] = pd.cut(df[~df.duration.str.contains('season', flags=re.I)]\
  .duration.str.split(' ', expand=True)[0].str.strip().astype('int')\
    .sort_values(), bins=np.linspace(0, 350, 8))

genre_df: pd.DataFrame = df[\
  ['date_added', 'release_year', 'rating', 'duration', 'year_added']\
  ].assign(genre=df["listed_in"]\
  .str.split(", ")).explode('genre')
genre_df.genre = genre_df.genre.apply(drop_filler).str.strip()

ps = Enumerable([
  # df.sample(5),
  # df.dtypes,
  # df.nunique(),
  # df.head(),
  # df2.groupby('year_added').genre.value_counts(normalize=True),
  df.duration_bin.value_counts(dropna=False),
  genre_df.columns
])

u.foreach(print,ps)

# sns.countplot(x='year_added', data=df, hue='type')
# plt.show()
