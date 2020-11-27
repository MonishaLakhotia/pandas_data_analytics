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

u.general_df_stats(df)

# have to migrate on columns matching *_exp to skill and skill_exp columns
# 1 row becomes many rows
sdf = df.stack().to_frame().T
print(sdf)
# u.general_df_stats(sdf)
exps = df.filter(regex=(".*_exp"))
print(exps)
mdf = pd.melt(df.head(5), id_vars=['char_link'], value_vars=exps)


def r(s):
    return re.sub('\D+', '', flags=re.I, string=s)


def remove_exp(s):
    return re.sub('(.*)_exp$', '\\1', flags=re.I, string=s)


mdf.rename(columns={'value': 'exp', 'variable': 'skill'}, inplace=True)
print(mdf.head())
mdf['exp'] = mdf['exp'].apply(r)
mdf['skill'] = mdf['skill'].apply(remove_exp)
mdf['exp'] = mdf['exp'].astype('int64')
print(mdf)

bplot = sns.barplot(x='char_link', y='exp', hue='skill',
                    data=mdf, palette=sns.color_palette('hls', 30))
bplot.set_xticklabels(bplot.get_xticklabels(), rotation=10)
plt.show()
