import pandas_data_analytics.utils as u
import toml
from pandas_data_analytics import *
import os
import pdpipe as pdp
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import numpy as np
import pandas_data_analytics.pdpipe_example.pipe_utils as pu
import pandas_data_analytics.pdpipe_example.clean as c
import functools as ft
from py_linq import Enumerable


this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))

pu.set_full_paths(config, this_dir)
csv_loc = config['file_locations']['clean']

df = pd.read_csv(csv_loc)

# Apply the default theme
sns.set_theme()

# u.general_df_stats(df)

# print(df.groupby('brand').agg(['count', 'mean']))


# plt.show()
