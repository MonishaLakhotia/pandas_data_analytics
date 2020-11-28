from sklearn import preprocessing
import functools as ft

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


def l(df): return [df.head(), df.dtypes, df.shape, df.columns, df.index]


def p(df):
    foreach(print, l(df))


def foreach(action, iterable):
    for element in iterable:
        action(element)


def general_df_stats(df):
    def count_of_unique_members_per_column(df):
        s = ''
        for (columnName, columnData) in df.iteritems():
            s += 'Colunm Name: ' + columnName+'\n'
            s += 'Number of unique members: ' + \
                str((len(columnData.unique()))) + '\n'
        return s

    l = [
        '------------------------------- GENERAL DF STATS BEGIN -------------------------------',
        '=Top 5 entries=',
        df.head(),
        '=Types=',
        df.dtypes,
        '=Shape=',
        df.shape,
        '=Descriptions=',
        df.describe(include='all'),
        '=Null counts=',
        df.isnull().sum(),
        '=Nan counts=',
        df.isna().sum(),
        '=Unique member counts=',
        count_of_unique_members_per_column(df),
        # '=DF info=',
        # df.info(),
        '------------------------------- GENERAL DF STATS END -------------------------------'
    ]

    def p(o):
        print('<<<>>>')
        print(o)
    foreach(p, l)


def create_cat_bins(bin_to_value_dictionary):
    def g(s):
        def f(acc, e):
            acc[e] = s
            return acc
        return f
    value_to_bin_dictionary = {}
    for key, value in bin_to_value_dictionary.items():
        value_to_bin_dictionary = ft.reduce(
            g(key), value, value_to_bin_dictionary)
    return value_to_bin_dictionary


# def top_n_per_group(df_groups):
#     for name, group in grouped:
#         print name
#         print group
