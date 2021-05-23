import pandas as pd

drinks = pd.read_csv('http://bit.ly/drinksbycountry')

"""
print(drinks.head())
print(drinks.index)
print(drinks.columns)

print(drinks[drinks.continent == 'South America'])
"""
print(drinks.loc[23, 'beer_servings'])

drinks.set_index('country', inplace=True)
print(drinks.head())
#print(drinks.index)
#print(drinks.columns)
print(drinks.loc['Brazil', 'beer_servings'])

drinks.index.name = None
print(drinks.head())

drinks.index.name = 'country'
drinks.reset_index(inplace=True)
print(drinks.head())

print(drinks.describe().loc['25%','beer_servings'])