import pandas as pd
import toml
import joblib
from sklearn.model_selection import train_test_split
from pokemon.tpot.clean import *


def use(config):
    inputs = config['dataframe']['inputs']
    output = config['dataframe']['outputs'][0]['name']
    joblib_file = config['model_file']
    model = joblib.load(joblib_file)
    df = clean_dataframe(
        get_dataframe(config['data']), config['dataframe'])
    outputs = [v['name'] for v in config['dataframe']['outputs']]

    tpot_data = df
    # NOTE: Make sure that the outcome column is labeled 'target' in the data file
    # tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
    features = tpot_data.drop(outputs, axis=1)
    training_features, testing_features, training_target, testing_target = \
        train_test_split(features, tpot_data[outputs], random_state=42)
    results = model.predict(testing_features)

    pd_results = pd.DataFrame(results)

    pd_results[output] = pd_results[0]

    pd_results.drop(0, axis=1, inplace=True)

    fullSet = testing_features.merge(
        pd_results, left_index=True, right_index=True)

    dfConfig = config['dataframe']

    inputs = dfConfig['inputs']
    outputs = dfConfig['outputs']
    allColumns = inputs + outputs

    for c in allColumns:
        preprocessorsInvert(fullSet, c)

    for c in allColumns:
        encodersInvert(fullSet, c)

    # print(pd_results.head())
    print(fullSet.head(100))

    # print(testing_features[0:5])
    # print(results[0:5])
    # print(list(zip(testing_features, results)))


config = toml.load("pokemon/tpot/config.toml")
use(config)
