import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import toml
import src.utils as u
import re

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))
u.set_full_paths(config, this_dir)

social_merged = pd.read_csv(config['file_locations']['social_merged'])
google_merged = pd.read_csv(config['file_locations']['google_merged'])
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#merging social data and google data
all_data = pd.concat([social_merged, google_merged])

#misc cleaning - drop duplicates, drop unnamed col, change date cols to date time
all_data.drop_duplicates(subset='Campaign_Name', keep='last', inplace=True)
all_data.drop(columns='Unnamed: 0', inplace=True)

date_cols = [column for column in all_data.columns if re.match('.*Date', column)]
for name in date_cols:
  all_data[name] = pd.to_datetime(all_data[name])