import pandas as pd
import numpy as np

"""
#toread certain columns
ufo = pd.read_csv('http://bit.ly/uforeports', usecols=['City', 'State'])

print(ufo.columns)

#iterating through entries in Series
for c in ufo.City:
  print(c)

#iterating through dataframe
for index, row in ufo.iterrows():
  print(index, row.City, row.State)
"""

#to delete every nonnumeric column
drinks = pd.read_csv('http://bit.ly/drinksbycountry')

print(drinks.dtypes)

print(drinks.select_dtypes(include=[np.number]).dtypes)
#dtypes added to included data types, not edited in place
drinks.describe()
