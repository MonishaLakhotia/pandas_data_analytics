# https://www.kaggle.com/herozerp/viz-rule-mining-for-groceries-dataset

# shows number of null values per column
# df.isnull().sum()

# shows number of nan values per column
# df.isna().sum()

# number of unique entries for the itemDescription column
# len(df["itemDescription"].unique())

# get 5 random samples
# df[['event', 'date']].sample(5)

# convert date like field to a date type. 's' is for unix time stamp to date
# pd.to_datetime(df['date_like_field'], unit='s')

# get year of date and count the freq of each year
# x = df['date'].dt.year.value_counts()
# x.sort_index() sorts the x values?

# group by stuff -- NOTE: count is the number of rows per group
# df.groupby('event')['views'].agg['count', 'mean', 'sum'].sort_values('sum')

# a safer eval to parse a string 
# import ast
# type(ast.literal_eval('[1,2,3]')) # outputs: list

# filtering df using a series
# occ_counts = df['occ'].value_counts()
# top_occs = occ_counts[occ_counts >= 5].index
# filtered_df = df[df['occ'].isin(top_occs)]

# reverse order and reset index
# df.loc[::-1].reset_index(drop=True)

# reverse column order
# df.loc[:, ::-1]

# select columns by data type
# df.select_dtype(include='number')
# df.select_dtype(include=['number', 'category'])
# df.select_dtype(exclude=['number', 'category'])

# convert string to numbers with strings that do not look like numbers converted to NAN
# pd.to_numeric(df['col'], errors='coerce')

# memory reduction step
# only read the columns you need from a csv
# cols = ['a', 'b']
# df = pd.read_csv('path/to/csv.csv', usecols=cols)

# memory reduction step
# specify categories up front
# cols = ['a', 'b']
# dtypes = {'a', 'category'}
# df = pd.read_csv('path/to/csv.csv', usecols=cols, dtype=dtypes)

# show memory usage of df
# df.info(memory_usage='deep')

# read from multiple csv's into 1 df (row wise)
# from glob import glob
# files = sorted(glob('data/stocks*.csv'))
# pd.concat((pd.read_csv(file) for file in files), ignore_index=True)

# read from multiple csv's into 1 df (column wise)
# from glob import glob
# files = sorted(glob('data/stocks*.csv'))
# pd.concat((pd.read_csv(file) for file in files), axis='columns')

# read data from clipboard
# df = pd.read_clipboard()

# split a dataframe into 2 random subsets
# df1 = df.sample(frac=0.75, random_state=1234)
# df2 = df.drop(df1.index)
# df1.index.sort_values()
# df2.index.sort_values()

# filter a dataframe by multiple categories
# df[df['genre'].isin(['action', 'scifi'])]
