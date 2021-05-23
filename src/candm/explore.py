import pandas_data_analytics.utils as u
import toml
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from py_linq import Enumerable
import re
from glob import glob

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))
u.set_full_paths(config, this_dir)
csv_loc = config['file_locations']['clean']

df = pd.read_csv(csv_loc)
df['price'] = pd.to_numeric(df['price'].apply(lambda p: re.sub('[$,]', '', p)))

def plot():
    bplot = sns.countplot(x='brand', data=df)
    bplot.set_xticklabels(bplot.get_xticklabels(), rotation=10)
    plt.show()

    bplot = sns.barplot(x='brand', y='price', data=df)
    bplot.set_xticklabels(bplot.get_xticklabels(), rotation=10)
    plt.show()

    bplot = sns.boxplot(x='brand', y='price', data=df)
    bplot.set_xticklabels(bplot.get_xticklabels(), rotation=10)
    plt.show()

def main():
    # Apply the default theme
    sns.set_theme()
    # u.general_df_stats(df)
    print(df.dtypes)
    # print(df.groupby('brand').agg(['count', 'mean']))

main()
