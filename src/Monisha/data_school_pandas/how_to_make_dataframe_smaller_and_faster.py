import pandas as pd

drinks = pd.read_csv('http://bit.ly/drinksbycountry')

print(drinks.head())

#info()
print(drinks.info())
print(drinks.info(memory_usage='deep'))

#memory_usage()
print(drinks.memory_usage(deep=True))
print(drinks.memory_usage(deep=True).sum)

#astype('category')
print(drinks.continent.unique())
drinks['continent'] = drinks.continent.astype('category')
print(drinks.dtypes)
print(drinks.memory_usage(deep=True))
drinks['country'] = drinks.country.astype('category')
print(drinks.memory_usage(deep=True))


df = pd.DataFrame({'ID':[100, 101, 102, 103],\
  'quality':['good', 'very good', 'good', 'excellent']})
print(df)
print()
print(df.sort_values('quality'))