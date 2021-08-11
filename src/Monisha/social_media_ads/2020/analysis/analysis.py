from matplotlib.colors import Normalize
from numpy.lib.function_base import average
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches
import os
import toml
import src.utils as u
import re
import numpy as np

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
#Platform_Chart.ax.set_ylim(0,100)
for p in Platform_Chart.ax.patches:
  Platform_Chart.ax.annotate(str(p.get_height().round(2)) + '%',
  (p.get_x() + p.get_width()/2., p.get_height()),
  ha='center', va='center',
  xytext=(0,5),
  textcoords='offset points')
Platform_Chart.set_xticklabels(rotation=25, horizontalalignment='right')
vals = Platform_Chart.ax.get_yticks()
Platform_Chart.set_yticklabels(['{}%'.format(x) for x in vals])

#plt.savefig('chart_for_platforms.png', bbox_inches='tight')

"""

"""
#breakdown by Objective
print(all_data.Objective.value_counts())
print(all_data.Objective.value_counts(normalize=True))

#breakdown of Traffic
print(all_data.loc[all_data.Objective == 'Traffic', 'Result_Type'].value_counts())
print(all_data.loc[all_data.Objective == 'Traffic', 'Result_Type'].value_counts(normalize=True))

#chart for Objective
objective_df = pd.DataFrame(all_data.Objective.value_counts(normalize=True).sort_values(ascending=False)).mul(100).reset_index().rename(columns={'index': 'Objective', 'Objective': "Percentage"})
Objective_Chart = sns.catplot(x='Objective', y='Percentage', data=objective_df, kind='bar', palette='cool')
Objective_Chart.set(title='Percent of Ads by Objective')
Objective_Chart.set_xlabels(fontsize=11)
Objective_Chart.set_ylabels(fontsize=11)
#Objective_Chart.ax.set_ylim(0,100)
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
Objective_Chart.set_xticklabels(rotation=25, horizontalalignment='right')
vals = Objective_Chart.ax.get_yticks()
Objective_Chart.set_yticklabels(['{}%'.format(x) for x in vals])

plt.savefig('chart_for_objectives.png', bbox_inches='tight')

