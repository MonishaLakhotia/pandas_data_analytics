import pandas as pd
import matplotlib.pyplot as plt

#Dataset 1
#police data set
#link to info: https://github.com/stanford-policylab/opp/blob/master/data_readme.md

ri = pd.read_csv('~/Desktop/ri_statewide_2020_04_01.csv')

#question 8: do most stops occur at night?

#convert time column to datetime
ri['time'] = pd.to_datetime(ri.time)

ri.time.dt.hour.value_counts().sort_index().plot()

plt.show()