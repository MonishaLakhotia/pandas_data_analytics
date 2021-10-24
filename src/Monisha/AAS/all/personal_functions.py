# personal_functions>
import numpy as np

def agg_functions(df):
  df['CTR'] = df.Clicks / df.Impressions
  df['CPC'] = df.Spend / df.Clicks
  df['ACOS'] = df.Spend / df.Sales
  df.ACOS.replace([np.inf, -np.inf], np.nan, inplace=True)
  df.CTR.replace(0, np.nan, inplace=True)

def meeting_format(df):
  df[['Spend', 'Sales', 'CPC']] = df[['Spend', 'Sales', 'CPC']].apply(
    lambda series: series.apply(lambda x: '${:,.2f}'.format(x)))
  df[['CTR', 'ACOS']] = df[['CTR', 'ACOS']].apply(
    lambda series: series.apply(lambda x: '{:.2f}%'.format((x*100))))
  df[['Impressions', 'Clicks', 'Orders']] = df[['Impressions', 'Clicks', 'Orders']].apply(
    lambda series: series.apply(lambda x: '{:,}'.format(x)))