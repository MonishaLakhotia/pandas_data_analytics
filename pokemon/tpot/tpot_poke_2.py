import math
import numpy as np
import pandas as pd
from sklearn.kernel_approximation import RBFSampler
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, make_union
from tpot.builtins import StackingEstimator
from tpot.export_utils import set_param_recursive
from sklearn.preprocessing import Normalizer
from sklearn import preprocessing
from tpot.export_utils import set_param_recursive
# import '../../utils'
from utils import *
# utils = __import__('../../utils')


df = pd.read_csv('~/Downloads/PokeTypeMatchupData.csv')


fire = 'Fire'
water = 'Water'
grass = 'Grass'
types = [fire, water, grass]

df = df[types]

labelEncoders = get_label_encoders(types, df)

label_encode_transform(labelEncoders, types, df)

l = [df.head(), df.dtypes, df.shape, df.columns, df.index]

foreach(print, l)

# grasscat = grass+'_cat'
grasscat = grass

tpot_data = df
# NOTE: Make sure that the outcome column is labeled 'target' in the data file
# tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop(grasscat, axis=1)
training_features, testing_features, training_target, testing_target = \
    train_test_split(features, tpot_data[grasscat], random_state=42)

# Average CV score on the training set was: 0.7059877038225073
exported_pipeline = make_pipeline(
    RBFSampler(gamma=0.8),
    StackingEstimator(estimator=LogisticRegression(
        C=0.1, dual=False, penalty="l2")),
    SGDClassifier(alpha=0.0, eta0=0.1, fit_intercept=True, l1_ratio=0.25,
                  learning_rate="invscaling", loss="log", penalty="elasticnet", power_t=0.0)
)
# Fix random state for all the steps in exported pipeline
set_param_recursive(exported_pipeline.steps, 'random_state', 42)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)

pd_results = pd.DataFrame(results)

pd_results[grass] = pd_results[0]

pd_results.drop(0, axis=1, inplace=True)


fullSet = testing_features.merge(pd_results, left_index=True, right_index=True)

label_encode_inverse_transform(labelEncoders, types, fullSet)

# print(pd_results.head())
print(fullSet.head(100))

# print(testing_features[0:5])
# print(results[0:5])
# print(list(zip(testing_features, results)))
