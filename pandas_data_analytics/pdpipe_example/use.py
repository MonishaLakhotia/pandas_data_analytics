import joblib
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

cdf = pipeline(user_query)
cdf = cdf.rename(columns={element: re.sub(r'^Avg. Area ', r'', element,
                                          flags=re.I) for element in user_query.columns.tolist()})
cdf = cdf.rename(columns={element: re.sub(r'\s+', r'_', element,
                                          flags=re.I) for element in cdf.columns.tolist()})


X = cdf.drop('Price', inplace=False, axis=1)

print(X.head())

ys = model.predict(X)

print(ys)
