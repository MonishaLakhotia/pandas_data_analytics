import re
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
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
import pandas_data_analytics.pdpipe_example.pipe_utils as pu


this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))

pu.set_full_paths(config, this_dir)


csv_loc = config['file_locations']['training_data']

df = pd.read_csv(csv_loc)
p(df)

colsToInt = ['Price', 'Avg. Area Income', 'Avg. Area House Age',
             'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Area Population']
pipeline = pdp.ColDrop(['Address'])
pipeline += pdp.ApplyByCols(colsToInt, pu.toInt, colsToInt, drop=True)
pipeline += pdp.ApplyByCols('Avg. Area Number of Rooms',
                            pu.size, 'House_Size', drop=False)
pipeline += pdp.OneHotEncode('House_Size', drop=True)


cdf = pipeline(df)

cdf = cdf.rename(columns={element: re.sub(r'^Avg. Area ', r'', element,
                                          flags=re.I) for element in df.columns.tolist()})
cdf = cdf.rename(columns={element: re.sub(r'\s+', r'_', element,
                                          flags=re.I) for element in cdf.columns.tolist()})
p(cdf)


Q1 = cdf.quantile(0.25)
Q3 = cdf.quantile(0.75)
IQR = Q3-Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

cdf = cdf[~((cdf < lower_bound) | (
    cdf > upper_bound)).any(axis=1)]

sns.boxplot(x=cdf['Price'])
# plt.show()

r = cdf

X = r.drop('Price', axis=1)
y = r['Price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, shuffle=True)

# Create model with config
model = ensemble.GradientBoostingRegressor(
    n_estimators=250,
    learning_rate=0.1,
    max_depth=5,
    min_samples_split=4,
    min_samples_leaf=6,
    max_features=0.6,
    loss='huber'
)

# Train the model
model.fit(X_train, y_train)

mae_train = mean_absolute_error(y_train, model.predict(X_train))
print("Training Set Mean Absolute Error: %.2f" % mae_train)

mae_test = mean_absolute_error(y_test, model.predict(X_test))
print("Test Set Mean Absolute Error: %.2f" % mae_test)

joblib.dump(model, config['file_locations']['model'])
joblib.dump(pipeline, config['file_locations']['pipeline'])
