from numpy.core.numeric import NaN, outer
import pandas as pd
import numpy as np
import re

social_data = pd.read_csv('~/Desktop/test.csv')

#google data for function no_overlap()
ill_be_watching_you = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/Analytics HBG+Imprint_ Forever Ill Be Watching You - 2020 -  PaidSocial 20200306-20200508 - All Dates.csv', \
  skiprows=6)
cowboy_come_home = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/Test_CowboyComeHome_Analytics HBG+Imprint_ Forever Missing Keyword  - 2020 - PaidSocial 20200310-20200429.csv', \
  skiprows=6)
first_kiss_with_a_cowboy = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/First_Kiss_With_A_Cowboy_Analytics HBG+Imprint_ Forever Missing  Keyword - 2020 - PaidSocial 20200501-20200614-3.csv', \
  skiprows=6)

#google data that has keywords but no content tag, keywords content and one pinterest ad
keywords_no_content = pd.read_csv('~/Desktop/Google_Analytics_2020/Keywords_No_Content/W Paris Secret - Keywords No Content Analytics HBG+Imprint_ Forever  Full View 2020 20200101-20201231-7.csv', skiprows=6)
keywords_content_onepin = pd.read_csv('~/Desktop/Google_Analytics_2020/Keywords_Content_1Pinterest/Keywords Content One Pin Analytics HBG+Imprint_ Forever Full View  2020 20200101-20201231-5.csv', skiprows=6)

pd.set_option('display.max_columns', None)

#Setting Date columns to datetime
social_data['End_Date'] = pd.to_datetime(social_data.End_Date)
social_data['Start_Date'] = pd.to_datetime(social_data.Start_Date)
social_data['Release_Date'] = pd.to_datetime(social_data.Release_Date)
social_data['Book_Matching'] = social_data.Book.str.replace('\'', '').str.replace(' ', '')
#social_data.set_index('Campaign_Name', inplace=True)
#social_data['Users'] = NaN
#social_data['Click_To_Retail'] = NaN

#dropping rows marked that have no or limited google analytics data 
social_data.drop(social_data.loc[social_data.Campaign_Name.str.contains('AMZ|Walmart|Sweepstakes|PagePromo|Review|FindYourForeverTrope|Tote|BookPeoplePreOrder|Valentine', flags=re.IGNORECASE, regex=True), :].index, axis=0, inplace=True)
social_data.drop(social_data.loc[social_data.Campaign_Name.str.contains('List|_Christmas_'), :].index, axis=0, inplace=True)

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
  
  #drop Date_Range column and format Campaign Name to Book_Matching Style
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
  df_merged_new = df_merged.groupby('Campaign_Name').aggregate(agg_functions).copy()

  #is adding the x and y columns - will have to just remove them after merge
  list_of_globals = globals()
  #list_of_globals['social_data'] = pd.merge(social_data, df_merged_new, left_index=True, right_index=True, how='outer')
  list_of_globals['social_data'] = pd.merge(social_data, df_merged_new, left_on='Campaign_Name', right_index=True, how='outer')

#running no_overlap on the three without overlap dates
no_overlap(cowboy_come_home)
no_overlap(ill_be_watching_you)
no_overlap(first_kiss_with_a_cowboy)

#FOR KEYWORDS BUT NO CONTENT
#drop colums Date Range and Ad Content, drop the-paris-secret where keyword is (not set)
keywords_no_content.drop(['Date Range', 'Ad Content'], axis=1, inplace=True)
keywords_no_content.drop(keywords_no_content.loc[(keywords_no_content.Campaign == 'the-paris-secret') & (keywords_no_content.Keyword == '(not set)')].index, axis=0, inplace=True)
keywords_no_content.drop(keywords_no_content.loc[(keywords_no_content.Campaign == 'the-paris-secret') & (keywords_no_content.Keyword == 'bookdiscussionclub')].index, axis=0, inplace=True)

#separating out Users and Clicks to Retail, dropping Segment, and renaming the Users Column for Clicks to Retail df
keywords_no_content_ctr = keywords_no_content.loc[keywords_no_content.Segment == 'Click to Retail', :].drop(columns='Segment').rename(columns={'Users': 'Click_To_Retail'})
keywords_no_content_u = keywords_no_content.loc[keywords_no_content.Segment == 'All Users', :].drop(columns='Segment')

