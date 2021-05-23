import pandas as pd

columns = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=columns, index_col='user_id')


print(users.head())
print(users.shape)

#duplicated() + drop_duplicates()
print(users.zip_code.duplicated())
print(users.zip_code.duplicated().sum())
print(users.duplicated())

print(users.loc[users.duplicated(), :])
print(users.loc[users.duplicated(keep=False), :])
print(users.shape)
print(users.drop_duplicates(keep='first').shape)

print(users.duplicated(subset=['age', 'zip_code']))