import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')

print(ufo.head())
print(ufo.dtypes)

#pd.to_datetime()
ufo['Time'] = pd.to_datetime(ufo.Time)
print(ufo.head())
print(ufo.dtypes)

ts = pd.to_datetime('1/1/1999')
print(ufo.loc[ufo.Time >= ts, :])

print(ufo.Time.dt.year.value_counts().sort_index())