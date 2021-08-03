from matplotlib.colors import Normalize
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches
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
#sns.set_context('talk', font_scale=.5)

#merging social data and google data
all_data = pd.concat([social_merged, google_merged])

#misc cleaning - drop duplicates, drop unnamed col, change date cols to date time
all_data.drop_duplicates(subset='Campaign_Name', keep='last', inplace=True)
all_data.drop(columns='Unnamed: 0', inplace=True)

date_cols = [column for column in all_data.columns if re.match('.*Date', column)]
for name in date_cols:
  all_data[name] = pd.to_datetime(all_data[name])

"""
#getting total campaigns, total books, total spend, total clicks, total impressions, and total audiences
print(all_data.describe()) #campaign total and stats info
print(all_data.Spend.sum()) #total spend
print(all_data.Clicks.sum()) #total clicks
print(all_data.Reach.sum()) #total reach
print(all_data.Audience.nunique()) #total unique audiences
"""

#setting up series for Placements for Graphs
all_data['Placements_For_Chart'] = all_data.Placements
all_data['Placements_For_Chart'] = all_data.Placements_For_Chart.str.replace('Pin Feed', 'Pinterest')
all_data['Placements_For_Chart'] = all_data.Placements_For_Chart.str.replace('IG\s.+', 'Instagram', regex=True)
all_data.Placements_For_Chart.fillna('Pinterest', inplace=True) #fixes missing value for Helena Hunting
all_data.loc[all_data.Placements_For_Chart.str.contains('FB\s.+Instagram'), 'Placements_For_Chart'] = 'Facebook/Instagram'
all_data['Placements_For_Chart'] = all_data.Placements_For_Chart.str.replace('FB\s.+', 'Facebook', regex=True)