#chart for correlation heatmap
all_data_corr = all_data.corr()
plt.figure(figsize=(12,9))
Corr_Heat_Map = sns.heatmap(all_data_corr, annot=True, cmap='YlOrRd', linewidths=.5)
Corr_Heat_Map.set_title('Correlations in Social Media Ads')
plt.xticks(rotation=40, horizontalalignment='right')
plt.savefig('chart_for_correlation.png', bbox_inches='tight')
"""


#charts for spend vs x
#as a def
def rename_save(graph):
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
  #saves the fig, commented out for now - DOESN'T WORK
  for_naming_x = x_axis.lower().replace(' ', '_')
  for_naming_y = y_label.lower().replace(' ', '_')
  my_file = for_naming_x + '_vs_' + for_naming_y + '.png'
  plt.savefig(my_file, bbox_inches='tight')

#ci=None will remove the confidence interval
spend_vs_reach = sns.lmplot(x='Spend', y='Reach', data=all_data, line_kws={'color': 'orange'}, scatter_kws={'color': '#CC0000'})
rename_save(spend_vs_reach)  
spend_vs_clicks = sns.lmplot(x='Spend', y='Clicks', data=all_data, line_kws={'color': 'orange'}, scatter_kws={'color': '#CC0000'})
rename_save(spend_vs_clicks)
spend_vs_total_users = sns.lmplot(x='Spend', y='Total_Users', data=all_data, line_kws={'color': 'orange'}, scatter_kws={'color': '#CC0000'})
rename_save(spend_vs_total_users)
spend_vs_total_click_to_retail = sns.lmplot(x='Spend', y='Total_Click_To_Retail', data=all_data, line_kws={'color': 'orange'}, scatter_kws={'color': '#CC0000'})
rename_save(spend_vs_total_click_to_retail)
spend_vs_cost_per_click_to_retail = sns.lmplot(x='Spend', y='Cost_Per_Click_To_Retail', data=all_data, line_kws={'color': 'orange'}, scatter_kws={'color': '#CC0000'})

#to rename the charts and y label - SEE FOR LOOP THAT RENAMES ALL OF THESE
#list_of_graphs = [spend_vs_reach, spend_vs_total_users, spend_vs_clicks, spend_vs_cost_per_click_to_retail, spend_vs_total_click_to_retail]

#charts for reach vs x
reach_vs_clicks = sns.lmplot(x='Reach', y='Clicks', data=all_data)
reach_vs_cpm = sns.lmplot(x='Reach', y='CPM', data=all_data)
reach_vs_ctr = sns.lmplot(x='Reach', y='CTR', data=all_data)
reach_vs_total_users = sns.lmplot(x='Reach', y='Total_Users', data=all_data, line_kws={'color': 'orange'}, scatter_kws={'color': '#CC0000'})
rename_save(reach_vs_total_users)
reach_vs_total_click_to_retail = sns.lmplot(x='Reach', y='Total_Click_To_Retail', data=all_data)

#to rename the charts and y label - SEE FOR LOOP THAT RENAMES ALL OF THESE
list_of_graphs = [reach_vs_clicks, reach_vs_cpm, reach_vs_ctr, reach_vs_total_users, reach_vs_total_click_to_retail]


#charts for clicks vs x
clicks_vs_ctr = sns.lmplot(x='Clicks', y='CTR', data=all_data)
clicks_vs_total_users = sns.lmplot(x='Clicks', y='Total_Users', data=all_data, line_kws={'color': 'orange'}, scatter_kws={'color': '#CC0000'})
rename_save(clicks_vs_total_users)
clicks_vs_total_click_to_retail = sns.lmplot(x='Clicks', y='Total_Click_To_Retail', data=all_data, line_kws={'color': 'orange'}, scatter_kws={'color': '#CC0000'})
rename_save(clicks_vs_total_click_to_retail)

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
users_vs_total_click_to_retail = sns.lmplot(x='Total_Users', y='Total_Click_To_Retail', data=all_data, line_kws={'color': 'orange'}, scatter_kws={'color': '#CC0000'})
rename_save(users_vs_total_click_to_retail)

#to rename the charts and y label - SEE FOR LOOP THAT RENAMES ALL OF THESE
list_of_graphs = [users_vs_cost_per_user, users_vs_total_click_to_retail]


#charts for cost per user vs x
cost_per_user_vs_cost_per_click_to_retail = sns.lmplot(x='Cost_Per_User', y='Cost_Per_Click_To_Retail', data=all_data)

#to rename the charts and y label - SEE FOR LOOP THAT RENAMES ALL OF THESE
list_of_graphs = [cost_per_user_vs_cost_per_click_to_retail]

"""
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
  #saves the fig, commented out for now - DOESN'T WORK
  for_naming_x = x_axis.lower().replace(' ', '_')
  for_naming_y = y_label.lower().replace(' ', '_')
  my_file = for_naming_x + '_vs_' + for_naming_y + '.png'
  plt.savefig(my_file, bbox_inches='tight')
"""

"""
"""

#chart for result type vs x
#creating df
result_type_df = pd.DataFrame(all_data.loc[:, ['Result_Type', 'Spend', 'Total_Users', 'Clicks', 'Total_Click_To_Retail', 'Reach']])
result_type_df = result_type_df.groupby('Result_Type').sum()
result_type_df['CPM'] = (result_type_df['Spend'] / result_type_df['Reach']) * 1000
result_type_df['CPC'] = result_type_df['Spend'] / result_type_df['Clicks']
result_type_df['CTR'] = (result_type_df['Clicks'] / result_type_df['Reach'])
result_type_df['Cost_Per_User'] = (result_type_df['Spend'] / result_type_df['Total_Users'])
result_type_df['Cost_Per_Click_To_Retail'] = (result_type_df['Spend'] / result_type_df['Total_Click_To_Retail'])
result_type_df['Click_To_Retail_Rate'] = (result_type_df['Total_Click_To_Retail'] / result_type_df['Total_Users'])
result_type_df.CPC.replace([np.inf, -np.inf], np.nan, inplace=True)
result_type_df.Cost_Per_User.replace([np.inf, -np.inf], np.nan, inplace=True)
result_type_df.Cost_Per_Click_To_Retail.replace([np.inf, -np.inf], np.nan, inplace=True)
result_type_df.CTR.replace(0.000000, np.nan, inplace=True)
result_type_df.reset_index(inplace=True)
result_type_df.sort_values('Total_Users', ascending=False, inplace=True)

"""
#creating user graph
result_type_user_graph = sns.barplot(x='Result_Type', y='Total_Users', data=result_type_df, palette='cool')
result_type_user_graph.set(title='Total Users By Result Type')
result_type_user_graph.axes.set_xlabel('Result Type', fontsize=11)
result_type_user_graph.axes.set_ylabel('Total Users', fontsize=11)
plt.xticks(rotation=25, horizontalalignment='right')
plt.savefig('result_type_vs_user_chart', bbox_inches='tight')