#merging Click to Retail and Users df into one
keywords_no_content_new = pd.merge(keywords_no_content_u, keywords_no_content_ctr, on=['Campaign', 'Source', 'Keyword']).copy()

#change Campaign to same style as Book Matching
keywords_no_content_new['Campaign'] = keywords_no_content_new.Campaign.str.replace('-', '').str.upper().copy()

#breaking out the Books that correspond to the keywords_no_content_new df Campaigns
keywords_matching = pd.DataFrame()
for value in keywords_no_content_new.Campaign:
  keywords_matching = pd.concat([keywords_matching, social_data.loc[value == social_data.Book_Matching, ['Campaign_Name', 'Book_Matching', 'Placements', 'Audience']]], axis=0).drop_duplicates()

#creating the Audience matching column in keywords_matching
keywords_matching['Audience'] = keywords_matching.Audience.str.split(' - ', expand=True)
keywords_matching['Audience'] = keywords_matching.Audience.str.replace(' ', '').str.lower()
keywords_matching['Audience'] = keywords_matching.Audience.str.replace('natashalester', 'parisorphanv1')

#changing Placements/Source columsn in keywords_matching and keyword_no_content_new for merge
keywords_matching.loc[keywords_matching.Placements.str.contains('FB'), 'Placements'] = 'Facebook'
keywords_matching.loc[keywords_matching.Placements.str.contains('Pin Feed'), 'Placements'] = 'Pinterest'
keywords_matching.loc[keywords_matching.Placements.str.contains('IG'), 'Placements'] = 'Instagram'
keywords_no_content_new['Source'] = keywords_no_content_new.Source.str.title().str.replace('Facebook-Instagram', 'Facebook')
keywords_no_content_new['Keyword'] = keywords_no_content_new.Keyword.replace('(not set)', NaN)
keywords_no_content_new['Users'] = keywords_no_content_new.Users.str.replace(',', '').astype(float)
keywords_no_content_new['Click_To_Retail'] = keywords_no_content_new.Click_To_Retail.astype(float)

#merging keywords_matching with keywords_no_content_new
no_content_merged = pd.merge(keywords_no_content_new, keywords_matching, left_on=['Campaign', 'Keyword', 'Source'], right_on=['Book_Matching', 'Audience', 'Placements'], how='outer')

#dropping columns from no_content_merged for merge to main social_ads df
no_content_merged.dropna(subset=['Campaign'], inplace=True)

no_content_merged.drop(columns=['Source', 'Keyword', 'Campaign', 'Book_Matching', 'Placements', 'Audience'], inplace=True)

#merging to main social doc
social_data = pd.merge(social_data, no_content_merged, on=['Campaign_Name'], how='outer',suffixes=('_z', '_a'))


#FOR KEYWORDS AND CONTENT AND ONE PINTEREST AD
#drop Date Range column
keywords_content_onepin.drop('Date Range', axis=1, inplace=True)

#separate out Users and Clicks to Retail
users = keywords_content_onepin.loc[keywords_content_onepin.Segment == 'All Users'].drop(columns='Segment')
clicks_to_retail = keywords_content_onepin.loc[keywords_content_onepin.Segment == 'Click to Retail'].drop(columns='Segment').rename(columns={'Users': 'Click_To_Retail'})

#merge Users and Clicks to Retail
keywords_content_onepin_new = pd.merge(users, clicks_to_retail)

#convert Users\s and Clicks to Retail to float
keywords_content_onepin_new['Users'] = keywords_content_onepin_new.Users.str.replace(',', '').astype(float)
keywords_content_onepin_new['Click_To_Retail'] = keywords_content_onepin_new.Click_To_Retail.astype(float)

#change Campaign to Book Matching Style
keywords_content_onepin_new['Campaign'] = keywords_content_onepin_new.Campaign.str.replace('-', '').str.upper().str.replace('ALADYSGUIDE', 'ALADYSGUIDETOMISCHIEFANDMAYHEM')

#breaking out the Books that correspond to the keywords_content_onepin_new df Campaigns
keywords_matching_2 = pd.DataFrame()
for value in keywords_content_onepin_new.Campaign:
  keywords_matching_2 = pd.concat([keywords_matching_2, social_data.loc[value == social_data.Book_Matching, ['Campaign_Name', 'Book_Matching', 'Placements', 'Audience', 'Objective', 'Result_Type']]], axis=0).drop_duplicates()

