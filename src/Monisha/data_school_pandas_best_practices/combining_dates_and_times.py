import pandas as pd
import matplotlib.pyplot as plt

#Dataset 1
#police data set
#link to info: https://github.com/stanford-policylab/opp/blob/master/data_readme.md

ri = pd.read_csv('~/Desktop/ri_statewide_2020_04_01.csv')

#question 6: which year had the least number of stops?
#checking columns
print(ri.columns)

#checking series date and time
print(ri.date)
print(ri.time)

#changed date to datetime
ri['date']= pd.to_datetime(ri.date)

#pulling out years, and using value_counts()
print(ri.date.dt.year.value_counts())
#2005 has the smallest number of arrest
#good to keep in mind that there might be a reason that this set of stops are so low


#to combine date and time
combined = ri.date.str.cat(ri.time, sep=' ')
ri['date_time'] = pd.to_datetime(combined)

#finding answer with combined
print(ri.date_time.dt.year.value_counts())