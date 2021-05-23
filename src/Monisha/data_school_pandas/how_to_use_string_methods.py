import pandas as pd

orders = pd.read_table('http://bit.ly/chiporders')


print(orders.head())

#making series upper
print(orders.item_name.str.upper())

#overwriting
orders.item_name = orders.item_name.str.upper()
print(orders.head())

#contains() - checking is a series contains a certain string
print(orders.item_name.str.contains('Chicken'))
#filter
print(orders.loc[orders.item_name.str.contains('Chicken')])

#multiple string methods chained together
print(orders.choice_description.str.replace('[', '').str.replace(']', ''))

#with regex (not working?)
print(orders.choice_description.str.replace('[\[\]]', ''))