#creating retail graph
result_type_retail_graph = sns.barplot(x='Result_Type', y='Total_Click_To_Retail', data=result_type_df, palette='cool')
result_type_retail_graph.set(title='Total Clicks To Retail By Result Type')
result_type_retail_graph.axes.set_xlabel('Result Type', fontsize=11)
result_type_retail_graph.axes.set_ylabel('Total Clicks To Retail', fontsize=11)
plt.xticks(rotation=25, horizontalalignment='right')
plt.savefig('result_type_vs_clicks_to_retail', bbox_inches='tight')

#creating clicks graph
result_type_df.sort_values('Clicks', inplace=True, ascending=False)
result_type_click_graph = sns.barplot(x='Result_Type', y='Clicks', data=result_type_df, palette='cool')
result_type_click_graph.set(title='Clicks By Result Type')
result_type_click_graph.axes.set_xlabel('Result Type', fontsize=11)
result_type_click_graph.axes.set_ylabel('Clicks', fontsize=11)
plt.xticks(rotation=25, horizontalalignment='right')
plt.savefig('result_type_vs_clicks', bbox_inches='tight')

#creating reach graph
result_type_df.sort_values('Reach', inplace=True, ascending=False)
result_type_reach_graph = sns.barplot(x='Result_Type', y='Reach', data=result_type_df, palette='cool')
result_type_reach_graph.set(title='Reach By Result Type')
result_type_reach_graph.axes.set_xlabel('Result Type', fontsize=11)
result_type_reach_graph.axes.set_ylabel('Reach', fontsize=11)
plt.xticks(rotation=25, horizontalalignment='right')
plt.savefig('result_type_vs_reach', bbox_inches='tight')

#creating ctr graph
result_type_df.sort_values('CTR', inplace=True, ascending=False)
result_type_ctr_graph = sns.barplot(x='Result_Type', y='CTR', data=result_type_df, palette='cool')
result_type_ctr_graph.set(title='CTR By Result Type')
result_type_ctr_graph.axes.set_xlabel('Result Type', fontsize=11)
result_type_ctr_graph.axes.set_ylabel('CTR', fontsize=11)
vals = result_type_ctr_graph.get_yticks()
result_type_ctr_graph.set_yticklabels(['{:,.2%}'.format(x) for x in vals])
plt.xticks(rotation=25, horizontalalignment='right')
for p in result_type_ctr_graph.patches:
  result_type_ctr_graph.annotate(str((p.get_height() * 100).round(2)) + '%',
  (p.get_x() + p.get_width()/2., p.get_height()),
  ha='center', va='center',
  xytext=(0,5),
  textcoords='offset points')
plt.savefig('result_type_vs_ctr', bbox_inches='tight')

#creating cpc graph
result_type_df.sort_values('CPC', inplace=True, ascending=False)
result_type_cpc_graph = sns.barplot(x='Result_Type', y='CPC', data=result_type_df, palette='cool')
result_type_cpc_graph.set(title='CPC By Result Type')
result_type_cpc_graph.axes.set_xlabel('Result Type', fontsize=11)
result_type_cpc_graph.axes.set_ylabel('CPC ($)', fontsize=11)
plt.xticks(rotation=25, horizontalalignment='right')
for p in result_type_cpc_graph.patches:
  result_type_cpc_graph.annotate('$' + str(p.get_height().round(2)),
  (p.get_x() + p.get_width()/2., p.get_height()),
  ha='center', va='center',
  xytext=(0,5),
  textcoords='offset points')
plt.savefig('result_type_vs_cpc', bbox_inches='tight')

