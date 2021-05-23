import pandas_data_analytics.utils as u
import toml
import re
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))
u.set_full_paths(config, this_dir)
csv_loc = config['file_locations']['training_data']
df = pd.read_csv(csv_loc)

def r(s):
  return re.sub('.*?\/(.*?)\/.*?\.\w+$', '\\1', flags=re.I, string=s) 

df['project'] = df['project_and_file'].apply(r)
df = df[~(df['project'] == 'Search')]
print('\n'.join(df['project'].unique()))

# aplot = sns.countplot(
#     data=df,
#     x="project"
# )

u.general_df_stats(df)

gdf = df[['project', 'project_and_file']].groupby('project').agg(['count'])

print(gdf)

# histogram with legend and no x labels
# aplot = sns.histplot(x='project', data=df, hue='project')
# plt.show()

# histogram without legend and has x labels
bplot = sns.countplot(x='project', data=df)
bplot.set_xticklabels(bplot.get_xticklabels(), rotation=10)
plt.show()
