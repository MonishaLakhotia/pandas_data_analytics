import pandas as pd
import numpy as np

#pd.DataFrame with dictionary
df = pd.DataFrame({'id': (100, 101, 102),\
   'color': ['red', 'blue', 'red']},\
      columns=['id', 'color'], index=['a', 'b', 'c'])

print(df)

#pd.DataFrame with list of lists
print(pd.DataFrame([[100, 'red'], [101, 'blue'],\
   [102, 'red']], columns=['id', 'color'], index=['a', 'b', 'c']))

#numpy array
arr = np.random.rand(4,2)
print(pd.DataFrame(arr, columns=[1, 2]))

#larger dataframe
df_large = pd.DataFrame({'student': np.arange(100, 110, 1), 
'test': np.random.randint(60, 101, 10)})

print(df_large)

#creating series and attaching to dataframe
s = pd.Series(['round', 'square'], index=['c','b'], name='shape')
print(s)

df = pd.concat([df, s], axis=1)

#fillna() practice
df.fillna('not specified', inplace=True)
print(df)