import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')

print(movies.head())
print(movies.describe()) #statistical info for numerical columns

print(movies.shape) #tuple w/ num of columsn and rows
print(movies.dtypes) #data types for each column

#example of keyword arugment for pandas method
print(movies.describe(include=['object']))