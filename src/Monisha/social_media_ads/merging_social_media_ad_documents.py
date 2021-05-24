#merge ad analytics documents for facebook/instagram and pinterest; eventually twitter

import pandas as pd

ad_schedule = pd.read_csv('~/Desktop/Social_Ads_Analytics_2020/SocialAdsSchedule_2020.csv')
facebook_instagram = pd.read_csv('~/Desktop/Social_Ads_Analytics_2020/FacebookData_2020.csv')
pinterest = pd.read_csv('~/Desktop/Social_Ads_Analytics_2020/PinterestData_2020.csv')

#facebook_instagram drop columns, rename columns, set index to Campaign_Name, rename Result_Type
facebook_instagram.drop(columns=['Reporting Starts', 'Reporting Ends', 'Ad Set Budget Type', 'Ends', 'Starts', 'Ad Set Budget'], inplace=True)
facebook_instagram.rename(columns={
  'Campaign Name': 'Campaign_Name',  
  'Amount Spent (USD)': 'Spend', 
  'Objective': 'Objective', 
  'Reach': 'Reach', 
  'Link Clicks': 'Clicks', 
  'Results': 'Results', 
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

#pinterest drop columns, rename columns, set index to Campaign_Name
pinterest.drop(columns=['Campaign status', 'Campaign ID', 'Campaign creative type', 'Cost per result type', 'Campaign Budget', 'Campaign start date/time', 'Campaign end date/time'], inplace=True)
pinterest.rename(columns={
  'Campaign name': 'Campaign_Name',
  'Spend': 'Spend', 
  'Reach': 'Reach', 
  'Paid outbound clicks': 'Clicks', 
  'Result': 'Results', 
  'Cost per result': 'Cost_Per_Result', 
  'Result type': 'Result_Type'}, inplace=True)
pinterest.set_index('Campaign_Name', inplace=True)

#ad_schedule rename 4 columns, set index to Campaign_Name, change Budget dtype to float, drop NaN values
ad_schedule.rename(columns={
  'Amount': 'Budget', 
  'Start Date': 'Start_Date', 
  'End Date': 'End_Date', 
  'Ad Name': 'Campaign_Name', 
  'Pub Day': 'Release_Date'}, inplace=True)
ad_schedule.set_index('Campaign_Name', inplace=True)
ad_schedule['Budget'] = ad_schedule.Budget.str.replace('$', '').str.replace(',', '').astype(float)
ad_schedule.drop(columns=['Platform', 'Type', 'When', '@', 'Media', 'Audience File', 'Notes', 'Unnamed: 15', 'Placements'], inplace=True)

#merging facebook_instagram and pinterest (eventually twitter)
social_merge = pd.concat([facebook_instagram, pinterest], axis=0)

#merging social_merge with ad_schedule - fixes issues with Budget, End_Date, Start_Date
ad_schedule_merge = pd.merge(social_merge, ad_schedule, left_index=True, right_index=True)

#changing date columns to datetime
ad_schedule_merge['End_Date'] = pd.to_datetime(ad_schedule_merge.End_Date)
ad_schedule_merge['Start_Date'] = pd.to_datetime(ad_schedule_merge.Start_Date)
ad_schedule_merge['Release_Date'] = pd.to_datetime(ad_schedule_merge.Release_Date)

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

#removing ',' from results and changing to float
ad_schedule_merge['Results'] = ad_schedule_merge.Results.str.replace(',', '').astype('float')

#change reach to float
ad_schedule_merge['Reach'] = ad_schedule_merge.Reach.astype('float')


"""
#SPECIFIC TO THIS DATAFRAME - Drop Christina Britton Rows - not sure on this
#print(ad_schedule_merge.Author.value_counts(dropna=False))
ad_schedule_merge.drop(ad_schedule_merge[ad_schedule_merge.Author == 'Christina Britton'].index, axis=0, inplace=True)
"""