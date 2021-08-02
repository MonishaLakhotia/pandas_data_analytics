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
cowboy_strong = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/Cowboy Strong Analytics HBG+Imprint_ Forever Make Mine a Cowboy -  2020 - PaidSocial 20200101-20201231-4.csv', \
  skiprows=6)
paradise_cove = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/paradise cove actual - Analytics HBG+Imprint_ Forever Make Mine a  Cowboy - 2020 - PaidSocial 20200101-20201231-6.csv', \
  skiprows=6)

#google data for function platform_specific_no_overlap()
a_good_duke_is_hard_to_find = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/a good duke is hard to find facebook Analytics HBG+Imprint_ Forever  Make Mine a Cowboy - 2020 - PaidSocial 20200101-20201231-11.csv', skiprows=6)
all_i_ask = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/all i ask  facebook Analytics HBG+Imprint_ Forever Make Mine a  Cowboy - 2020 - PaidSocial 20200101-20201231-9.csv', skiprows=6)
cant_hurry_love = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/cant hurry love facebook Analytics HBG+Imprint_ Forever Make Mine a  Cowboy - 2020 - PaidSocial 20200101-20201231-10.csv', skiprows=6)
mermaid_inn = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/mermaid inn facebookAnalytics HBG+Imprint_ Forever Make Mine a  Cowboy - 2020 - PaidSocial 20200101-20201231-7.csv', skiprows=6)
sunshine_on_silver_lake = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/sunshine on silver lake facebook Analytics HBG+Imprint_ Forever  Make Mine a Cowboy - 2020 - PaidSocial 20200101-20201231-8 (1).csv', skiprows=6)
a_duke_by_any_other_name_facebook = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/to add 1/a duke by any other name - facebook - platform specific Analytics  HBG+Imprint_ Forever Platform Specific No Overlap - 2020 - PaidSocial  20200101-20201231-6.csv', skiprows=6)
a_duke_by_any_other_name_instagram = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/to add 1/a duke by any other name - instagram - platform specific Analytics  HBG+Imprint_ Forever Platform Specific No Overlap - 2020 - PaidSocial  20200101-20201231-7.csv', skiprows=6)
forever_strong_facebook = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/to add 1/forever strong facebook - placement specific Analytics HBG+Imprint_  Forever Platform Specific No Overlap - 2020 - PaidSocial  20200101-20201231.csv', skiprows=6)
photos_of_you_instagram = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/to add 1/photos of you - instagram - platform specific Analytics  HBG+Imprint_ Forever Platform Specific No Overlap - 2020 - PaidSocial  20200101-20201231-4.csv', skiprows=6)
starting_over_at_blueberry_creek_instagram = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/to add 1/starting over blue insta platform spec Analytics HBG+Imprint_  Forever Platform Specific No Overlap - 2020 - PaidSocial  20200101-20201231-15.csv', skiprows=6)
starting_over_at_blueberry_creek_pinterest = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/to add 1/starting over at blueberry - pinterest - platform specificAnalytics  HBG+Imprint_ Forever Platform Specific No Overlap - 2020 - PaidSocial  20200101-20201231-1.csv', skiprows=6)
starting_over_at_blueberry_creek_facebook = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/to add 1/starting over at blueberry creek - facebook - platform specific  Analytics HBG+Imprint_ Forever Platform Specific No Overlap - 2020 -  PaidSocial 20200101-20201231-2.csv', skiprows=6)
the_highland_rogue_facebook = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/to add 1/the highland rogue - facebook - platform specificAnalytics  HBG+Imprint_ Forever Platform Specific No Overlap - 2020 - PaidSocial  20200101-20201231-5.csv', skiprows=6)
kiss_my_cupcake_pinterest = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/to add 2/kiss my cupcake - pinterest - platform specific Analytics  HBG+Imprint_ Forever Platform Specific No Overlap - 2020 - PaidSocial  20200101-20201231-13.csv', skiprows=6)
kiss_my_cupcake_facebook = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/to add 2/kiss my cupcake -facebook - platform specific Analytics  HBG+Imprint_ Forever Platform Specific No Overlap - 2020 - PaidSocial  20200101-20201231-14.csv', skiprows=6)
photos_of_you_facebook = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/to add 2/photos of you - facebook - platform specific Analytics HBG+Imprint_  Forever Platform Specific No Overlap - 2020 - PaidSocial  20200101-20201231-8.csv', skiprows=6)
the_boyfriend_project_pinterest = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/to add 2/the boyfriend project - pinterest - placement specific Analytics  HBG+Imprint_ Forever Platform Specific No Overlap - 2020 - PaidSocial  20200101-20201231-12.csv', skiprows=6)
the_happy_ever_after_playlist_instagram = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/to add 2/the happy ever after playlist - instagram - platform specific  Analytics HBG+Imprint_ Forever Platform Specific No Overlap - 2020 -  PaidSocial 20200101-20201231-11.csv', skiprows=6)
the_highland_rogue_pinterest = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/to add 2/the highland rogue - pinterest - platform specific Analytics  HBG+Imprint_ Forever Platform Specific No Overlap - 2020 - PaidSocial  20200101-20201231-9.csv', skiprows=6)

