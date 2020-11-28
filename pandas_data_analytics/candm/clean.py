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

# u.general_df_stats(df)

# print(df.groupby('brand').agg(['count', 'mean']))

all_brands = df['brand'].unique()
real_brands = Enumerable(list(filter(lambda b: b != 'learn more', all_brands)))


def brand_mapper(row):
    if(row['brand'] == 'learn more'):
        matching_brand = real_brands.first_or_default(
            lambda b: b.lower() in row['listing_link'].lower())
        row['brand'] = matching_brand
    return row


# print(df['brand'].value_counts())

# if brand is learn more, then check the listing_link against the all_brands list and first match, set the real_brand do that match
df = df.apply(brand_mapper, axis=1)

# print(df['brand'].value_counts())

# print(df[df['brand'] == 'learn more'].head(65))

df.to_csv(config['file_locations']['clean'])
