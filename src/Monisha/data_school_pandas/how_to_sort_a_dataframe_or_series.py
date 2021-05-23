import pandas as pd

movies = pd.read_csv('https://bit.ly/imdbratings')

#print(movies)

#for series - dot or bracket notation and sort_values()
movies.title.sort_values()
movies[title].sort_values()

#descending order
movies.title.sort_values(ascending=False)

#sort dataframe by series
movies.sort_values('title')

#sort by multiple columns
movies.sort_values('content_rating', 'genre')