from sklearn import preprocessing


def l(df): return [df.head(), df.dtypes, df.shape, df.columns, df.index]


def p(df):
    foreach(print, l(df))


def foreach(action, iterable):
    for element in iterable:
        action(element)