the_happy_ever_after_playlist_facebook = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/to add 3/hea playlist - 1 facebook test Analytics HBG+Imprint_ Forever  Platform Specific No Overlap - 2020 - PaidSocial 20200407-20200413-1.csv', skiprows=6)
dream_make_facebook = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/to add 3/dream maker - 1 facebook - test Analytics HBG+Imprint_ Forever  Platform Specific No Overlap - 2020 - PaidSocial 20200610-20200630.csv', skiprows=6)
the_boyfriend_project_facebook = pd.read_csv('~/Desktop/Google_Analytics_2020/No_Date_Overlap/misc/to add 3/the boyfriend project - 1 facebook - test Analytics HBG+Imprint_  Forever Platform Specific No Overlap - 2020 - PaidSocial  20200602-20200608-1.csv', skiprows=6)


#google data that has keywords but no content tag, keywords content and one pinterest ad
keywords_no_content = pd.read_csv('~/Desktop/Google_Analytics_2020/Keywords_No_Content/W Paris Secret - Keywords No Content Analytics HBG+Imprint_ Forever  Full View 2020 20200101-20201231-7.csv', skiprows=6)
keywords_content_onepin = pd.read_csv('~/Desktop/Google_Analytics_2020/Keywords_Content_1Pinterest/Actual Keywords ContentAnalytics HBG+Imprint_ Forever Full View  2020 20200101-20201231-9.csv', skiprows=6)

#google data for matching book title and platform
the_book_of_second_chances = pd.read_csv('~/Desktop/Google_Analytics_2020/Book_Title_Platform_Match/The Book of Second Chances Analytics HBG+Imprint_ Forever Book and  Platform 2020 20200101-20201231.csv', skiprows=6)
one_pinterest = pd.read_csv('~/Desktop/Google_Analytics_2020/Book_Title_Platform_Match/Pinterest Ads Book Platform match Analytics HBG+Imprint_ Forever  Book and Platform 2020 20200101-20201231-1.csv', skiprows=6)
one_instagram = pd.read_csv('~/Desktop/Google_Analytics_2020/Book_Title_Platform_Match/Instagram take 2Analytics HBG+Imprint_ Forever Book and Platform  2020 20200101-20201231-3.csv', skiprows=6)

pd.set_option('display.max_columns', None)