"""
#breakdown of Placements
print(all_data.Placements_For_Chart.value_counts()) #for totals of Placements
print(all_data.Placements_For_Chart.value_counts(normalize=True)) #for % totals of Placements

#chart for Placements
platform_df = pd.DataFrame(all_data.Placements_For_Chart.value_counts(normalize=True).sort_values(ascending=False)).mul(100).reset_index().rename(columns={'index': 'Platform', 'Placements_For_Chart': 'Percentage'})
Platform_Chart = sns.catplot(x='Platform', y='Percentage', data=platform_df, kind='bar', palette='cool')
Platform_Chart.set(title='Percent of Ads by Social Media Platform')
Platform_Chart.set_xlabels(fontsize=11)
Platform_Chart.set_ylabels(fontsize=11)
Platform_Chart.ax.set_ylim(0,100)
for p in Platform_Chart.ax.patches:
  Platform_Chart.ax.annotate(str(p.get_height().round(2)) + '%',
  (p.get_x() + p.get_width()/2., p.get_height()),
  ha='center', va='center',
  xytext=(0,5),
  textcoords='offset points')

#breakdown by Objective
print(all_data.Objective.value_counts())
print(all_data.Objective.value_counts(normalize=True))

#breakdown of Traffic
print(all_data.loc[all_data.Objective == 'Traffic', 'Result_Type'].value_counts())
print(all_data.loc[all_data.Objective == 'Traffic', 'Result_Type'].value_counts(normalize=True))

#chart for Objective
#objective_df = pd.DataFrame(all_data.loc[:, ['Objective', 'Result_Type']].value_counts(normalize=True).sort_values(ascending=False)).mul(100).reset_index().rename(columns={0: 'Percentage'})
#Objective_Chart = objective_df.set_index(['Objective', 'Result_Type'])['Percentage'].unstack().plot.bar(stacked=True)
objective_df = pd.DataFrame(all_data.Objective.value_counts(normalize=True).sort_values(ascending=False)).mul(100).reset_index().rename(columns={'index': 'Objective', 'Objective': "Percentage"})
Objective_Chart = sns.catplot(x='Objective', y='Percentage', data=objective_df, kind='bar', palette='cool')
Objective_Chart.set(title='Percent of Ads by Objective')
Objective_Chart.set_xlabels(fontsize=11)
Objective_Chart.set_ylabels(fontsize=11)
Objective_Chart.ax.set_ylim(0,100)
for p in Objective_Chart.ax.patches:
  Objective_Chart.ax.annotate(str(p.get_height().round(2)) + '%',
  (p.get_x() + p.get_width()/2, p.get_height()),
  ha='center', va='center',
  xytext=(0,5),
  textcoords='offset points')
plt.text(1, 60, '''Traffic Breakdown:
Link Clicks: 48.21%
Landing Page Views: 30.26%
Clicks: 21.54%
''', fontsize=8.5, bbox={'fc': 'white', 'boxstyle': 'larrow'})

#chart for correlation heatmap
all_data_corr = all_data.corr()
Corr_Heat_Map = sns.heatmap(all_data_corr, annot=True, cmap='Blues', linewidths=.5)
Corr_Heat_Map.set_title('Correlations in Social Media Ads')


#charts for spend vs x
#ci=None will remove the confidence interval
spend_vs_reach = sns.lmplot(x='Spend', y='Reach', data=all_data)
spend_vs_clicks = sns.lmplot(x='Spend', y='Clicks', data=all_data)
spend_vs_total_users = sns.lmplot(x='Spend', y='Total_Users', data=all_data)
spend_vs_total_click_to_retail = sns.lmplot(x='Spend', y='Total_Click_To_Retail', data=all_data)
spend_vs_cost_per_click_to_retail = sns.lmplot(x='Spend', y='Cost_Per_Click_To_Retail', data=all_data)

#to rename the charts and y label - SEE FOR LOOP THAT RENAMES ALL OF THESE
list_of_graphs = [spend_vs_reach, spend_vs_total_users, spend_vs_clicks, spend_vs_cost_per_click_to_retail, spend_vs_total_click_to_retail]


#charts for reach vs x
reach_vs_clicks = sns.lmplot(x='Reach', y='Clicks', data=all_data)
reach_vs_cpm = sns.lmplot(x='Reach', y='CPM', data=all_data)
reach_vs_ctr = sns.lmplot(x='Reach', y='CTR', data=all_data)
reach_vs_total_users = sns.lmplot(x='Reach', y='Total_Users', data=all_data)
reach_vs_total_click_to_retail = sns.lmplot(x='Reach', y='Total_Click_To_Retail', data=all_data)

#to rename the charts and y label - SEE FOR LOOP THAT RENAMES ALL OF THESE
list_of_graphs = [reach_vs_clicks, reach_vs_cpm, reach_vs_ctr, reach_vs_total_users, reach_vs_total_click_to_retail]


#charts for clicks vs x
clicks_vs_ctr = sns.lmplot(x='Clicks', y='CTR', data=all_data)
clicks_vs_total_users = sns.lmplot(x='Clicks', y='Total_Users', data=all_data)
clicks_vs_total_click_to_retail = sns.lmplot(x='Clicks', y='Total_Click_To_Retail', data=all_data)

#to rename the charts and y label - SEE FOR LOOP THAT RENAMES ALL OF THESE
list_of_graphs = [clicks_vs_ctr, clicks_vs_total_users, clicks_vs_total_click_to_retail]


#charts for cpm vs x
cpm_vs_ctr = sns.lmplot(x='CPM', y='CTR', data=all_data)
cpm_vs_total_users = sns.lmplot(x='CPM', y='Total_Users', data=all_data) #don't include
cpm_vs_total_click_to_retail = sns.lmplot(x='CPM', y='Total_Click_To_Retail', data=all_data) #don't include

#to rename the charts and y label - SEE FOR LOOP THAT RENAMES ALL OF THESE
list_of_graphs = [cpm_vs_ctr, cpm_vs_total_users, cpm_vs_total_click_to_retail]


#charts for ctr vs x
ctr_vs_total_users = sns.lmplot(x='CTR', y='Total_Users', data=all_data)
ctr_vs_total_click_to_retail = sns.lmplot(x='CTR', y='Total_Click_To_Retail', data=all_data)

#to rename the charts and y label - SEE FOR LOOP THAT RENAMES ALL OF THESE
list_of_graphs = [ctr_vs_total_users, ctr_vs_total_click_to_retail]


#charts for users vs x
users_vs_cost_per_user = sns.lmplot(x='Total_Users', y='Cost_Per_User', data=all_data)
users_vs_total_click_to_retail = sns.lmplot(x='Total_Users', y='Total_Click_To_Retail', data=all_data)

#to rename the charts and y label - SEE FOR LOOP THAT RENAMES ALL OF THESE
list_of_graphs = [users_vs_cost_per_user, users_vs_total_click_to_retail]


#charts for cost per user vs x
cost_per_user_vs_cost_per_click_to_retail = sns.lmplot(x='Cost_Per_User', y='Cost_Per_Click_To_Retail', data=all_data)

#to rename the charts and y label - SEE FOR LOOP THAT RENAMES ALL OF THESE
list_of_graphs = [cost_per_user_vs_cost_per_click_to_retail]

#for loop that renames all of these
for graph in list_of_graphs:
  y_label = str(graph.ax.get_ylabel).split()
  y_label = y_label[5].replace('ylabel=','').replace('>>', '').strip().replace('_', ' ').replace('\'', '')
  graph.set_ylabels(y_label)
  y_axis = str(graph.ax.get_ylabel).split()
  y_axis = ' '.join(y_axis[5:]).replace('ylabel=','').replace('>>', '').replace('\'', '')
  x_axis = str(graph.ax.get_xlabel).split()
  x_axis = ' '.join(x_axis[4])
  x_axis = re.sub('.+=|\'|,|\s', '', x_axis).replace('_', ' ')
  graph.set_xlabels(x_axis)
  graph.set(title=(str(x_axis) + ' vs ' + str(y_axis)))
  #max_y_value = all_data[str(y_axis).replace(' ', '_')].max()
  #print(max_y_value)
  #graph.ax.set_xlim(auto=True)
"""

