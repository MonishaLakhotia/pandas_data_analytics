import pandas as pd

drinks = pd.read_csv('http://bit.ly/drinksbycountry')

print(drinks.head())
print(drinks.continent.head())
drinks.set_index('country', inplace=True)
print(drinks.head())
print(drinks.continent.head())

#using series methods on series returning method
print(drinks.continent.value_counts())
print(drinks.continent.value_counts()['Africa'])
print(drinks.continent.value_counts().sort_values())

#sor values
print(drinks.continent.value_counts().sort_index())

#consturcting Series
people = pd.Series([3000000, 85000], index=['Albania', \
  'Andorra'], name='Population')
print(people)

print(drinks.beer_servings * people)

print(pd.concat([drinks, people], axis=1).head())