import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import toml
import src.utils as u
import re

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))
u.set_full_paths(config, this_dir)

social_merged = pd.read_csv(config['file_locations']['social_merged'])
google_merged = pd.read_csv(config['file_locations']['google_merged'])
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#merging social data and google data
all_data = pd.concat([social_merged, google_merged])

#misc cleaning - drop duplicates, drop unnamed col, change date cols to date time
all_data.drop_duplicates(subset='Campaign_Name', keep='last', inplace=True)
all_data.drop(columns='Unnamed: 0', inplace=True)

date_cols = [column for column in all_data.columns if re.match('.*Date', column)]
for name in date_cols:
  all_data[name] = pd.to_datetime(all_data[name])

#breaking up by objective
print(all_data.Objective.value_counts())
traffic = all_data.loc[all_data.Objective == 'Traffic', :]
conversions = all_data.loc[all_data.Objective == 'Conversions', :]
engagement = all_data.loc[all_data.Objective == 'Engagement', :]
reach = all_data.loc[all_data.Objective == 'Reach', :]
page_likes = all_data.loc[all_data.Objective == 'Page Likes', :]
video_views = all_data.loc[all_data.Objective == 'Video Views', :]
"""
Presentation notes
Traffic        200
Conversions     26
Engagement      13
Reach            9
Page Likes       3
Video Views      2

Traffic breakdown:
Link Clicks           94
Landing Page Views    59
Clicks                43
Impressions            4
"""

print(traffic.loc[traffic.Result_Type == 'Impressions'])

#sns.barplot(x='Objective', y='Reach', data=all_data)
#sns.barplot(x='Objective', y='Clicks', data=all_data)
#sns.barplot(x='Objective', y='CPM', data=all_data)
#sns.barplot(x='Result_Type', y='CPM', data=all_data)
#sns.barplot(x='Objective', y='CPC', data=all_data)
#sns.barplot(x='Result_Type', y='CPC', data=all_data)

#sns.barplot(x='Objective', y='CTR', data=all_data)
#sns.barplot(x='Objective', y='Total_Users', data=all_data)
#sns.barplot(x='Objective', y='Total_Users', data=all_data)
#sns.barplot(x='Result_Type', y='Total_Users', data=all_data)

#sns.barplot(x='Objective', y='Total_Click_To_Retail', data=all_data)
#sns.barplot(x='Result_Type', y='Total_Click_To_Retail', data=all_data)

#sns.barplot(x='Objective', y='Cost_Per_User', data=all_data)
#sns.barplot(x='Objective', y='Cost_Per_Click_To_Retail', data=all_data)


#all_data_corr = all_data.corr()
#sns.heatmap(all_data_corr, annot=True)
#sns.lmplot(x='Spend', y='Clicks', data=all_data)
#sns.lmplot(x='Spend', y='Reach', data=all_data)
#sns.lmplot(x='Spend', y='CPC', data=all_data)
#sns.pairplot(all_data)

#plt.show()