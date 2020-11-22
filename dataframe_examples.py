import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
import math


def toNum(n):
    return 0 if(math.isnan(n)) else n


def fn1(row):
    return toNum(row['Price']) + toNum(row['Propertycount'])


df = pd.read_csv('~/Downloads/Melbourne_housing_FULL.csv')

# the param 'inplace=True' can be used to perform a sideeffect
# on the dataframe rather than return a new dataframe

# removes columns
# r = df.drop('Address', axis=1).drop('Regionname', axis=1)[
#     ['Price', 'Distance', 'Propertycount']]

# map examples.
r['AddedStuff'] = r.apply(fn1, axis=1)
r['Price'] = r.Price.map(lambda x: x + 1)

# # filters rows with nan prices
# r = r[r.apply(lambda row: not math.isnan(row['Price']), axis=1)]


# removes columns and then drops all rows with missing values in for any feature
r = df.drop(['Address', 'Method', 'SellerG', 'Date',
             'Postcode', 'Lattitude', 'Longtitude', 'Regionname', 'Propertycount'], axis=1).dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
# grabs a row
# n = df.iloc[99]
# grabs a range of rows
n = df.loc[0:2]

# grab specific feature value of a row
# dataframe[column name][row index]
# list of column headers
# c = df.columns

# To get the 2nd and the 4th row, and only the User Name, Gender and Age columns,
# we can pass the rows and columns as two lists like the below.
#df[['User Name', 'Age', 'Gender']].loc[[1,3]]


# >>> df.index
# RangeIndex(start=0, stop=4, step=1)
# >>> df.columns
# Index(['User Name', 'Country', 'City', 'Gender', 'Age'], dtype='object')

# grabs the first 5 rows by default
h = r.head()
print(h)

# gets the dimension of the dataframe n rows by m columns (n,m)
print(df.shape)

# get data types of all columns
print(df.dtypes)

print(len(df))
print(len(r))