#creating the Audience matching column in keywords_matching_2
keywords_matching_2['Audience'] = keywords_matching_2.Audience.str.split(' - ', expand=True)
keywords_matching_2['Audience'] = keywords_matching_2.Audience.str.split('(', expand=True)
keywords_matching_2['Audience'] = keywords_matching_2.Audience.str.split('/', expand=True)
keywords_matching_2['Audience'] = keywords_matching_2.Audience.str.replace(' ', '').str.replace('\'', '').str.lower()

#changing Ad Content to Result_Type format
keywords_content_onepin_new['Ad Content'] = keywords_content_onepin_new['Ad Content'].str.replace('-', ' ').str.title().str.replace('Conversions', 'Conversion')
keywords_content_onepin_new.loc[keywords_content_onepin_new.Campaign == 'THETWELVEDOGSOFCHRISTMAS', 'Ad Content'] = keywords_content_onepin_new['Ad Content'].str.replace('Impressions', 'Conversion')

#changing Placements/Source columsn in keywords_matching and keyword_no_content_new for merge
keywords_matching_2.loc[keywords_matching_2.Placements.str.contains('FB'), 'Placements'] = 'Facebook'
keywords_matching_2.loc[keywords_matching_2.Placements.str.contains('Pin Feed'), 'Placements'] = 'Pinterest'
keywords_matching_2.loc[keywords_matching_2.Placements.str.contains('IG'), 'Placements'] = 'Instagram'
keywords_content_onepin_new['Source'] = keywords_content_onepin_new.Source.str.title().str.replace('Facebook-Instagram', 'Facebook')
keywords_content_onepin_new['Keyword'] = keywords_content_onepin_new.Keyword.replace('(not set)', NaN)
keywords_content_onepin_new['Ad Content'] = keywords_content_onepin_new['Ad Content'].replace('(Not Set)', 'Clicks')
keywords_content_onepin_new.loc[keywords_content_onepin_new.Campaign == 'ALADYSGUIDETOMISCHIEFANDMAYHEM', 'Ad Content'] = keywords_content_onepin_new['Ad Content'].str.replace('Landing Page Views', 'Link Clicks')

#merging keywords_matching_2 with keywords_content_onepin_new
keywords_content_onepin_merged = pd.merge(keywords_content_onepin_new, keywords_matching_2, left_on=['Campaign', 'Keyword', 'Source', 'Ad Content'], right_on=['Book_Matching', 'Audience', 'Placements', 'Result_Type'], how='outer')

#misc cleaning - drop Campaigns that have NaN values
keywords_content_onepin_merged.dropna(subset=['Campaign', 'Campaign_Name'], inplace=True)

#dropping columns from no_content_merged for merge to main social_ads df
keywords_content_onepin_merged.drop(columns=['Campaign', 'Source', 'Keyword', 'Ad Content', 'Book_Matching', 'Placements', 'Audience', 'Objective', 'Result_Type'], inplace=True)

#merging to social_data
social_data = pd.merge(social_data, keywords_content_onepin_merged, on=['Campaign_Name'], how='outer')

"""
##MOVE THIS AFTER THE NEXT ROUND -- haven't added this part to the doc notes
#adding the no_overlaps to create Users_New and Click_To_Retail_New
cols_Users = ['Users_x', 'Users_y', 'Users_z', 'Users_a']
social_data = social_data.assign(Users_New = social_data[cols_Users].sum(axis=1))

cols_Click_To_Retail = ['Click_To_Retail_a', 'Click_To_Retail_x', 'Click_To_Retail_y', 'Click_To_Retail_z']
social_data = social_data.assign(Click_To_Retail_New = social_data[cols_Click_To_Retail].sum(axis=1))

#drop unnecessary User and Click_To_Retail columns
social_data.drop(columns=['Users_x', 'Click_To_Retail_x', 'Click_To_Retail_y', 'Users_y', 'Click_To_Retail_a', 'Users_a', 'Click_To_Retail_z', 'Users_z'], inplace=True)

print(social_data.info())
##MOVE THIS AFTER THE NEXT ROUND - END

print(social_data.loc[social_data.Users_New != 0, :])


#for the merge, add the _drop kind of thing instead o letting it do _x
#END MOVE NOTES
"""