#creating cpm graph
result_type_df.sort_values('CPM', inplace=True, ascending=False)
result_type_cpm_graph = sns.barplot(x='Result_Type', y='CPM', data=result_type_df, palette='cool')
result_type_cpm_graph.set(title='CPM By Result Type')
result_type_cpm_graph.axes.set_xlabel('Result Type', fontsize=11)
result_type_cpm_graph.axes.set_ylabel('CPM ($)', fontsize=11)
plt.xticks(rotation=25, horizontalalignment='right')
plt.savefig('result_type_vs_cpm', bbox_inches='tight')
for p in result_type_cpm_graph.patches:
  result_type_cpm_graph.annotate('$' + str(p.get_height().round(2)),
  (p.get_x() + p.get_width()/2., p.get_height()),
  ha='center', va='center',
  xytext=(0,5),
  textcoords='offset points')
plt.savefig('result_type_vs_cpm', bbox_inches='tight')

#creating cost per user graph
result_type_df.sort_values('Cost_Per_User', inplace=True, ascending=False)
result_type_cost_per_user_graph = sns.barplot(x='Result_Type', y='Cost_Per_User', data=result_type_df, palette='cool')
result_type_cost_per_user_graph.set(title='Cost Per User By Result Type')
result_type_cost_per_user_graph.axes.set_xlabel('Result Type', fontsize=11)
result_type_cost_per_user_graph.axes.set_ylabel('Cost Per User ($)', fontsize=11)
plt.xticks(rotation=25, horizontalalignment='right')
for p in result_type_cost_per_user_graph.patches:
  result_type_cost_per_user_graph.annotate('$' + str(p.get_height().round(2)),
  (p.get_x() + p.get_width()/2., p.get_height()),
  ha='center', va='center',
  xytext=(0,5),
  textcoords='offset points')
plt.savefig('result_type_vs_cost_per_user', bbox_inches='tight')


#creating cost per click to retail graph
result_type_df.sort_values('Cost_Per_Click_To_Retail', inplace=True, ascending=False)
result_type_cost_per_retail_graph = sns.barplot(x='Result_Type', y='Cost_Per_Click_To_Retail', data=result_type_df, palette='cool')
result_type_cost_per_retail_graph.set(title='Cost Per Click To Retail By Result Type')
result_type_cost_per_retail_graph.axes.set_xlabel('Result Type', fontsize=11)
result_type_cost_per_retail_graph.axes.set_ylabel('Cost Per Click To Retail ($)', fontsize=11)
plt.xticks(rotation=25, horizontalalignment='right')
for p in result_type_cost_per_retail_graph.patches:
  result_type_cost_per_retail_graph.annotate('$' + str(p.get_height().round(2)),
  (p.get_x() + p.get_width()/2., p.get_height()),
  ha='center', va='center',
  xytext=(0,5),
  textcoords='offset points')
plt.savefig('result_type_vs_cost_per_retail_click', bbox_inches='tight')

#creating click to retail rate graph
result_type_df.sort_values('Click_To_Retail_Rate', inplace=True, ascending=False)
result_type_cost_per_retail_graph = sns.barplot(x='Result_Type', y='Click_To_Retail_Rate', data=result_type_df, palette='cool')
result_type_cost_per_retail_graph.set(title='Click To Retail Rate By Result Type')
result_type_cost_per_retail_graph.axes.set_xlabel('Result Type', fontsize=11)
result_type_cost_per_retail_graph.axes.set_ylabel('Click To Retail Rate', fontsize=11)
vals = result_type_cost_per_retail_graph.get_yticks()
result_type_cost_per_retail_graph.set_yticklabels(['{:,.2%}'.format(x) for x in vals])
plt.xticks(rotation=25, horizontalalignment='right')
for p in result_type_cost_per_retail_graph.patches:
  result_type_cost_per_retail_graph.annotate(str((p.get_height() * 100).round(2)) + '%',
  (p.get_x() + p.get_width()/2., p.get_height()),
  ha='center', va='center',
  xytext=(0,5),
  textcoords='offset points')

plt.savefig('result_type_vs_retail_click_rate', bbox_inches='tight')

