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
import re

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))

pu.set_full_paths(config, this_dir)
csv_loc = config['file_locations']['training_data']

df = pd.read_csv(csv_loc)

# have to migrate on columns matching *_exp to skill and skill_exp columns
# 1 row becomes many rows
# sdf = df.stack().to_frame().T
# print(sdf)

df.rename(columns={'char_link': 'character'}, inplace=True)

u.general_df_stats(df)

# get columns that have exp in the name
exps = df.filter(regex=(".*_exp"))
print(exps)


def r(s):
    return re.sub('\D+', '', flags=re.I, string=s)


def remove_exp(s):
    return re.sub('(.*)_exp$', '\\1', flags=re.I, string=s)


mdf = pd.melt(df, id_vars=['character'], value_vars=exps)
mdf.rename(columns={'value': 'exp', 'variable': 'skill'}, inplace=True)
mdf['skill_bin'] = mdf['skill'].apply(lambda skill:
                                      'combat' if re.search(
                                          '(attack|str|hp|def|rang|mage|pray)', skill)
                                      else 'gathering' if re.search(
                                          '(wc|fish|hunt|mining|farm)', skill)
                                      else 'artisan(production)' if re.search(
                                          '(fm|cook|smith|craft|rc|herb|fletch|con)', skill)
                                      else 'support'
                                      )
mdf['exp'] = mdf['exp'].apply(r)
mdf['skill'] = mdf['skill'].apply(remove_exp)
mdf['exp'] = mdf['exp'].astype('int64')

# bplot = sns.barplot(x='character', y='exp', hue='skill_bin',
#                     data=mdf)  # , palette=sns.color_palette('hls', 30))
# bplot.set_xticklabels(bplot.get_xticklabels(), rotation=10)

# bplot = sns.barplot(x='skill', y='exp',
#                     data=mdf)  # , palette=sns.color_palette('hls', 30))
# bplot.set_xticklabels(bplot.get_xticklabels(), rotation=10)

# NOT WORKING!
# g = sns.FacetGrid(mdf, col="skill_bin")
# g.map(sns.barplot, 'skill', 'exp')
# g.add_legend()
# for ax in g.axes.flat:
#     for label in ax.get_xticklabels():
#         label.set_rotation(30)

plt.show()
