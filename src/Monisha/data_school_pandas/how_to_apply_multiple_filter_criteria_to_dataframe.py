import pandas as pd

movies = pd.read_csv('https://bit.ly/imdbratings')
#print(movies.head())

#like single fitering
print(movies[(movies.duration >= 200) & (movies.genre == 'Drama')])

#use & for and
#use | for or

#to see multiple values/multiple or conditions
print(movies[movies.genre.isin(['Crime', 'Drama', 'Action'])])