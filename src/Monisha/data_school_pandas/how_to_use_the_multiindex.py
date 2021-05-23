import pandas as pd

stocks = pd.read_csv('http://bit.ly/smallstocks')

print(stocks)
print(stocks.index)
print(stocks.groupby('Symbol').Close.mean())

#multiindex
ser = stocks.groupby(['Symbol', 'Date']).Close.mean()

print(ser.index)

#unstack()
print(ser.unstack())

#pivot_table()
df = stocks.pivot_table(values='Close', index='Symbol', columns='Date')

#sorting multiindex series
print(ser.loc['AAPL'])
print(ser.loc['AAPL', '2016-10-03'])
print(ser.loc[:, '2016-10-03'])

#creating multiindex dataframe
stocks.set_index(['Symbol', 'Date'], inplace=True)
stocks.sort_index(inplace=True)
print(stocks)

#sorting multiindex dataframe
print(stocks.loc['AAPL'])
print(stocks.loc[('AAPL', '2016-10-03'), :])
print(stocks.loc[(['AAPL', 'MSFT']), :])
print(stocks.loc[(slice(None) , '2016-10-03'), :])