#Setting Date columns to datetime, misc cleaning, adding Book Matching and Placement Matching columns
social_data['End_Date'] = pd.to_datetime(social_data.End_Date)
social_data['Start_Date'] = pd.to_datetime(social_data.Start_Date)
social_data['Release_Date'] = pd.to_datetime(social_data.Release_Date)
social_data['Book'] = social_data.Book.str.replace('SUMMER ON HONEYSUCKLE', 'SUMMER ON HONEYSUCKLE RIDGE')
social_data['Book_Matching'] = social_data.Book.str.replace('\'', '').str.replace(' ', '')
#social_data.set_index('Campaign_Name', inplace=True)
#social_data['Users'] = NaN
#social_data['Click_To_Retail'] = NaN
social_data.drop(social_data.loc[social_data.Placements.isna(), :].index, axis=0, inplace=True)
social_data.loc[(social_data.Book_Matching == 'KISSMYCUPCAKE') & (social_data.Campaign_Name.str.contains('IGAd')), 'Placements'] = social_data.Placements.str.replace('FB Feed, IG Feed, IG Explore, IG Stories', 'IG Feed, IG Explore, IG Stories')
social_data['Placement_Matching'] = social_data.Placements
social_data.loc[social_data.Placement_Matching.str.contains('FB'), 'Placement_Matching'] = 'Facebook'
social_data.loc[social_data.Placement_Matching.str.contains('Pin Feed'), 'Placement_Matching'] = 'Pinterest'
social_data.loc[social_data.Placement_Matching.str.contains('IG'), 'Placement_Matching'] = 'Instagram'

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
  list_of_globals['social_data'] = pd.merge(social_data, df_merged_new, left_on='Campaign_Name', right_index=True, how='outer')

#running no_overlap on the five without overlap dates
no_overlap(cowboy_come_home)
no_overlap(ill_be_watching_you)
no_overlap(first_kiss_with_a_cowboy)
no_overlap(cowboy_strong)
no_overlap(paradise_cove)


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

#misc cleaning
keywords_matching_2['Result_Type'] = keywords_matching_2.Result_Type.str.replace('Reach', 'Impressions')
keywords_matching_2.loc[(keywords_matching_2.Book_Matching == 'FOREVERWITHYOU') & (keywords_matching_2.Audience == 'contemporaryromance'), 'Result_Type'] = keywords_matching_2.Result_Type.str.replace('Impressions', 'Landing Page Views')
keywords_matching_2.loc[(keywords_matching_2.Book_Matching == 'WHENAROGUEMEETSHISMATCH') & (keywords_matching_2.Audience == 'historicalromance'), 'Placements'] = keywords_matching_2.Placements.str.replace('Instagram', 'Facebook')

#merging keywords_matching_2 with keywords_content_onepin_new
keywords_content_onepin_merged = pd.merge(keywords_content_onepin_new, keywords_matching_2, left_on=['Campaign', 'Keyword', 'Source', 'Ad Content'], right_on=['Book_Matching', 'Audience', 'Placements', 'Result_Type'], how='outer')

#misc cleaning - drop Campaigns that have NaN values
keywords_content_onepin_merged.dropna(subset=['Campaign', 'Campaign_Name'], inplace=True)

#dropping columns from no_content_merged for merge to main social_ads df
keywords_content_onepin_merged.drop(columns=['Campaign', 'Source', 'Keyword', 'Ad Content', 'Book_Matching', 'Placements', 'Audience', 'Objective', 'Result_Type'], inplace=True)

#merging to social_data
social_data = pd.merge(social_data, keywords_content_onepin_merged, on=['Campaign_Name'], how='outer')