#chart for result type vs users/click to retail
#creating df
result_type_df = pd.DataFrame(all_data.loc[:, ['Result_Type', 'Total_Users', 'Clicks', 'Total_Click_To_Retail', 'CPC', 'Reach', 'CPM', 'CTR', 'Cost_Per_User', 'Cost_Per_Click_To_Retail']])
result_type_df = result_type_df.groupby('Result_Type').sum()
result_type_df['Percent'] = result_type_df.Total_Users / result_type_df.Clicks
result_type_df.reset_index(inplace=True)
result_type_df.Percent.fillna(0, inplace=True)
result_type_df.sort_values('Total_Users', ascending=False, inplace=True)

"""
#creating user graph
result_type_user_graph = sns.barplot(x='Result_Type', y='Total_Users', data=result_type_df, palette='cool')
result_type_user_graph.set(title='Total Users By Result Type')
result_type_user_graph.axes.set_xlabel('Result Type', fontsize=11)
result_type_user_graph.axes.set_ylabel('Total Users', fontsize=11)


#creating result graph
result_type_retail_graph = sns.barplot(x='Result_Type', y='Total_Click_To_Retail', data=result_type_df, palette='cool')
result_type_retail_graph.set(title='Total Clicks To Retail By Result Type')
result_type_retail_graph.axes.set_xlabel('Result Type', fontsize=11)
result_type_retail_graph.axes.set_ylabel('Total Clicks To Retail', fontsize=11)


#creating clicks graph
result_type_df.sort_values('Clicks', inplace=True, ascending=False)
result_type_click_graph = sns.barplot(x='Result_Type', y='Clicks', data=result_type_df, palette='cool')
result_type_click_graph.set(title='Clicks By Result Type')
result_type_click_graph.axes.set_xlabel('Result Type', fontsize=11)
result_type_click_graph.axes.set_ylabel('Clicks', fontsize=11)

#creating reach graph
result_type_df.sort_values('Reach', inplace=True, ascending=False)
result_type_reach_graph = sns.barplot(x='Result_Type', y='Reach', data=result_type_df, palette='cool')
result_type_reach_graph.set(title='Reach By Result Type')
result_type_reach_graph.axes.set_xlabel('Result Type', fontsize=11)
result_type_reach_graph.axes.set_ylabel('Reach', fontsize=11)
"""
print(result_type_df)

#sns.barplot(x='Result_Type', y='Clicks', data=result_type_df, palette='cool')

#splitting Objectives
traffic = all_data.loc[all_data.Objective == 'Traffic', :]
conversions = all_data.loc[all_data.Objective == 'Conversions', :]
engagement = all_data.loc[all_data.Objective == 'Engagement', :]
reach = all_data.loc[all_data.Objective == 'Reach', :]
page_likes = all_data.loc[all_data.Objective == 'Page Likes', :]
video_views = all_data.loc[all_data.Objective == 'Video Views', :]


#print(traffic.loc[traffic.Result_Type == 'Impressions'])

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


#sns.lmplot(x='Spend', y='Clicks', data=all_data)
#sns.lmplot(x='Spend', y='Reach', data=all_data)
#sns.lmplot(x='Spend', y='CPC', data=all_data)
#sns.pairplot(all_data)

plt.show()