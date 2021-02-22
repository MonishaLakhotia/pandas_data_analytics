from glob import glob
import os
import pandas as pd
import pandas_data_analytics.utils as u
import re
import toml
from ast import literal_eval

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))
u.set_full_paths(config, this_dir)

df: pd.DataFrame = pd.read_csv(config['file_locations']['data_csv'])
df.columns = df.columns.str.strip()
# print(df['Academic Period Code'].head(5))
# print(df.dtypes)

# sets display options for the dataframe
pd.set_option('display.max_rows', df.shape[0]+1)
pd.set_option('display.max_columns', 10000)
pd.set_option('display.max_colwidth', 200)

dayPatterns = [
  'M',
  'T',
  'W',
  'R',
  'F'
]

  # genre_df: pd.DataFrame = df[\
  #   ['date_added', 'release_year', 'rating', 'duration', 'year_added']\
  #   ].assign(genre=df["listed_in"]\
  #   .str.split(", ")).explode('genre')

md1 = 'Meet Days 1'
# print(df[[md1]])
df['DayList'] = df[md1]\
  .str.strip()\
  .str.replace('('+'|'.join(dayPatterns)+')', r'\1, ', regex=True, flags=re.I)\
  .str.replace('(.*), $', r'\1', regex=True)\
  .str.split(', ')

# df.DayList = df.DayList.fillna([])
# df.loc[df['DayList'].isna(),['DayList']] = df.loc[df['DayList'].isna(),'DayList'].apply(lambda x: [])

# df.dropna(inplace=True,axis=1)
# df.convert_dtypes()
# print(df.dtypes)
print(df['DayList'])
df.explode('DayList')


# df.to_excel(config['file_locations']['cleaned_data'], index=False, sheet_name='Export Worksheet')
# df.to_csv(config['file_locations']['cleaned_data_csv'], index=False)
