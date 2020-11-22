import numpy as np
import pandas as pd
from sklearn.decomposition import FastICA
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, make_union
from sklearn.preprocessing import PolynomialFeatures
from tpot.builtins import StackingEstimator
from xgboost import XGBClassifier
from tpot.export_utils import set_param_recursive
from utils import *

df = pd.read_csv('~/Downloads/PokeTypeMatchupData.csv')

# df.drop(['Postcode', 'Address'], inplace=True, axis=1)

fire = 'Fire'
water = 'Water'
grass = 'Grass'
types = [fire, water, grass]

df = df[types]

for t in types:
    df[t] = df[t].astype('category')
    df[t+'_cat'] = df[t].cat.codes

df.drop(types, axis=1, inplace=True)

l = [df.head(), df.dtypes, df.shape, df.columns, df.index]

foreach(print, l)

grasscat = grass+'_cat'

tpot_data = df
# NOTE: Make sure that the outcome column is labeled 'Grass_cat' in the data file
# tpot_data = pd.read_csv('~/Downloads/PokeTypeMatchupData.csv')
# tpot_data = pd.read_csv('PATH/TO/DATA/FILE',
# sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('Grass_cat', axis=1)
training_features, testing_features, training_target, testing_target = \
    train_test_split(features, tpot_data['Grass_cat'], random_state=42)

# Average CV score on the training set was: 0.7060144346431436
exported_pipeline = make_pipeline(
    StackingEstimator(estimator=ExtraTreesClassifier(bootstrap=False, criterion="entropy",
                                                     max_features=0.25, min_samples_leaf=3, min_samples_split=2, n_estimators=100)),
    FastICA(tol=0.0),
    PolynomialFeatures(degree=2, include_bias=False, interaction_only=False),
    XGBClassifier(learning_rate=0.5, max_depth=7, min_child_weight=19,
                  n_estimators=100, nthread=1, subsample=0.9000000000000001)
)
# Fix random state for all the steps in exported pipeline
set_param_recursive(exported_pipeline.steps, 'random_state', 42)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
print(results)
