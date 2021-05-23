import pandas as pd
import matplotlib.pyplot as plt

#Dataset 1
#police data set
#link to info: https://github.com/stanford-policylab/opp/blob/master/data_readme.md

ri = pd.read_csv('~/Desktop/ri_statewide_2020_04_01.csv')


#question 7: how does drug activity change by time of day
#checking column names
#print(ri.columns)

#checking contraband_drugs series dtype - not a boolean
#print(ri.contraband_drugs.dtype)

#drop the nan values
ri.dropna(subset=['contraband_drugs'], how='any', inplace=True)

#make sure they're dropped
print(ri.contraband_drugs.value_counts(dropna=False))

#converting to boolean
ri['contraband_drugs_bool'] = ri.contraband_drugs.astype(bool)

#making sure it converted
print(ri.contraband_drugs_bool.value_counts(dropna=False))

#convert time series to datetime
ri['time'] = pd.to_datetime(ri.time)

#seeing hour
print(ri.time.dt.hour)

#grouping by time, ristricting to contraband_drugs_bool series, getting mean, and plotting
ri.groupby(ri.time.dt.hour).contraband_drugs_bool.mean().plot()

#showing plot
plt.show()