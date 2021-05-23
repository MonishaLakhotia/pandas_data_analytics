import pandas as pd

#read_table to read table in pandas
pd.read_table('http://bit.ly/chiporders')

#sep and header keyword arguments to specify different sep and header
pd.read_table('http://bit.ly/movieusers', sep='|', header=None)

#to add names to columns
columns = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
print(pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=columns))

#save as an dataframe object
data = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=columns)

#then can print