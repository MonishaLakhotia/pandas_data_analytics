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

df = df.drop(\
  ['web-scraper-order',
  'web-scraper-start-url',
  'name_link-href',
  'generation-href'
  ], axis=1)

pd.set_option('display.max_rows', df.shape[0]+1)
pd.set_option('display.max_columns', 175)

# name field is unique per pokemon

# movesdf: pd.DataFrame = df[['name', 'moves_learnt_by_level_up', 'generation']].dropna()
movesdf: pd.DataFrame = df.drop(['name_link'], axis=1)

types = ['ground', 'electric', 'bug', 'ghost', 'normal', 'psychic', 'fire', 'fairy', 'dark', 'grass', 'fighting', 'water', 'ice', 'dragon', 'poison', 'rock', 'flying', 'steel']

# def get_thing(phrase, s):
#   m = re.search(phrase,s)
#   return m.group(1) if m is not None\
#     else np.nan
# def parse_moves_lvl_up(s):
#   lvl = get_thing('^(\d+)', s)
#   return lvl
# movesdf['moves_learnt_by_level_up_lvl'] = movesdf.moves_learnt_by_level_up.apply(parse_moves_lvl_up)

def parse_moves(df, field):
  df[f'{field}_lvl'] = df\
    [field]\
    .str.replace(r'(^\d+)(.*)', r'\1', regex=True)
  df[f'{field}_move'] = df\
    [field]\
    .str.replace('(^\\d+)(\\D+(?:'+'|'.join(types)+'))(.*)', r'\2', regex=True, flags=re.I)\
    .str.replace('(.*?)('+'|'.join(types)+')'+'$', r'\1', regex=True, flags=re.I)
  df[f'{field}_type'] = df\
    [field]\
    .str.replace('(^\\d+)(\\D+(?:'+'|'.join(types)+'))(.*)', r'\2', regex=True, flags=re.I)\
    .str.replace('(.*?)('+'|'.join(types)+')'+'$', r'\2', regex=True, flags=re.I)
  df[f'{field}_power'] = df\
    [field]\
    .str.strip()\
    .str.replace('(^\\d+)(\\D+(?:'+'|'.join(types)+'))(.*)', r'\3', regex=True, flags=re.I)\
    .str.replace(r'(.*?)(\d{,4}|—|∞)\s{,4}(\d{,4}|—|∞)$', r'\2', regex=True, flags=re.I)\
    .str.replace(r'∞', 'inf', regex=True)\
    .str.replace(r'—', '', regex=True)
  df[f'{field}_acc'] = df\
    [field]\
    .str.strip()\
    .str.replace('(^\\d+)(\\D+(?:'+'|'.join(types)+'))(.*)', r'\3', regex=True, flags=re.I)\
    .str.replace(r'(.*?)(\d{,4}|—|∞)\s{,4}(\d{,4}|—|∞)$', r'\3', regex=True, flags=re.I)\
    .str.replace(r'∞', 'inf', regex=True)\
    .str.replace(r'—', '', regex=True)
  # df['json'] = df.to_json(orient='records', lines=True).splitlines()
  return df


print(df.columns)

l = [
  'moves_learnt_by_level_up',
  'moves_learnt_by_tm',
  'moves_learnt_by_tr',
  'moves_learnt_by_move_tutor',
  'moves_learnt_by_egg',
  'moves_learnt_by_hm',
  'moves_learnt_by_transfer',
  'moves_learnt_by_evolution'
  ]
for f in l:
  movesdf = parse_moves(movesdf, f)

pdf = movesdf
field = 'moves_learnt_by_level_up'
pdf = pdf.filter(regex=f'{field}|name', axis=1)
# pdf.columns[pdf.columns.str.contains(f'({field}.*|name|generation)', flags=re.I,regex=True)]
total_rows = len(pdf.index.value_counts())
unique_rows = len(pdf.drop_duplicates().index.value_counts())
dup_rows = len(pdf[movesdf.duplicated()].index.value_counts())
percent_duped = (dup_rows / total_rows) * 100
# dups are due to alonan forms/ alter form tabs for move sets
# try to filter then out based on if the number in the move set entry restarts
# FOR EACH GENERATION
# if 1..23..88 then 2..22..88
  # then drop the entries from 2 onward since these are alonan form move sets

ps = Enumerable([
  # lambda: pdf[~(pdf.year_added == pdf.release_year)].sample(5),
  # lambda: pdf.isna().mean().sort_values(ascending=False),
  # lambda: pdf[pdf.name.str.contains('Salad', flags = re.I)].name,
  # lambda: pdf.groupby('food_cat').carbs_marco_ratio.count(),
  lambda: pdf.columns,
  lambda: total_rows,
  lambda: unique_rows,
  lambda: dup_rows,
  lambda: percent_duped,
  lambda: pdf.sample(5),
  # lambda: pdf.sort_values(['name', 'generation', 'moves_learnt_by_level_up_lvl']).drop([], axis=1).sample(5),
  # lambda: pdf.sort_values(['name', 'generation', 'moves_learnt_by_level_up_lvl']).sample(5),
  # lambda: pdf[movesdf.duplicated()].sort_values(['name', 'generation'])
  # lambda: pdf.sort_values('calories')
])
u.foreach(lambda f: print(f()),ps)

# df.to_csv(config['file_locations']['data'])

# Apply the default theme
sns.set_theme()

# aplot = sns.boxplot(x='food_cat', y='carbs_marco_ratio', data=df)
# General plot stuff
# aplot.set_xticklabels(aplot.get_xticklabels(), rotation=30)
# plt.show()