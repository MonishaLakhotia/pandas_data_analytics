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

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# get the directory path where this script is
this_dir = os.path.dirname(os.path.realpath(__file__))
# grab the config file from this directory
config = toml.load(os.path.join(this_dir, 'config.toml'))
# prefix partial file paths found in the config.toml with the full path
u.set_full_paths(config, this_dir)

aas_schedule = pd.read_csv(config['file_locations']['aas_schedule'])
all_campaigns = pd.read_csv(config['file_locations']['all_campaigns'])

all_campaigns.drop(columns=['State', 'Status', 'Campaign bidding strategy',
'Portfolio', 'Budget(USD)', 'Cost type', 'ROAS', 'Viewable impressions', 'VCPM(USD)'], inplace=True)

all_campaigns.columns = all_campaigns.columns.str.title().str.replace(' ', '_').str.replace('\(Usd\)', '')
all_campaigns.rename(columns={'Ctr': 'CTR', 'Cpc': 'CPC', 'Acos': 'ACOS'}, inplace=True)
aas_schedule.columns = aas_schedule.columns.str.replace(' ', '_')

print(aas_schedule)

"""
NOTE:
TO DO:
AAS SCHEDULE:
-add underscores
-rename cols
-drop the unnamed cols, can leave the NaN rows I think
ALL CAMPAIGNS:
-Merging end dates
-fix the rate cols
-Change format of numeric cols


Need to add something about reading out from individual titles so I can merge this into that doc (or try to)
--if that doesn't work, then can just copy paste whatever happens here into the individual doc and rename

Also - make sure you add the schedule as a tab to the cleaned data doc because i need that too
-make sure to remove any unused libraries from the top too
"""