import pandas as pd
import matplotlib.pyplot as plt

#Dataset 1
#police data set
#link to info: https://github.com/stanford-policylab/opp/blob/master/data_readme.md

ri = pd.read_csv('~/Desktop/ri_statewide_2020_04_01.csv')

#exercise 2: Do men or women speed more often
print(ri.columns)
print(ri.subject_sex.head())
print(ri.reason_for_stop.head())

#solution version 1: groupby() and loc[] - I solved
#shows count of each value
print(ri.groupby('subject_sex').reason_for_stop.value_counts())

#saving groupby in object
df = ri.groupby('subject_sex').reason_for_stop.value_counts(normalize=True)
print(df)

#using loc[]
print(df.loc[:, 'Speeding'])

#solution version 2: filtering - he solved
print(ri[ri.reason_for_stop == 'Speeding'].subject_sex.value_counts(normalize=True))