from glob import glob
import os
import pandas as pd
import src.utils as u
import re
import toml
from ast import literal_eval
import datetime
import numpy as np

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))
u.set_full_paths(config, this_dir)

df: pd.DataFrame = pd.read_excel(config['file_locations']['data'], sheet_name='Export Worksheet')
# df: pd.DataFrame = pd.read_csv(config['file_locations']['data_csv'])
df.columns = df.columns.str.strip()
# df.to_csv('data.csv', index=False)
# print(df['Academic Period Code'].head(5))
# print(df.dtypes)

# sets display options for the dataframe
pd.set_option('display.max_rows', df.shape[0] + 1)
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
df['Day'] = df[md1]\
  .str.strip()\
  .str.replace('(' + '|'.join(dayPatterns) + ')', r'\1, ', regex=True, flags=re.I)\
  .str.replace('(.*), $', r'\1', regex=True)\
  .str.split(', ')


def time_binner(r):
  sd = r['start_time']
  ed = r['end_time']
  # x = r['time_span']
  # if np.isnan(ed) or np.isnan(sd):
  h = str(sd.hour)
  m = sd.minute
  em = '0'
  if h == 'nan':
    return r
  if m >= 30:
    em = '30'
  curr_time = datetime.datetime.strptime(h + ":" + em, '%H:%M')
  time_bins = []
  while (curr_time.hour <= ed.hour):
    if (curr_time.hour < ed.hour or curr_time.minute <= ed.minute):
      time_bins.append(str(curr_time.hour).rjust(2, '0') + ':' + str(curr_time.minute).rjust(2, '0'))
    curr_time += datetime.timedelta(minutes=30)
  r['time_bins'] = time_bins
  return r


def to_mil_time(d):
  h = str(d.hour)
  if h == 'nan':
    return np.nan
  return str(d.hour).rjust(2, '0') + ':' + str(d.minute).rjust(2, '0')


df['time_ext_begin'] = df['Begin Time 1'].str.split(' ', expand=True)[1]
df['time_ext_end'] = df['End Time 1'].str.split(' ', expand=True)[1]
df['start_time'] = pd.to_datetime(df['Begin Time 1'], format='%I:%M %p')
df['end_time'] = pd.to_datetime(df['End Time 1'], format='%I:%M %p')
df['time_span'] = df.end_time - df.start_time
df['military_begin_time'] = df['start_time'].apply(to_mil_time)
df['military_end_time'] = df['end_time'].apply(to_mil_time)
df = df.apply(time_binner, axis=1)

# df.Day = df.Day.fillna([])
# df.loc[df['Day'].isna(),['Day']] = df.loc[df['Day'].isna(),'Day'].apply(lambda x: [])

# print(df.military_end_time)
# print(df.time_ext_end)
# df.dropna(inplace=True,axis=1)
# df.convert_dtypes()
# print(df.dtypes)
# print(df)
# print(df['time_bins'])
df = df.explode('time_bins')
df = df.explode('Day')

df['num_day'] = df['Day'].replace({
  'M': '1-Monday',
  'T': '2-Tuesday',
  'W': '3-Wednesday',
  'R': '4-Thursday',
  'F': '5-Friday'
})

# print(df['num_day'])

# df.to_excel(config['file_locations']['cleaned_data'], index=False, sheet_name='Export Worksheet')
# df.to_csv(config['file_locations']['cleaned_data_csv'], index=False)
