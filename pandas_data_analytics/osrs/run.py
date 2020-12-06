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
from py_linq import Enumerable

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))

pu.set_full_paths(config, this_dir)
csv_loc = config['file_locations']['training_data']

df = pd.read_csv(csv_loc)

# have to migrate on columns matching *_exp to skill and skill_exp columns
# 1 row becomes many rows
# sdf = df.stack().to_frame().T
# print(sdf)
df.drop(['web-scraper-order', 'web-scraper-start-url', 'char_link-href'], inplace=True, axis=1)
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

# bplot = sns.barplot(x='skill', y='exp',data=mdf)
# bplot.set_xticklabels(bplot.get_xticklabels(), rotation=25)
# plt.show()
# OR
# bplot.set_xticklabels(rotation=25)

# NOT WORKING!
# g = sns.FacetGrid(mdf, col="skill_bin")
# g.map(sns.barplot, 'skill', 'exp')
# g.add_legend()
# for ax in g.axes.flat:
#     for label in ax.get_xticklabels():
#         label.set_rotation(30)

# global settings of sns style
# sns.set_style

# good plotting for distribution of catagories
# sns.catplot(x='skill', y='exp', data=mdf, hue='skill_bin').set_xticklabels(rotation=30)
# sns.violinplot(x='skill', y='exp', data=mdf)
# sns.histplot(x='skill', y='exp', data=mdf)
# sns.boxplot(x='skill', y='exp', data=mdf)
# sns.jointplot is good for numeric x,y scatter plot for checking bin relationships
# plt.show()
exp_df = df.loc[:,df.columns.isin(Enumerable(df.columns).where(lambda c: re.match('.*exp', c)).to_list())]
def keep_digits(e):
    r = re.sub('\D', '', e)
    return r
exp_df = exp_df.applymap(keep_digits).astype(int)
mean_exp = exp_df.mean().astype(int)
# sns.heatmap(exp_df.corr())

# plt.show()

