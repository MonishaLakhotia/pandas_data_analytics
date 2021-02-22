from glob import glob
import os
import pandas as pd
import pandas_data_analytics.utils as u
import re
import toml

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))
u.set_full_paths(config, this_dir)

df: pd.DataFrame = pd.read_csv(config['file_locations']['data'])

# sets display options for the dataframe
pd.set_option('display.max_rows', df.shape[0]+1)
pd.set_option('display.max_columns', 10000)
pd.set_option('display.max_colwidth', 200)

dayPatterns = [
  'M',
  'T(?!r)',
  'W',
  'Tr',
  'F'
]

  # genre_df: pd.DataFrame = df[\
  #   ['date_added', 'release_year', 'rating', 'duration', 'year_added']\
  #   ].assign(genre=df["listed_in"]\
  #   .str.split(", ")).explode('genre')

df.DayList = df\
  .Days\
  .str.strip()
  .str.replace('('+'|'.join(dayPatterns)+')', r'\1,', regex=True, flags=re.I)\
  .str.replace('(.*),$', r'\1', regex=True)\
  .str.split(',')

# df.Day = df.explode('DayList')

pdf: pd.DataFrame = df
ps = [
  # lambda: pdf.columns,
  # lambda: pdf['Products'],
  lambda: pdf.sample(5)
  # lambda: pdf.Products.sort_values()
  # lambda: pdf.dtypes,
]
u.foreach(lambda f: print(f()),ps)

df.to_csv(config['file_locations']['cleaned_data'], index=False)
