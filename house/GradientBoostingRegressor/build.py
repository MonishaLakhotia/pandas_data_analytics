import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
import math
import joblib
from utils import *


def toNum(n):
    return 0 if(math.isnan(n)) else n


def fn1(row):
    return toNum(row['Price']) + toNum(row['Propertycount'])


df = pd.read_csv('~/Downloads/Melbourne_housing_FULL.csv')

# r = df.drop('Address', axis=1).drop('Regionname', axis=1)[
#     ['Price', 'Distance', 'Propertycount']]
# r['AddedStuff'] = r.apply(fn1, axis=1)
# r['Price'] = r.Price.map(lambda x: x + 1)
# # filters rows with nan prices
# r = r[r.apply(lambda row: not math.isnan(row['Price']), axis=1)]


r = df.drop(['Address', 'Method', 'SellerG', 'Date',
             'Postcode', 'Lattitude', 'Longtitude', 'Regionname', 'Propertycount'], axis=1)
r.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)
s = r.loc[8895]
r.to_csv('b4.csv')
# n = df.iloc[99]
# c = df.columns

r = pd.get_dummies(r, columns=['Suburb', 'CouncilArea', 'Type'])

X = r.drop('Price', axis=1)
y = r['Price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, shuffle=True)

h = r.head()

l = [h, len(df), len(r)]

foreach(print, l)

r.to_csv('out.csv')

model = ensemble.GradientBoostingRegressor(
    n_estimators=250,
    learning_rate=0.1,
    max_depth=5,
    min_samples_split=4,
    min_samples_leaf=6,
    max_features=0.6,
    loss='huber'
)

model.fit(X_train, y_train)

mae_train = mean_absolute_error(y_train, model.predict(X_train))

print("Training Set Mean Absolute Error: %.2f" % mae_train)

mae_test = mean_absolute_error(y_test, model.predict(X_test))
print("Test Set Mean Absolute Error: %.2f" % mae_test)

joblib_file = "house_model.pkl"
joblib.dump(model, joblib_file)
