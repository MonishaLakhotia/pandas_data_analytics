import numpy as np
import pandas as pd
import toml
from utils import foreach
from preprocessors.index import preprocessor_selector
from encoders.index import encoder_selector


def get_dataframe(dataConfig):
    return pd.read_csv(dataConfig['connectionstring']) if dataConfig['format'] == 'csv' \
        else None


def setEncoders(df, column):
    foreach(lambda step: setEncoder(
        df, step, column), column.get('encoding_steps'))


def setEncoder(df, step, column):
    if(step is not None):
        step['encoder'] = encoder_selector(
            step['algo'])(column['name'], df, step.get('settings'))


def encodersTransform(df, column):
    foreach(lambda step: encoderTransform(
        df, step), column.get('encoding_steps'))


def encoderTransform(df, step):
    if(step is not None):
        step['encoder'].transform(df)


def encodersInvert(df, column):
    foreach(lambda step: encoderInvert(
        df, step), column.get('encoding_steps'))


def encoderInvert(df, step):
    if(step is not None):
        step['encoder'].invert_transform(df)


def setPreprocessors(df, column):
    foreach(lambda step: setPreprocessor(
        df, step, column), column.get('preprocess_steps'))


def setPreprocessor(df, step, column):
    if(step is not None):
        step['preprocessor'] = preprocessor_selector(
            step['algo'])(column['name'], df, step.get('settings'))


def preprocessorsTransform(df, column):
    foreach(lambda step: preprocessorTransform(
        df, step), column.get('preprocess_steps'))


def preprocessorTransform(df, step):
    if(step is not None):
        step['preprocessor'].transform(df)


def preprocessorsInvert(df, column):
    foreach(lambda step: preprocessorInvert(
        df, step), column.get('preprocess_steps'))


def preprocessorInvert(df, step):
    if(step is not None):
        step['preprocessor'].invert_transform(df)


def clean_dataframe(dataframe, dfConfig):
    inputs = dfConfig['inputs']
    outputs = dfConfig['outputs']
    allColumns = inputs + outputs

    requiredColumns = [i['name'] for i in allColumns]

    df = dataframe[requiredColumns].copy()

    for c in allColumns:
        setPreprocessors(df, c)

    for c in allColumns:
        preprocessorsTransform(df, c)

    for c in allColumns:
        setEncoders(df, c)

    for c in allColumns:
        encodersTransform(df, c)

    l = [df.head(), df.dtypes, df.shape, df.columns, df.index]

    foreach(print, l)

    return df
