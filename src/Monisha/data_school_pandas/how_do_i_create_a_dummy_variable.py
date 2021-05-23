import pandas as pd

train = pd.read_csv('http://bit.ly/kaggletrain')
print(train.head())

#.map()
train['Sex_male'] = train.Sex.map({'female': 0, 'male': 1})
print(train.head())

#get_dummies()
print(pd.get_dummies(train.Sex, prefix='Sex').iloc[:, 1:])

#adding to the dataframe
sex_dummies = pd.get_dummies(train.Sex, prefix='Sex')\
  .iloc[:, 1:]
train=pd.concat([train, sex_dummies], axis=1)
print(train.head())

#passing dataframe to pd.get_dummies()
print(pd.get_dummies(train, columns=['Sex','Embarked'], \
  drop_first = True))