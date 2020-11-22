import joblib
import pandas_data_analytics.pdpipe_example.clean as c
import pandas_data_analytics.pdpipe_example.pipe_utils as pu
import os
import pandas as pd
import re
import toml


this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))
pu.set_full_paths(config, this_dir)

model = joblib.load(config['file_locations']['model'])
pipeline = joblib.load(config['file_locations']['pipeline'])

csv_loc = config['file_locations']['user_query']
user_query = pd.read_csv(csv_loc)

cdf = c.clean_dataframe(user_query, pipeline)

X = cdf.drop('Price', inplace=False, axis=1)

print(X.head())

ys = model.predict(X)

print(ys)
