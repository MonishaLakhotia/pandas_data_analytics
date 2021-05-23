import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')

print(ufo.head())
print(ufo.shape)

#use drop() method to remove
ufo.drop('Colors Reported', axis=1, inplace=True)

#axis=1 for columns, axis=0 for rows
#pass the column name you want to delete to method
print(ufo.head())

#multiple
ufo.drop(['City', 'State'], axis=1, inplace=True)
print(ufo.head())

#deleting rows
ufo.drop([0,1], axis=0, inplace=True)