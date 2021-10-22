from glob import glob
import os
from numpy.core.numeric import NaN
import pandas as pd
import numpy as np
import src.utils as u
import re
import toml
from pandas import ExcelWriter
import openpyxl
from personal_functions import agg_functions, meeting_format
#imports functions from personal_functions doc

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# get the directory path where this script is
this_dir = os.path.dirname(os.path.realpath(__file__))
# grab the config file from this directory
config = toml.load(os.path.join(this_dir, 'config.toml'))
# prefix partial file paths found in the config.toml with the full path
u.set_full_paths(config, this_dir)

all_campaigns = pd.read_csv(config['file_locations']['all_campaigns'])
aas_schedule = pd.read_csv(config['file_locations']['aas_schedule'])
individual_titles_output = pd.read_excel(config['file_locations']['individual_titles_output'], sheet_name=None)

#drops columns from both dfs
all_campaigns.drop(columns=['State', 'Status', 'Campaign bidding strategy',
'Portfolio', 'Budget(USD)', 'Cost type', 'ROAS', 'Viewable impressions', 
'VCPM(USD)', 'Start date', 'End date'], 
inplace=True)
aas_schedule.drop(columns=['Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10'], inplace=True)

#adds underscore and deals with caps from both dfs
all_campaigns.columns = all_campaigns.columns.str.title().str.replace(' ', '_').str.replace('\(Usd\)', '')
all_campaigns.rename(columns={'Ctr': 'CTR', 'Cpc': 'CPC', 'Acos': 'ACOS'}, inplace=True)
aas_schedule.columns = aas_schedule.columns.str.replace(' ', '_')

#formatting type and targeting for all_campaigns
all_campaigns['Type'] = all_campaigns.Type.replace('SP', 'Sponsored Product')
all_campaigns['Targeting'] = all_campaigns.Targeting.str.title()

#merging start and end dates to all_campaigns
for_merge = aas_schedule.loc[:, ['Campaign_Name', 'Start_Date', 'End_Date']]
for_merge.drop(for_merge.loc[for_merge.Campaign_Name.isna(), :].index, inplace=True)
for_merge.rename(columns={'Campaign_Name': 'Campaigns'}, inplace=True)
merged_campaigns = pd.merge(all_campaigns, for_merge, on='Campaigns')

#sorting merged_campaigns
merged_campaigns.sort_values(['Orders', 'ACOS'], ascending=False, inplace=True)

#adding total row to merged_columns
merged_campaigns.loc['Total'] = merged_campaigns.sum(numeric_only=True, axis=0)
merged_campaigns.loc['Total', 'Campaigns'] = 'Total'

#adding total row to aas schedule Spend col
aas_schedule['Budget'] = aas_schedule.Budget.str.replace('\$|,', '')
aas_schedule['Budget'] = aas_schedule.Budget.str.split('.').str[0]
aas_schedule.dropna(how='all', inplace=True)
aas_schedule['Budget'] = aas_schedule.Budget.astype(int)
aas_schedule.loc['Total', 'Budget'] = aas_schedule.Budget.sum()
aas_schedule.loc['Total', 'Campaign'] = 'Total'

#calling agg_functions and meeting_format on merged_campaigns
agg_functions(merged_campaigns)
meeting_format(merged_campaigns)
#the above runs rate-based agg functions on CTR, CPC, and ACOS and formats doc for meeting

#reordering columns
reordered = merged_campaigns[['Campaigns', 'Start_Date', 'End_Date', 'Type', 'Targeting', 
'Impressions', 'Clicks', 'Orders', 'Spend', 'Sales', 'CTR', 'CPC', 'ACOS']]

#add to the individual_titles_output dictionary
individual_titles_output['aas_schedule'] = aas_schedule
individual_titles_output['all_campaigns'] = reordered

#reset the index of all sheets
for sheet in individual_titles_output:
  individual_titles_output[sheet].reset_index(drop=True, inplace=True)


#to save onto the multisheet xlsx with the rest of the data
file_location = ExcelWriter(config['file_locations']['all_data_output'])
for key in individual_titles_output:
  individual_titles_output[key].to_excel(file_location, key, index=False)
file_location.save()  
