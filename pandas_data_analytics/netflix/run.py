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
# amazing!!! converts datatypes as best it can
# string nan values become <NA>, still a rep for nan
df = df.convert_dtypes()
df.rating = df.rating.astype('category')
pd.set_option('display.max_rows', df.shape[0]+1)
pd.set_option('display.max_columns', df.shape[1]+1)

def drop_filler(g):
  if(Enumerable(['tv shows', 'movies']).any(lambda e: g.lower() == e)):
    return g
  return re.sub('Movies|TV|Shows|Series|Features', '', g)

# creates bins for the durations, does not include season info
# only assigns indices where duration was minute based
df['duration_bin'] = pd.cut(df[~df.duration.str.contains('season', flags=re.I)]\
  .duration.str.split(' ', expand=True)[0].str.strip().astype('int')\
    .sort_values(), bins=np.linspace(0, 350, 8))

def genre_df_sup():
  genre_df: pd.DataFrame = df[\
    ['date_added', 'release_year', 'rating', 'duration', 'year_added']\
    ].assign(genre=df["listed_in"]\
    .str.split(", ")).explode('genre')
  genre_df.genre = genre_df.genre.apply(drop_filler).str.strip()
  genre_df.genre = genre_df.genre.astype('category')
  return genre_df

def director_df_sup():
  director_df: pd.DataFrame = df[\
    ['director', 'date_added', 'release_year', 'rating', 'duration', 'year_added']\
    ].assign(director=df['director']\
      .str.split(', ')).explode('director')
  director_df.director = director_df.director.astype('category')
  return director_df

ps = (lambda pdf, field: Enumerable([
  # lambda: df.sample(5),
  # lambda: df.dtypes,
  # lambda: df.nunique(),
  # lambda: df.head(),
  # lambda: genre_df.genre.value_counts(normalize=True),
  # lambda: genre_df.groupby('year_added').genre.value_counts(normalize=True),
  lambda: pdf[field].value_counts(dropna=False),
  lambda: len(pdf[field].unique()),
  # lambda: df[['director', 'title']],
  lambda: pdf.columns
]))(genre_df_sup(), 'genre')
u.foreach(lambda f: print(f()),ps)

# Apply the default theme
sns.set_theme()
# sns.countplot(x='year_added', data=df, hue='type')
# aplot = sns.countplot(x='duration_bin', data=df, hue='rating')
# aplot.set_xticklabels(aplot.get_xticklabels(), rotation=30)
# plt.show()
