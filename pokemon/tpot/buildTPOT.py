import numpy as np
import pandas as pd
from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer
from sklearn import preprocessing
from tpot.export_utils import set_param_recursive
from utils import *

import math

df = pd.read_csv('~/Downloads/PokeTypeMatchupData.csv')

fire = 'Fire'
water = 'Water'
grass = 'Grass'
types = [fire, water, grass]

df = df[types]

le = preprocessing.LabelEncoder()

for t in types:
    df[t] = le.fit_transform(df[t])
    # df[t] = df[t].astype('category')
    # df[t+'_cat'] = df[t].cat.codes

# df.drop(types, axis=1, inplace=True)

l = [df.head(), df.dtypes, df.shape, df.columns, df.index]

foreach(print, l)

# grasscat = grass+'_cat'
grasscat = grass

tpot_data = df
features = tpot_data.drop(grasscat, axis=1)
training_features, testing_features, training_target, testing_target = \
    train_test_split(features, tpot_data[grasscat], random_state=42)

tpot = TPOTClassifier(generations=50, population_size=50,
                      verbosity=2, random_state=42, memory='auto')
tpot.fit(training_features, training_target)
print(tpot.score(testing_features, testing_target))
tpot.export('tpot_poke_50_generations.py')

# # Average CV score on the training set was: 0.9826086956521738
# exported_pipeline = make_pipeline(
#     Normalizer(norm="l2"),
#     KNeighborsClassifier(n_neighbors=5, p=2, weights="distance")
# )
# # Fix random state for all the steps in exported pipeline
# set_param_recursive(exported_pipeline.steps, 'random_state', 42)

# exported_pipeline.fit(training_features, training_target)
# results = exported_pipeline.predict(testing_features)

print('end')