"""

#creating keywords df
keywords_df = pd.DataFrame(all_data.loc[:, ['Spend', 'Audience', 'Reach', 'Clicks', 'Total_Users', 'Total_Click_To_Retail']])
keywords_df['Audience'] = keywords_df.Audience.str.title()
keywords_df['Audience'] = keywords_df.Audience.str.split(' - ', expand=True)
keywords_df['Audience'] = keywords_df.Audience.str.replace('\s+\(Just\s.*Keyword;\sAll\sAges\)', ' Keyword', regex=True).str.replace(' Based', '').str.replace('Snowfall\sAudience\s.+', 'Snowfall Audience', regex=True)
keywords_df['Audience'] = keywords_df.Audience.str.replace('N/A', 'Misc Pinterest').str.replace('.+Pinterest', 'Misc Pinterest')
keywords_df = keywords_df.groupby('Audience').sum()
keywords_df['CPM'] = (keywords_df['Spend'] / keywords_df['Reach']) * 1000
keywords_df['CPC'] = keywords_df['Spend'] / keywords_df['Clicks']
keywords_df['CTR'] = keywords_df['Clicks'] / keywords_df['Reach']
keywords_df['Cost_Per_User'] = keywords_df['Spend'] / keywords_df['Total_Users']
keywords_df['Cost_Per_Click_To_Retail'] = keywords_df['Spend'] / keywords_df['Total_Click_To_Retail']
keywords_df['Click_To_Retail_Rate'] = keywords_df['Total_Click_To_Retail'] / keywords_df['Total_Users']
keywords_df.replace([np.inf, -np.inf], np.nan, inplace=True)
keywords_df.drop(keywords_df.loc[keywords_df.index.str.contains('Christina-Britton'), :].index, inplace=True)

for_nan = ['Clicks', 'Total_Users', 'Total_Click_To_Retail', 'Reach', 'CTR']
for value in for_nan:
  keywords_df[value] = keywords_df[value].replace(0, np.nan)
  keywords_df[value] = keywords_df[value].replace(0.000000, np.nan)

"""
#creates and saves graphs for cpm, cpc, cost_per_user, cost_per_click_to_retail
cols_for_graphs = ['CPM', 'CPC', 'Cost_Per_User', 'Cost_Per_Click_To_Retail']
for col in cols_for_graphs:
  keywords_df.sort_values(col, inplace=True)
  keywords_df_head = keywords_df.head(10)
  barplot = sns.catplot(x=keywords_df_head.index, y=col, data=keywords_df_head, kind='bar', palette='cool', ci=None)
  y_label = str(barplot.ax.get_ylabel).split()
  y_label = y_label[5].replace('ylabel=','').replace('>>', '').strip().replace('_', ' ').replace('\'', '')
  barplot.set_ylabels(y_label + ' ($)')
  y_axis = str(barplot.ax.get_ylabel).split()
  y_axis = ' '.join(y_axis[5:]).replace('ylabel=','').replace('>>', '').replace('\'', '')
  x_axis = str(barplot.ax.get_xlabel).split()
  x_axis = ' '.join(x_axis[4])
  x_axis = re.sub('.+=|\'|,|\s', '', x_axis).replace('_', ' ')
  barplot.set_xlabels(x_axis)
  y_for_title = y_label.replace(' ($)', '')
  barplot.set(title=(str(y_for_title) + ' by ' + str(x_axis)))
  barplot.set_xticklabels(rotation=45, horizontalalignment='right', fontsize='x-small')
  #left_lim, right_lim = plt.ylim()
  #mean_value = keywords_df_head[col].mean()
  #right_lim = right_lim - mean_value
  #min_value = keywords_df_head[col].min().round(2)
  #min_name = keywords_df_head[col].idxmin()
  #plt.text(left_lim, right_lim, r'''Lowest {}:
  #{} (${})'''.format(y_for_title, min_name, min_value), fontsize=8, bbox={'fc': 'white'})
  for p in barplot.ax.patches:
    barplot.ax.annotate('$' + str(p.get_height().round(2)),
  (p.get_x() + p.get_width()/2., p.get_height()),
  ha='center', va='center',
  xytext=(0,5),
  textcoords='offset points',
  fontsize=8)
  #saves the fig, commented out for now - DOES WORK
  my_file = 'keywords_df_' + col + '.png'
  plt.savefig(my_file, bbox_inches='tight')

