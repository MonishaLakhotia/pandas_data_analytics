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
import joblib
import pandas_data_analytics.pdpipe_example.pipe_utils as pu
import pandas_data_analytics.pdpipe_example.clean as c
import functools as ft


this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))

pu.set_full_paths(config, this_dir)
csv_loc = config['file_locations']['training_data']

df = pd.read_csv(csv_loc)

# df['Year'] = df['Year'].apply(int)

# Apply the default theme
sns.set_theme()

# print(df.head())
u.general_df_stats(df)
# print(dots['align'].unique())
# sns.relplot(
#     data=dots, kind="line",
#     x="time", y="firing_rate", col="align",
#     hue="choice", size="coherence", style="choice",
#     facet_kws={'sharex': False},
# )
# print(df['Platform'].unique())

bins = np.linspace(df['Global_Sales'].min(), df['Global_Sales'].max(),  5)
df['Global_Sales_Bin'] = pd.cut(df['Global_Sales'], bins=bins)  # .astype(str)

company_to_console = {
    'nintendo': ['Wii', 'NES', 'GB', 'DS', 'SNES',
                 'GBA', '3DS', 'N64', 'WiiU', 'GC'],
    'microsoft': ['X360', 'XOne', 'XB'],
    'sony': ['PS3', 'PS2', 'PS4', 'PSP', 'PS'],
    'pc': ['PC'],
    'other': ['2600', 'GEN', 'DC', 'PSV', 'SAT',
              'SCD', 'WS', 'NG', 'TG16', '3DO', 'GG', 'PCFX']
}

console_to_company = u.create_cat_bins(company_to_console)


# pdf = df[df['Genre'] == 'Puzzle']
# print(df.describe(include='all'))

# scatter_plot = sns.relplot(x="Genre", y="Global_Sales", data=df, hue='Genre')
# scatter_plot = sns.relplot(x="Year", y="Global_Sales", data=df, hue='Genre')

bins = np.linspace(1980, 2020, 5)
df['Year_Bin'] = pd.cut(df['Year'], bins=bins)  # .astype(str)

df['Platform_Bin'] = df['Platform'].apply(lambda p: console_to_company[p])


# df['Year_Bin'] = df['Year_Bin'].apply(str)

dfgr = df.groupby(['Year_Bin', 'Platform_Bin'])
print(dfgr)

grdf = dfgr.apply(lambda x: x.sort_values(
    by=['Global_Sales'], ascending=False)['Global_Sales'].sum())

print(grdf)

sumdf = dfgr.agg(np.sum)


print(sumdf)

df['Year_Bin_Str'] = pd.cut(df['Year'], bins=bins).astype(str)

cats = [str(c)
        for c in list(df['Year_Bin'].unique().sort_values(ascending=True))[0:-1]]

print(cats)


# count distribution
# aplot = sns.countplot(x="Platform_Bin", data=df, hue='Genre')

# data distribution over time
# aplot = sns.kdeplot(x="Year", data=df)

# aplot = sns.histplot(x="Platform_Bin", data=df, hue='Genre')
aplot = sns.boxplot(
    x="Global_Sales", data=df)
# aplot.set_xticklabels(aplot.get_xticklabels(), rotation=30)

# sns.relplot(
#     data=df,
#     x="Year", y="Global_Sales"
# )

# displot = sns.displot(data=df, x='Year', hue='Year_Bin')

# print(df.head())

# scatter plot
# sns.relplot(
#     data=df,
#     x="Year", y="Global_Sales", hue='Platform_Bin',
#     size='Rank'
# )


def countplot(x, hue, **kwargs):
    sns.countplot(x=x, hue=hue, **kwargs)


# g = sns.FacetGrid(df, col="Platform_Bin", hue='Genre')
# g.map(sns.countplot, 'Year_Bin')
# g.add_legend()
# for ax in g.axes.flat:
#     for label in ax.get_xticklabels():
#         label.set_rotation(30)

# aplot = sns.histplot(data=df, x='Year_Bin')

# sns.countplot(
#     data=df,
#     x="Year_Bin", hue='Genre',
#     palette=sns.color_palette('hls', 8)
# )

sns.countplot(
    data=df,
    x="Global_Sales_Bin"
)

# sns.barplot(
#     data=sumdf,
#     x='Year_Bin',
#     y='Global_Sales',
#     hue='Platform_Bin'
# )

# continuous distribution of density of years
# sns.kdeplot(x='Year', data=df)

plt.show()
