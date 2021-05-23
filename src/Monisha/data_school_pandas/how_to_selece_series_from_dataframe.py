import pandas as pd

#ufo = pd.read_table('http://bit.ly/uforeports', sep=',')

#use read_csv for csv
ufo = pd.read_csv('http://bit.ly/uforeports')

#type to see data type 
type(ufo)

#seeing top five to see columns
ufo.head()

"""
#to select out a series (specific column)
#bracket notation
print(ufo['City'])
#dot notation
print(ufo.City)


#concatination of series
print(ufo.City + ', ' + ufo.State)
"""

#assign concatination to a new series in dataframe
ufo['Location'] = ufo.City + ', ' + ufo.State

print(ufo)