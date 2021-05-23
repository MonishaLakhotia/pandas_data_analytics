import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')

print(movies.head())
print(movies.dtypes)

print(movies.genre.describe())

#value counts, more detail
print(movies.genre.value_counts())
print(movies.genre.value_counts(normalize=True))

#unique() and nunique()
print(movies.genre.unique())
print(movies.genre.nunique())

#pd.crosstab()
print(pd.crosstab(movies.genre, movies.content_rating))
print(movies.duration.describe())
print(movies.duration.mean())
print(movies.duration.std())
print(movies.duration.value_counts())