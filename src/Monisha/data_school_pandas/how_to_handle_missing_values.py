import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')

#print(ufo.tail())
\
#isnull() notnull()
print(ufo.isnull().tail())
print(ufo.notnull().tail())
print(ufo.isnull().sum())
print(ufo.isnull().astype(int).sum())
print(ufo[ufo.City.isnull()])

#dropna()
print(ufo.shape)
print(ufo.dropna(how='any').shape)
print(ufo.dropna(how='all').shape)
print(ufo.dropna(subset=['City', 'Shape Reported'],\
   how='any').shape)

#fillna()
print(ufo['Shape Reported'].value_counts(dropna=False))
print(ufo['Shape Reported'].\
  fillna(value='VARIOUS').value_counts())