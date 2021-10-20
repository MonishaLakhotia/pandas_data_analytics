from glob import glob
import os
from numpy.core.numeric import NaN
import pandas as pd
import numpy as np
import src.utils as u
import re
import toml
from datetime import date
from dateutil.relativedelta import relativedelta
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
merged_campaigns.reset_index(drop=True, inplace=True)

#calling agg_functions and meeting_format on merged_campaigns
agg_functions(merged_campaigns)
meeting_format(merged_campaigns)
#the above runs rate-based agg functions on CTR, CPC, and ACOS and formats doc for meeting

#reordering columns
reordered = merged_campaigns[['Campaigns', 'Start_Date', 'End_Date', 'Type', 'Targeting', 
'Impressions', 'Clicks', 'Orders', 'Spend', 'Sales', 'CTR', 'CPC', 'ACOS']]

#print(for_merge.dtypes)
#print(aas_schedule.dtypes)
print(reordered)
#print(all_campaigns.dtypes)
#ValueError: You are trying to merge on float64 and object columns. If you wish to proceed you should use pd.concat

"""
NOTE:
TO DO:
AAS SCHEDULE:
-drop the unnamed cols, can leave the NaN rows I think
ALL CAMPAIGNS:
-add a total line


Need to add something about reading out from individual titles so I can merge this into that doc (or try to)
--if that doesn't work, then can just copy paste whatever happens here into the individual doc and rename

Also - make sure you add the schedule as a tab to the cleaned data doc because i need that too
-make sure to remove any unused libraries from the top too

Make sure to check the email with To-Dos for anything too
"""