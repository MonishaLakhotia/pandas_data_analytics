import pandas as pd
import toml
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
import math
import joblib
import pandas_preprocessor as pp
import os


def ldf(df): return [df.head(), df.dtypes, df.shape, df.columns, df.index]


def p(df):
    foreach(print, ldf(df))


this_dir = os.path.dirname(os.path.realpath(__file__))
config_name = "config.toml"

# Loads config
tomlLoc = os.path.join(this_dir, config_name)
config = toml.load(tomlLoc)

# prefix all file locations with this directory
set_full_paths(config, this_dir)

# get training/test data
df = get_dataframe(config['data'])

# clean training/test data for models consumption
r = df.drop(['Address', 'Method', 'SellerG', 'Date',
             'Postcode', 'Lattitude', 'Longtitude', 'Regionname', 'Propertycount'], axis=1)
r.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)
r = clean_dataframe(r, config['dataframe'])

print('Cleaned DF')
p(r)
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

# joblib_file = os.path.join(this_dir, config['model_file_location'])
joblib.dump(model, config['model_file_location'])

# Transform training/test data back to users data structure
inverted_df = invert_cleaning(r, config['dataframe'])
print('Inverted DF')
p(inverted_df)
