import pandas_data_analytics.utils as u
import toml
import re
from pandas_data_analytics import *
import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import numpy as np
import joblib
import functools as ft

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))

u.set_full_paths(config, this_dir)
csv_loc = config['file_locations']['data']

df = pd.read_csv(csv_loc)

def food_binner(s):
    return "pastry" if re.search('donut|eclair|cake', s, re.I) else\
        "drink" if re.search('shake|soda|coke|hot chocolate|cappacino', s, re.I) else\
        "ice_cream" if re.search('cone|icecream|sundae', s, re.I) else\
        "hot_dog" if re.search('dog', s, re.I) else\
            np.nan

# df['food_cat'] = df.name.apply(food_binner)
