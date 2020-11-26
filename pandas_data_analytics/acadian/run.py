import pandas_data_analytics.utils as u
import toml
import re
from pandas_data_analytics import *
import os
import pdpipe as pdp
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import numpy as np
import joblib
import pandas_data_analytics.pdpipe_example.pipe_utils as pu
import pandas_data_analytics.pdpipe_example.clean as c
import functools as ft

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))

pu.set_full_paths(config, this_dir)
csv_loc = config['file_locations']['training_data']

df = pd.read_csv(csv_loc)

def r(s):
  return re.sub('.*?\/(.*?)\/.*?\.\w+$', '\\1', flags=re.I, string=s) 

# def remove_front(s):
#   ee =  re.sub('[[a-z]\.]+?(.*)', '\\1', flags=re.I, string=s) 
#   return ee

df['project'] = df['project_and_file'].apply(r)
df = df[~(df['project'] == 'Search')]
# IQR_price = price_df[~((price_df < lowqe_bound) | (
#     price_df > upper_bound)).any(axis=1)]
print('\n'.join(df['project'].unique()))

# aplot = sns.countplot(
#     data=df,
#     x="project"
# )

u.general_df_stats(df)

gdf = df[['project', 'project_and_file']].groupby('project').agg(['count'])

print(gdf)

# histogram with legend and no x labels
# aplot = sns.histplot(x='project', data=df, hue='project')
# plt.show()

# histogram without legend and has x labels
bplot = sns.countplot(x='project', data=df)
bplot.set_xticklabels(bplot.get_xticklabels(), rotation=10)
plt.show()
