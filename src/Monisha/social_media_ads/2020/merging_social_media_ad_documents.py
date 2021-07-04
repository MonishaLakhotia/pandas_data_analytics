#merge ad analytics documents for facebook/instagram and pinterest with social ads schedule; eventually twitter

from numpy.core.numeric import NaN
import pandas as pd
import numpy as np
import re
import os
import toml
import src.utils as u

# get the directory path where this script is
this_dir = os.path.dirname(os.path.realpath(__file__))
# grab the config file from this directory
config = toml.load(os.path.join(this_dir, 'config.toml'))
# prefix partial file paths found in the config.toml with the full path
u.set_full_paths(config, this_dir)

ad_schedule = pd.read_csv(config['file_locations']['ad_schedule'])
facebook_instagram = pd.read_csv(config['file_locations']['facebook_instagram'])
pinterest = pd.read_csv(config['file_locations']['pinterest'])
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#facebook_instagram drop columns, rename columns, set index to Campaign_Name, rename Result_Type
facebook_instagram.drop(columns=['Reporting Starts', 'Reporting Ends', 'Ad Set Budget Type', 'Ends', 'Starts', 'Ad Set Budget'], inplace=True)
facebook_instagram.rename(columns={
  'Campaign Name': 'Campaign_Name',  
  'Amount Spent (USD)': 'Spend', 
  'Link Clicks': 'Clicks', 
  'Result Indicator': 'Result_Type', 
  'Cost per Results': 'Cost_Per_Result'}, inplace=True)
facebook_instagram.set_index('Campaign_Name', inplace=True)
facebook_instagram.Result_Type.replace({
  'actions:link_click': 'Link Clicks', 
  'actions:post_engagement': 'Engagement', 
  'actions:like': 'Page Likes', 
  'actions:landing_page_view': 'Landing Page Views', 
  'video_thruplay_watched_actions': 'Video Views', 
  'actions:offsite_conversion.fb_pixel_add_to_cart': 'Conversion', 
  'reach': 'Reach'}, inplace=True)
facebook_instagram['Results'] = facebook_instagram.Results.replace(',', '')

#facebook_instagram.columns = facebook_instagram.columns.str.strip().str.replace('\s+', '_', regex=True)
#print(facebook_instagram.columns)
#pinterest drop columns, rename columns, set index to Campaign_Name
pinterest.drop(columns=['Campaign status', 'Campaign ID', 'Campaign creative type', 'Cost per result type', 'Campaign Budget', 'Campaign start date/time', 'Campaign end date/time'], inplace=True)
pinterest.rename(columns={
  'Campaign name': 'Campaign_Name', 
  'Paid outbound clicks': 'Clicks', 
  'Result': 'Results', 
  'Cost per result': 'Cost_Per_Result', 
  'Result type': 'Result_Type'}, inplace=True)
pinterest.set_index('Campaign_Name', inplace=True)
pinterest['Results'] = pinterest.Results.str.replace(',', '')

#ad_schedule rename 4 columns, set index to Campaign_Name, change Budget dtype to float, drop NaN values
ad_schedule.rename(columns={
  'Amount': 'Budget', 
  'Start Date': 'Start_Date', 
  'End Date': 'End_Date',
  'Ad Name': 'Campaign_Name', 
  'Pub Day': 'Release_Date',
  '@': 'Daily_Budget'}, inplace=True)
ad_schedule.set_index('Campaign_Name', inplace=True)
ad_schedule['Budget'] = ad_schedule.Budget.str.replace('\$|,','',regex=True).astype(float)
ad_schedule.drop(columns=['Type', 'When', 'Media', 'Audience File', 'Notes', 'Unnamed: 15', 'Platform'], inplace=True)

#merging facebook_instagram and pinterest (eventually twitter)
social_merge = pd.concat([facebook_instagram, pinterest], axis=0)

#merging social_merge with ad_schedule - fixes issues with Budget, End_Date, Start_Date
ad_schedule_merge = pd.merge(social_merge, ad_schedule, left_index=True, right_index=True)

#changing date columns to datetime
date_col = [column for column in ad_schedule_merge.columns if re.match('.*_Date',column)]
for name in date_col:
  ad_schedule_merge[name] = pd.to_datetime(ad_schedule_merge[name])

#dropping rows where spend == 0
ad_schedule_merge.drop(ad_schedule_merge.loc[ad_schedule_merge.Spend == 0, :].index, axis=0, inplace=True)

#changing objective to str.title()
ad_schedule_merge['Objective'] = ad_schedule_merge.Objective.str.title()

#filling Pinterest objective using Result_Type and Index Contains
for value in ad_schedule_merge.Objective:
  if ad_schedule_merge.Objective.isna().any():
    if ad_schedule_merge.index.str.contains('Pinterest').any():
      if ad_schedule_merge.Result_Type.all() == 'Clicks':        
        ad_schedule_merge.Objective.fillna('Traffic', inplace=True)
      elif ad_schedule_merge.Result_Type.all() == 'Impressions':
        ad_schedule_merge.Objective.fillna('Brand Awareness', inplace=True)

#filling NaN in clicks with 0.0
ad_schedule_merge.Clicks.fillna(0.0, inplace=True)

#changing Results and Reach to float
for column in ['Results', 'Reach']:
  ad_schedule_merge[column] = ad_schedule_merge[column].astype('float')

#creating CPM, CPC, CTR column - calculations using reach
ad_schedule_merge['CPM'] = (ad_schedule_merge['Spend'] / ad_schedule_merge['Reach']) * 1000
ad_schedule_merge['CPC'] = (ad_schedule_merge['Spend'] / ad_schedule_merge['Clicks'])
ad_schedule_merge['CTR'] = (ad_schedule_merge['Clicks'] / ad_schedule_merge['Reach'])

#replacing CPC inf values with NaN
ad_schedule_merge.CPC.replace([np.inf, -np.inf], np.nan, inplace=True)

#reordering columns
reordered = ad_schedule_merge[['Book', 'Author', 'Release_Date', 'Start_Date', 'End_Date', 'Budget', 'Daily_Budget', 'Spend', 'Placements', 'Audience', 'Objective', 'Reach', 'Clicks', 'CPM', 'CPC', 'CTR', 'Results', 'Cost_Per_Result', 'Result_Type']]

#sending to csv
reordered.to_csv('~/Desktop/test.csv')

#move the ga part to a new doc