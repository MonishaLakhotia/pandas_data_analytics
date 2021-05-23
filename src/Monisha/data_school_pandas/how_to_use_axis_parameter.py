import pandas as pd

drinks = pd.read_csv('http://bit.ly/drinksbycountry')
print(drinks.head())

#removing column
print(drinks.drop('continent', axis=1).head()) #not in place

#removing row
print(drinks.drop(2, axis=0).head()) #not in place

#mean()
#moves downs each column
#default is axis=0
print(drinks.mean())

#to do each row's mean (moving left to right)
print(drinks.mean(axis=1))