from sklearn import preprocessing

# https://www.kaggle.com/herozerp/viz-rule-mining-for-groceries-dataset

# shows number of null values per column
# df.isnull().sum()

# shows number of nan values per column
# df.isna().sum()

# number of unique entries for the itemDescription column
# len(df["itemDescription"].unique())


def l(df): return [df.head(), df.dtypes, df.shape, df.columns, df.index]


def p(df):
    foreach(print, l(df))


def foreach(action, iterable):
    for element in iterable:
        action(element)
