import pandas as pd

drinks = pd.read_csv('http://bit.ly/drinksbycountry')

"""
#pd.get_option(), pd.set_option(), reset_option
print(pd.get_option('display.max_rows'))
pd.set_option('display.max_rows', None)
print(drinks)
print(pd.get_option('display.max_columns'))
pd.set_option('display.max_columns', None)
print(drinks)
pd.reset_option('display.max_columns')
"""

#pd.describe_option()
print(pd.describe_option())