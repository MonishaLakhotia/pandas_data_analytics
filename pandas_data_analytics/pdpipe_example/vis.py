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
import plotly.express as px
import plotly.offline as py
from plotly.offline import plot
import plotly.graph_objects as go
import plotly.graph_objs as go

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))

pu.set_full_paths(config, this_dir)
csv_loc = config['file_locations']['training_data']

df = pd.read_csv(csv_loc)

# print(df.isnull().sum())
# print(df.isna().sum())
# print(df.mode())
# print(df.mean())
# print(df.median())
# the range
# print(df['Price'].max() - df['Price'].min())
# the domain
# print(df['Price'].max(), df['Price'].min())
# general states
# print(df['Price'].describe())


# qcut for bins with same number of members. or for bins of custom quantile sizes

# Quartile based buckets
df['Price_Quartile'] = pd.qcut(df['Price'], q=4)
# print(df['Price_Quartile'].value_counts())

# 20% buckets with labels
bin_labels_5 = ['Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond']
df['Quantile_Desc_Labels'] = pd.qcut(df['Price'],
                                     q=5,
                                     #   q=[0, .2, .4, .6, .8, 1],
                                     labels=bin_labels_5)
# print(df['Quantile_Desc_Labels'].value_counts())
# print(df.describe(include='category'))
# describes each column with percentile ranges aswell
# print(df.describe(percentiles=[0, 1/3, 2/3, 1]))

df['Quantile_Number_Labels'] = pd.qcut(df['Price'],
                                       q=[0, .2, .4, .6, .8, 1],
                                       labels=False,
                                       precision=0)
# print(df.head())


# cut for bins with same range sizes. or self defined range sizes

# df['Price_Bins'] = pd.cut(df['Price'], bins=5)
# bins of 500k range sizes
bins = np.linspace(0, 2500000, 6)
df['Price_Bins'] = pd.cut(df['Price'], bins=bins)  # .astype(str)

# in place binning
# df['ext price'].value_counts(bins=4, sort=False)


# print(df['Price_Bins'].describe(include='category'))
print(df['Price_Bins'].value_counts())

# sns.boxplot(x=cdf['Price'])
# plt.show()


# def price_bins(p):
#     if(p > 2000000):
#         return '>2000000'
#     if(p > 1500000):
#         return '>1500000'
#     if(p > 1000000):
#         return '>1000000'
#     if(p > 500000):
#         return '>500000'
#     return '>0'


# pipeline = pdp.ApplyByCols('Price', price_bins, 'Price_Bins', drop=False)

# cdf = pipeline(df)
cdf = df

print(cdf['Price_Bins'].unique())

print(cdf.head())
print(cdf["Price_Bins"].value_counts())

# fig = px.bar(cdf["Price_Bins"].value_counts(), orientation="v", color=cdf["Price_Bins"].value_counts(), color_continuous_scale=px.colors.sequential.Plasma,
#              log_x=False, labels={'value': 'Count',
#                                   'index': 'Price',
#                                   'color': 'None'
#                                   })


gdf = cdf.groupby('Price_Bins')
print(gdf.head(10))
barplot = sns.countplot(x="Price_Bins", data=cdf)
barplot.set_xticklabels(barplot.get_xticklabels(), rotation=30)
# [plt.setp(ax.get_xticklabels(), rotation=90) for ax in barplot.axes.flat]
plt.show()

# fig.update_layout(
#     font_color="black",
#     title_font_color="red",
#     legend_title_font_color="green",
#     title_text="Price by count"
# )

# fig.show()