#creates and saves graphs for ctr, click_to_retail_rate
cols_for_rate_graphs = ['CTR', 'Click_To_Retail_Rate']
for col in cols_for_rate_graphs:
  keywords_df.sort_values(col, ascending=False, inplace=True)
  keywords_df_head = keywords_df.head(10)
  barplot = sns.catplot(x=keywords_df_head.index, y=col, data=keywords_df_head, kind='bar', palette='cool', ci=None)
  y_label = str(barplot.ax.get_ylabel).split()
  y_label = y_label[5].replace('ylabel=','').replace('>>', '').strip().replace('_', ' ').replace('\'', '')
  barplot.set_ylabels(y_label)
  y_axis = str(barplot.ax.get_ylabel).split()
  y_axis = ' '.join(y_axis[5:]).replace('ylabel=','').replace('>>', '').replace('\'', '')
  x_axis = str(barplot.ax.get_xlabel).split()
  x_axis = ' '.join(x_axis[4])
  x_axis = re.sub('.+=|\'|,|\s', '', x_axis).replace('_', ' ')
  barplot.set_xlabels(x_axis)
  barplot.set(title=(str(y_axis) + ' by ' + str(x_axis)))
  barplot.set_xticklabels(rotation=45, horizontalalignment='right', fontsize='x-small')
  vals = barplot.ax.get_yticks()
  barplot.set_yticklabels(['{:,.2%}'.format(x) for x in vals])
  #left_lim, right_lim = plt.ylim()
  #mean_value = keywords_df_head[col].std()
  #right_lim = right_lim - mean_value
  #left_lim = left_lim + 4.5
  #max_value = keywords_df_head[col].max().round(4) * 100
  #max_name = keywords_df_head[col].idxmax()
  #plt.text(left_lim, right_lim, r'''Highest {}:
  #{} ({}%)'''.format(y_axis, max_name, max_value), fontsize=8, bbox={'fc': 'white'})
  for p in barplot.ax.patches:
    barplot.ax.annotate(str((p.get_height() * 100).round(2)) + '%',
  (p.get_x() + p.get_width()/2., p.get_height()),
  ha='center', va='center',
  xytext=(0,5),
  textcoords='offset points',
  fontsize=7.5)
  #saves the fig, commented out for now - DOES WORK
  my_file = 'keywords_df_' + col + '.png'
  plt.savefig(my_file, bbox_inches='tight')

"""
#creating authors df
authors_df = pd.DataFrame(all_data.loc[:, ['Author', 'Spend', 'Reach', 'Clicks', 'Total_Users', 'Total_Click_To_Retail']])
authors_df = authors_df.groupby('Author').sum()
authors_df['CPM'] = (authors_df['Spend'] / authors_df['Reach']) * 1000
authors_df['CPC'] = authors_df['Spend'] / authors_df['Clicks']
authors_df['CTR'] = authors_df['Clicks'] / authors_df['Reach']
authors_df['Cost_Per_User'] = authors_df['Spend'] / authors_df['Total_Users']
authors_df['Cost_Per_Click_To_Retail'] = authors_df['Spend'] / authors_df['Total_Click_To_Retail']
authors_df['Click_To_Retail_Rate'] = authors_df['Total_Click_To_Retail'] / authors_df['Total_Users']
authors_df.replace([np.inf, -np.inf], np.nan, inplace=True)

for_nan = ['Clicks', 'Total_Users', 'Total_Click_To_Retail', 'Reach', 'CTR']
for value in for_nan:
  authors_df[value] = authors_df[value].replace(0, np.nan)
  authors_df[value] = authors_df[value].replace(0.000000, np.nan)

"""
#creates and saves graphs for cpm, cpc, cost_per_user, cost_per_click_to_retail
cols_for_graphs = ['CPM', 'CPC', 'Cost_Per_User', 'Cost_Per_Click_To_Retail']
for col in cols_for_graphs:
  authors_df.sort_values(col, inplace=True)
  authors_df_head = authors_df.head(5)
  barplot = sns.catplot(x=authors_df_head.index, y=col, data=authors_df_head, kind='bar', palette='cool', ci=None)
  y_label = str(barplot.ax.get_ylabel).split()
  y_label = y_label[5].replace('ylabel=','').replace('>>', '').strip().replace('_', ' ').replace('\'', '')
  barplot.set_ylabels(y_label)
  y_axis = str(barplot.ax.get_ylabel).split()
  y_axis = ' '.join(y_axis[5:]).replace('ylabel=','').replace('>>', '').replace('\'', '')
  x_axis = str(barplot.ax.get_xlabel).split()
  x_axis = ' '.join(x_axis[4])
  x_axis = re.sub('.+=|\'|,|\s', '', x_axis).replace('_', ' ')
  barplot.set_xlabels(x_axis)
  y_for_title = y_label.replace(' ($)', '')
  barplot.set(title=(str(y_for_title) + ' by ' + str(x_axis)))
  barplot.set_xticklabels(rotation=45, horizontalalignment='right', fontsize='x-small')
  #left_lim, right_lim = plt.ylim()
  #mean_value = authors_df_head[col].mean()
  #std_value = authors_df_head[col].std()
  #right_lim = right_lim - mean_value + std_value
  #min_value = authors_df_head[col].min().round(2)
  #min_name = authors_df_head[col].idxmin()
  #plt.text(left_lim, right_lim, r'''Lowest {}:
  #{} (${})'''.format(y_for_title, min_name, min_value), fontsize=8, bbox={'fc': 'white'})
  for p in barplot.ax.patches:
    barplot.ax.annotate('$' + str(p.get_height().round(2)),
  (p.get_x() + p.get_width()/2., p.get_height()),
  ha='center', va='center',
  xytext=(0,5),
  textcoords='offset points',
  fontsize=8)
  #saves the fig, commented out for now - DOES WORK
  my_file = 'audience_df_' + col + '.png'
  plt.savefig(my_file, bbox_inches='tight')

