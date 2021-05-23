import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')
print(ufo.head(3))

#loc[]
print(ufo.loc[0, :])
print(ufo.loc[[0, 1, 2], :])
print(ufo.loc[0:2, :])
print(ufo.loc[:, 'City'])
print(ufo.loc[:, ['City', 'State']])
print(ufo.loc[:, 'City':'State'])
print(ufo.loc[ufo.City == 'Oakland', :])

#iloc[]
print(ufo.iloc[0:4, 1:3])

#.ix - not working
drinks = pd.read_csv('http://bit.ly/drinksbycountry', \
  index_col='country')
print(drinks.ix['Albania', 0])