#BACK TO NO CONTENT, BUT DIFFERENT PLATFORMS
def book_platform(df2):
  #drop Date Range
  df2.drop('Date Range', axis=1, inplace=True)

  #changing Campaign to Book_Matching
  df2['Campaign'] = df2.Campaign.str.replace('-', '').str.upper()

  #separate All Users from Click to Retail and merge
  df2_users = df2.loc[df2.Segment == 'All Users', :].drop('Segment', axis=1)
  df2_ctr = df2.loc[df2.Segment == 'Click to Retail', :].rename(columns={'Users': 'Click_To_Retail'}).drop('Segment', axis=1)
  df2_merged = pd.merge(df2_users, df2_ctr)

  #converting Users and Click_To_Retail to float
  df2_merged['Users'] = df2_merged.Users.str.replace(',', '').astype(float)
  df2_merged['Click_To_Retail'] = df2_merged.Click_To_Retail.astype(float)

  #creating the matching DataFrame
  platform_matching = pd.DataFrame()
  for value in df2_merged.Campaign:
    platform_matching = pd.concat([platform_matching, social_data.loc[value == social_data.Book_Matching, ['Campaign_Name', 'Book_Matching', 'Placements']]], axis=0).drop_duplicates()

  #formatting Source and Placements
  platform_matching['Placements'] = platform_matching.Placements.str.lower()
  platform_matching.loc[platform_matching.Placements.str.contains('fb'), 'Placements'] = 'facebook'
  platform_matching.loc[platform_matching.Placements.str.contains('pin feed'), 'Placements'] = 'pinterest'
  platform_matching.loc[platform_matching.Placements.str.contains('ig'), 'Placements'] = 'instagram'
  df2_merged['Source'] = df2_merged.Source.str.replace('facebook-instagram', 'facebook')

  #merging platform_matching and df2_merged
  platform_merged = pd.merge(platform_matching, df2_merged, left_on=['Book_Matching', 'Placements'], right_on=['Campaign', 'Source'])
  
  #dropping unnecessary columns
  platform_merged.drop(['Book_Matching', 'Placements', 'Source', 'Campaign'], axis=1, inplace=True)
  
  #is adding the x and y columns - will have to just remove them after merge
  list_of_globals = globals()
  #list_of_globals['social_data'] = pd.merge(social_data, df_merged_new, left_index=True, right_index=True, how='outer')
  list_of_globals['social_data'] = pd.merge(social_data, platform_merged, on='Campaign_Name', how='outer')

book_platform(the_book_of_second_chances)
book_platform(one_pinterest)
book_platform(one_instagram)


#PLATFORM SPECIFIC NO OVERLAP - Basically the last of what's left for the books who's one pin or one insta got added
def platform_specific_no_overlap(df):
  #create new column and fill with campaign name
  df['Campaign2'] = df.Campaign.iloc[0]
  df['Placement2'] = df['Source / Medium'].iloc[0]
  df['Placement2'] = df.Placement2.str.split(' / ', expand=True)
  df['Placement2'] = df.Placement2.str.replace('facebook', 'Facebook')
  df['Placement2'] = df.Placement2.str.replace('facebook-instagram', 'Facebook')
  df['Placement2'] = df.Placement2.str.replace('instagram', 'Instagram')
  df['Placement2'] = df.Placement2.str.replace('pinterest', 'Pinterest')

  #drop rows with NaN values
  df.dropna(subset=['Campaign'], how='any', inplace=True)
  
  #drop top rows with Campaign name and Source/Medium; drop Users and Bounce Rate
  df.drop(df.loc[df.Campaign == df.Campaign2, :].index, axis=0, inplace=True)
  df.drop(['Users', 'Bounce Rate'], axis=1, inplace=True)
  
  #drop row with second df column names and rename columns
  df.drop(7, axis=0, inplace=True)
  
  #ADDED PLACEMENT
  cols=['Day', 'Date_Range', 'Segment', 'Users', 'Campaign', 'Placement']
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
  df_merged.drop('Placement_x', axis=1, inplace=True)
  df_merged['Placement_y'] = df_merged.Placement_y.str.replace('Facebook-Instagram', 'Facebook')
  df_merged['Placement_y'] = df_merged.Placement_y.str.replace('instagram', 'Instagram')
  df_merged['Placement_y'] = df_merged.Placement_y.str.replace('pinterest', 'Pinterest')

  #adding Campaign_Name to df
  df_merged['Campaign_Name'] = NaN

  df_merged.drop(df_merged.loc[df_merged.Users == 0, :].index, axis=0, inplace=True)
  df_merged.reset_index(inplace=True)

  #ADDED PLACEMENT MATCHING
  #creating new df from slice of original df - might try to get this out later
  for value in df_merged.Campaign:
    for placement in df_merged.Placement_y:
      social_segment = social_data.loc[(social_data.Book_Matching == value) & (social_data.Placement_Matching == placement), ['Campaign_Name', 'Book_Matching', 'Placements', 'Start_Date', 'End_Date']].copy()
      social_segment.reset_index(inplace=True)

  social_segment.drop(social_segment.loc[social_segment.Campaign_Name.str.contains('IGBoost'), :].index, axis=0, inplace=True)
  social_segment.drop_duplicates(subset='Start_Date', keep=False, inplace=True)  
  social_segment.reset_index(inplace=True)
  #adding Campaign Names to df - note that this fills in some rows that should remain NaN but that's okay?
  for date in range(len(df_merged.Day)):
    for end_index in range(len(social_segment.End_Date)):
      for start_index in range(len(social_segment.Start_Date)):
        if (df_merged.Day[date] >= social_segment.Start_Date[start_index]) & (df_merged.Day[date] <= social_segment.End_Date[end_index]):
          df_merged['Campaign_Name'][date] = social_segment.Campaign_Name[end_index]
  
  #dropping the Day column for agg
  df_merged.drop(columns='Day', inplace=True)

  #aggregating click to retail and users in df_merged
  agg_functions = {'Click_To_Retail': 'sum', 'Users': 'sum'}
  df_merged_new = df_merged.groupby('Campaign_Name').aggregate(agg_functions).copy()

  #is adding the x and y columns - will have to just remove them after merge
  list_of_globals = globals()
  list_of_globals['social_data'] = pd.merge(social_data, df_merged_new, left_on='Campaign_Name', right_index=True, how='outer')


