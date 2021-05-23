import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')
print(ufo.shape)
print(ufo.head())

ufo.drop('City', axis=1, inplace=True)
print(ufo.head())

print(ufo.dropna(how='any').shape)