import pandas as pd
import numpy as np

movies = pd.read_csv('http://bit.ly/imdbratings')

print(movies.head())
print(movies.content_rating.isnull().sum())
print(movies[movies.content_rating.isnull()])
print(movies.content_rating.value_counts())

# = np.na
print(movies[movies.content_rating == 'NOT RATED'].content_rating)
movies.loc[movies.content_rating == 'NOT RATED', 'content_rating'] = np.nan
print(movies.content_rating.isnull().sum())

#change individual value
top_movies = movies.loc[movies.star_rating >= 9, :].copy()
print(top_movies.duration.head())
top_movies.loc[0,'duration'] = 150
print(top_movies.duration.head())
print(movies.duration.head())