import numpy as np
import pandas as pd
import toml
from pokemon.tpot.clean import *
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, make_union
from sklearn.kernel_approximation import RBFSampler
from sklearn.linear_model import LogisticRegression, SGDClassifier
from tpot.builtins import StackingEstimator
from tpot.export_utils import set_param_recursive
from sklearn.preprocessing import Normalizer
from encoders.index import encoder_selector
import joblib


def build(config):
    df = clean_dataframe(
        get_dataframe(config['data']), config['dataframe'])
    outputs = [v['name'] for v in config['dataframe']['outputs']]

    tpot_data = df
    # NOTE: Make sure that the outcome column is labeled 'target' in the data file
    # tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
    features = tpot_data.drop(outputs, axis=1)
    training_features, testing_features, training_target, testing_target = \
        train_test_split(features, tpot_data[outputs], random_state=42)

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

    exported_pipeline.fit(training_features, training_target.values.ravel())
    joblib_file = config['model_file']
    joblib.dump(exported_pipeline, joblib_file)


config = toml.load("pokemon/tpot/config.toml")
build(config)
