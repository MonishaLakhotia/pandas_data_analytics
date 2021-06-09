from numpy.core.numeric import NaN
import pandas as pd
import numpy as np
import re

social_data = pd.read_csv('~/Desktop/test.csv')

#google data for function no_overlap()
ill_be_watching_you = pd.read_csv('~/Desktop/Analytics HBG+Imprint_ Forever Ill Be Watching You - 2020 -  PaidSocial 20200306-20200508 - All Dates.csv', \
  skiprows=6)

pd.set_option('display.max_columns', None)

#Setting Date columns to datetime
social_data['End_Date'] = pd.to_datetime(social_data.End_Date)
social_data['Start_Date'] = pd.to_datetime(social_data.Start_Date)
social_data['Release_Date'] = pd.to_datetime(social_data.Release_Date)
social_data['Book_Matching'] = social_data.Book.str.replace('\'', '').str.replace(' ', '')
social_data.set_index('Campaign_Name', inplace=True)

#dropping rows marked that have no or limited google analytics data 
social_data.drop(social_data.loc[social_data.index.str.contains('AMZ|Walmart|Sweepstakes|PagePromo|Review|FindYourForeverTrope|List|Tote', flags=re.IGNORECASE, regex=True), :].index, axis=0, inplace=True)

#function for campaigns where all start/end dates are unique and there is no overlap
def no_overlap(df):
  #create new column and fill with campaign name
  df['Campaign2'] = df.Campaign.iloc[0]

  #drop rows with NaN values
  df.dropna(subset=['Campaign'], how='any', inplace=True)
  
  #drop top rows with Campaign name and Source/Medium; drop Users and Bounce Rate
  df.drop(df.loc[df.Campaign == df.Campaign2, :].index, axis=0, inplace=True)
  df.drop(['Users', 'Bounce Rate'], axis=1, inplace=True)
  
  #drop row with second df column names and rename columns
  df.drop(7, axis=0, inplace=True)
  cols=['Day', 'Date_Range', 'Segment', 'Users', 'Campaign']
  df.columns=cols
  
  #drop Date_Range column and format Campaign Name to Campaign Name Style
  df.drop(['Date_Range'], axis=1, inplace=True)
  df['Campaign'] = df.Campaign.str.replace('-', '').str.upper()
  
  #set index to Day for merge of All Users and Clicks to Retail
  df.set_index('Day', inplace=True)
  
  #separate 'All Users' and 'Clicks to Retail'
  df_all_users = df.loc[df.Segment == 'All Users', :].copy()
  df_all_users.rename(columns={'Users': 'Users'}, inplace=True)
  df_all_users.drop('Segment', axis=1, inplace=True)
  
  df_click_to_retail = df.loc[df.Segment == 'Click to Retail', :].copy()
  df_click_to_retail.rename(columns={'Users': 'Click_To_Retail'}, inplace=True)
  df_click_to_retail.drop(['Segment', 'Campaign'], axis=1, inplace=True)
  
  #merging 'All Users' and 'Clicks to Retail
  df_merged = pd.merge(df_all_users, df_click_to_retail, left_index=True, right_index=True)
  
  #resetting index and changing day to datetime
  df_merged.reset_index(inplace=True)
  df_merged['Day'] = pd.to_datetime(df_merged.Day)
  
  #formatting
  df_merged['Users'] = df_merged.Users.astype(int)
  df_merged['Click_To_Retail'] = df_merged.Click_To_Retail.astype(int)
  
  #adding Campaign_Name to df
  df_merged['Campaign_Name'] = NaN
  
  #creating new df from slice of original df - might try to get this out later
  for value in df_merged.Campaign:
    social_segment = social_data.loc[social_data.Book_Matching == value, :].copy()
    social_segment.reset_index(inplace=True)
  
  #adding Campaign Names to df - note that this fills in some rows that should remain NaN but that's okay?
  for date in range(len(df_merged.Day)):
    for end_index in range(len(social_segment.End_Date)):
      for start_index in range(len(social_segment.Start_Date)):
        if (df_merged.Day[date] <= social_segment.End_Date[end_index]) & (df_merged.Day[date] >= social_segment.Start_Date[start_index]):
          df_merged['Campaign_Name'][date] = social_segment.Campaign_Name[end_index]
          
  #dropping the Day column for agg
  df_merged.drop(columns='Day', inplace=True)
  
  #aggregating click to retail and users in df_merged
  agg_functions = {'Click_To_Retail': 'sum', 'Users': 'sum'}
  df_merged_new = df_merged.groupby('Campaign_Name').aggregate(agg_functions)
  
  #merging df_merged_new to social_data
  global social_data_new
  social_data_new = pd.merge(social_data, df_merged_new, left_index=True, right_index=True, how='outer')

  return social_data_new

no_overlap(ill_be_watching_you)
print(social_data_new)

#next - import another ga doc to test this function
#then need to create the functions for the other two