#creates and saves graphs for ctr, click_to_retail_rate
cols_for_rate_graphs = ['CTR', 'Click_To_Retail_Rate']
for col in cols_for_rate_graphs:
  authors_df.sort_values(col, ascending=False, inplace=True)
  authors_df_head = authors_df.head(5)
  barplot = sns.catplot(x=authors_df_head.index, y=col, data=authors_df_head, kind='bar', palette='cool', ci=None)
  y_label = str(barplot.ax.get_ylabel).split()
  y_label = y_label[5].replace('ylabel=','').replace('>>', '').strip().replace('_', ' ').replace('\'', '')
  barplot.set_ylabels(y_label)
  y_axis = str(barplot.ax.get_ylabel).split()
  y_axis = ' '.join(y_axis[5:]).replace('ylabel=','').replace('>>', '').replace('\'', '')
  x_axis = str(barplot.ax.get_xlabel).split()
  x_axis = ' '.join(x_axis[4])
  x_axis = re.sub('.+=|\'|,|\s', '', x_axis).replace('_', ' ')
  barplot.set_xlabels(x_axis)
  barplot.set(title=(str(y_axis) + ' by ' + str(x_axis)))
  barplot.set_xticklabels(rotation=45, horizontalalignment='right', fontsize='x-small')
  vals = barplot.ax.get_yticks()
  barplot.set_yticklabels(['{:,.2%}'.format(x) for x in vals])
  #left_lim, right_lim = plt.ylim()
  #mean_value = authors_df_head[col].std()
  #right_lim = right_lim - mean_value
  #left_lim = left_lim + 2.5
  #max_value = authors_df_head[col].max().round(4) * 100
  #max_name = authors_df_head[col].idxmax()
  #plt.text(left_lim, right_lim, r'''Highest {}:
  #{} ({}%)'''.format(y_axis, max_name, max_value), fontsize=8, bbox={'fc': 'white'})
  for p in barplot.ax.patches:
    barplot.ax.annotate(str((p.get_height() * 100).round(2)) + '%',
  (p.get_x() + p.get_width()/2., p.get_height()),
  ha='center', va='center',
  xytext=(0,5),
  textcoords='offset points',
  fontsize=7.5)
  #saves the fig, commented out for now - DOES WORK
  my_file = 'authors_df_' + col + '.png'
  plt.savefig(my_file, bbox_inches='tight')

"""

#splitting Objectives
traffic = all_data.loc[all_data.Objective == 'Traffic', :]
conversions = all_data.loc[all_data.Objective == 'Conversions', :]
engagement = all_data.loc[all_data.Objective == 'Engagement', :]
reach = all_data.loc[all_data.Objective == 'Reach', :]
page_likes = all_data.loc[all_data.Objective == 'Page Likes', :]
video_views = all_data.loc[all_data.Objective == 'Video Views', :]


#sns.pairplot(all_data)

#plt.show()