import pandas as pd
import matplotlib.pyplot as plt

#Dataset 1
#police data set
#link to info: https://github.com/stanford-policylab/opp/blob/master/data_readme.md

ri = pd.read_csv('~/Desktop/ri_statewide_2020_04_01.csv')

#question 3: does gender effect who gets searched during a stop
print(ri.columns)
#relevant columns are subject_sex and search_conducted

#v1 - value_counts() and normalize = True
#establish baseline %
print(ri.search_conducted.value_counts(normalize=True))

#gender with percent
ser = ri.groupby('subject_sex').search_conducted.value_counts(normalize=True)
print(ser.loc[: , True])

#v2 - mean() - percentage of 1's (True values)
#establish baseline - to get percentage of 1's (True)
print(ri.search_conducted.mean())

#gender with percentage of 1's (True)
print(ri.groupby('subject_sex').search_conducted.mean())

#might be a relationship between gender and search conducted
#test to see if all violations lead to higher searches based on gender
print(ri.groupby(['reason_for_stop', 'subject_sex']).search_conducted.mean())

#men generally have a higher search rate than women regardless of offense
#can't say it's causation but there is a relationship