#running platform_specific_no_overlap on the data that qualifies
platform_specific_no_overlap(a_good_duke_is_hard_to_find)
platform_specific_no_overlap(all_i_ask)
platform_specific_no_overlap(cant_hurry_love)
platform_specific_no_overlap(mermaid_inn)
platform_specific_no_overlap(sunshine_on_silver_lake)
platform_specific_no_overlap(a_duke_by_any_other_name_facebook)
platform_specific_no_overlap(a_duke_by_any_other_name_instagram)
platform_specific_no_overlap(forever_strong_facebook)
platform_specific_no_overlap(photos_of_you_facebook)
platform_specific_no_overlap(starting_over_at_blueberry_creek_instagram)
platform_specific_no_overlap(starting_over_at_blueberry_creek_pinterest)
platform_specific_no_overlap(starting_over_at_blueberry_creek_facebook)
platform_specific_no_overlap(the_highland_rogue_facebook)
platform_specific_no_overlap(the_highland_rogue_pinterest)
platform_specific_no_overlap(kiss_my_cupcake_pinterest)
platform_specific_no_overlap(kiss_my_cupcake_facebook)
platform_specific_no_overlap(the_boyfriend_project_pinterest)
platform_specific_no_overlap(the_happy_ever_after_playlist_instagram)
platform_specific_no_overlap(the_happy_ever_after_playlist_facebook)
platform_specific_no_overlap(dream_make_facebook)
platform_specific_no_overlap(the_boyfriend_project_facebook)

#adding all Users and Click_To_Retail columns into one and dropping unnecessary columns
cols_Users = [column for column in social_data.columns if re.match('Users.*', column)]
social_data = social_data.assign(Total_Users = social_data[cols_Users].sum(axis=1))

cols_Click_To_Retail = [column for column in social_data.columns if re.match('Click_To_Retail.*', column)]
social_data = social_data.assign(Total_Click_To_Retail = social_data[cols_Click_To_Retail].sum(axis=1))

social_data.drop(columns=social_data.loc[: , social_data.columns.str.contains('^Users.*|^Click_To_Retail.*')], inplace=True)

#misc cleaning
social_data.drop(columns=['Book_Matching', 'Placement_Matching'], inplace=True)
social_data.replace([np.inf, -np.inf], np.nan, inplace=True)
social_data.replace(0, NaN, inplace=True)
social_data.Clicks.fillna(0, inplace = True)
social_data.loc[social_data.Clicks < social_data.Total_Users, ['Total_Users', 'Total_Click_To_Retail']] = NaN

#creating cost per User and Click_To_Retail columns
social_data['Cost_Per_User'] = social_data['Spend']/social_data['Total_Users']
social_data['Cost_Per_Click_To_Retail'] = social_data['Spend']/social_data['Total_Click_To_Retail']

#print(social_data.loc[(social_data.Clicks == NaN) & (social_data.Total_Users != NaN)])
print(social_data.loc[social_data.Result_Type == 'Clicks', :])
social_data.to_csv('~/Desktop/google_merge_test.csv')
print('done')


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