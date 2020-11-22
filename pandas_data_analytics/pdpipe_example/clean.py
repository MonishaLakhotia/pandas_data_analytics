
import re
import pdpipe as pdp
import pandas_data_analytics.pdpipe_example.pipe_utils as pu
import pandas as pd


def get_pipeline():
    colsToInt = ['Price', 'Avg. Area Income', 'Avg. Area House Age',
                 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Area Population']
    pipeline = pdp.ColDrop(['Address'])
    pipeline += pdp.ApplyByCols(colsToInt, pu.toInt, colsToInt, drop=True)
    pipeline += pdp.ApplyByCols('Avg. Area Number of Rooms',
                                pu.size, 'House_Size', drop=False)
    pipeline += pdp.OneHotEncode('House_Size', drop=True)
    return pipeline


def clean_dataframe(df, pipeline):
    cdf = pipeline(df)
    cdf = cdf.rename(columns={element: re.sub(r'^Avg. Area ', r'', element,
                                              flags=re.I) for element in df.columns.tolist()})
    cdf = cdf.rename(columns={element: re.sub(r'\s+', r'_', element,
                                              flags=re.I) for element in cdf.columns.tolist()})
    return cdf
