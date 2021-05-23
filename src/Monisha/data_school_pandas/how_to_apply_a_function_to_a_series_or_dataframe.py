import pandas as pd

train = pd.read_csv('http://bit.ly/kaggletrain')

print(train.head())

#.map()
train['Sex_male'] = train.Sex.map({'female': 0, 'male': 1})

print(train.loc[0:4, ['Sex', 'Sex_male']])

#.apply()
train['name_length'] = train.Name.apply(len)
print(train.loc[0:4, ['Name', 'name_length']])

#.apply() w/ function
def get_element(my_list, position):
  return my_list[position]

print(train.Name.str.split(',').apply(get_element, position=0).head())

#same as above but with lambda function
print(train.Name.str.split(',').apply(lambda x: x[0]).head())

drinks = pd.read_csv('http://bit.ly/drinksbycountry')

print(drinks.loc[:, 'beer_servings':'wine_servings'].apply(max, axis=1))

#.applymap()
print(drinks.loc[:, 'beer_servings':'wine_servings'].applymap(float))