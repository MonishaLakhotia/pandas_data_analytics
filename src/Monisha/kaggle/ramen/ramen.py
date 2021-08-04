from numpy.core.numeric import NaN
import pandas as pd
import numpy as np
import re
import os
import toml
import src.utils as u

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))
u.set_full_paths(config, this_dir)

ramen_df = pd.read_csv(config['file_locations']['ramen'])
#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#changing Stars to float & unrated to nan
ramen_df.replace('Unrated', np.nan, inplace=True)
ramen_df['Stars'] = ramen_df.Stars.astype(float)

#print(ramen_df.describe(include=['object']))
print(ramen_df.describe())
print(ramen_df.info())
print(ramen_df)
