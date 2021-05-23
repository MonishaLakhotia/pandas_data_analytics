import pandas as pd


drinks = pd.read_csv('http://bit.ly/drinksbycountry')
print(drinks.head())
print(drinks.dtypes)

#int to float
drinks.beer_servings = drinks.beer_servings.astype(float)
print(drinks.head())
print(drinks.dtypes)

#to chage dtype before reading file
drinks = pd.read_csv('http://bit.ly/drinksbycountry', dtype={'beer_servings':float})
print(drinks.dtypes)

#new dataset
orders = pd.read_table('http://bit.ly/chiporders')

print(orders.head())
print(orders.dtypes)
#item price stored as string

#remove the dollar sign
print(orders.item_price.str.replace('$', '').astype(float).mean())

print(orders.item_name.str.contains('Chicken').astype(int))