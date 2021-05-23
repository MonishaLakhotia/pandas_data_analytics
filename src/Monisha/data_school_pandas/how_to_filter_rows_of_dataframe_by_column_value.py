import pandas as pd

movies = pd.read_csv('https://bit.ly/imdbratings')

print(movies.head())
print(movies.shape)

"""
#LONG WAY
#first create for loop for list of booleans

booleans = []
for length in movies.duration:
  if length >= 200:
    booleans.append(True)
  else:
    booleans.append(False)
  
print(booleans[:5])
print(len(booleans))

#next convert booleans to a pandas series
#use pd.Series()
is_long = pd.Series(booleans)
print(is_long.head())

#final step: pass is_long to movies dataframe 
#use bracket notation
print(movies[is_long])
"""

"""
#short way
#in place of for loop
in_place = movies.duration >= 200
print(movies[in_place])
"""

#even shorter
#and more conventional way
print(movies[movies.duration >= 200])
print(movies[movies.duration >= 200].shape)

#filtered to 200 min and just showing genre
print(movies[movies.duration >= 200].genre)
print(movies[movies.duration >= 200]['genre'])

#using .loc
print(movies.loc[movies.duration >= 200, 'genre'])