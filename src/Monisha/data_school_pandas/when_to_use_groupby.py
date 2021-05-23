import pandas as pd

drinks = pd.read_csv('http://bit.ly/drinksbycountry')
print(drinks.head())

#asking question what is the average beer servings across all countries
print(drinks.beer_servings.mean())

#let's say you want to look at it by continent
print(drinks.groupby('continent').beer_servings.mean())

#example with filtering
print(drinks[drinks.continent == 'Africa'].beer_servings.mean())

#max() min()
print(drinks.groupby('continent').beer_servings.max())
print(drinks.groupby('continent').beer_servings.min())

#agg
print(drinks.groupby('continent').beer_servings.agg(['count', 'min', 'max', 'mean']))

#not specified column when using groupby
print(drinks.groupby('continent').mean())

