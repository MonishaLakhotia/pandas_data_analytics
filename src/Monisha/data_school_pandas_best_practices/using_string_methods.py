import pandas as pd
import matplotlib.pyplot as plt

#Dataset 1
#police data set
#link to info: https://github.com/stanford-policylab/opp/blob/master/data_readme.md

ri = pd.read_csv('~/Desktop/ri_statewide_2020_04_01.csv')

#question 5: during search how often is a driver frisked
#check columns to find right column
print(ri.columns)

#search_conducted and frisk_performed
print(ri.loc[ri.search_conducted == False, 'frisk_performed'])
#frisk_performed is False when search_conducted is False

print(ri.loc[ri.search_conducted == True, 'frisk_performed'].value_counts(normalize=True))
#driver is frisked about 52% of the time

#using str method on reason_for_search
print(ri.reason_for_search.value_counts(dropna=False))
print(ri.reason_for_search.str.contains('Frisk').mean())
#in reason_for_search marked as frisk is about 9% of the time
#i don't think this is the right way to do it since we have a frisk_performed column