import pandas_data_analytics.utils as u
import toml
import os
import pandas as pd
import pandas_data_analytics.pdpipe_example.pipe_utils as pu
import pandas_data_analytics.pdpipe_example.clean as c
import functools as ft
from py_linq import Enumerable


this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))

pu.set_full_paths(config, this_dir)
csv_loc = config['file_locations']['raw']

df = pd.read_csv(csv_loc)

print(df.isnull().sum())

print(df['country'].unique())

print(df.duplicated().sum())
