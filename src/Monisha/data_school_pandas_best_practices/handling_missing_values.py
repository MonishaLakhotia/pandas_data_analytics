import pandas as pd
import matplotlib.pyplot as plt

#Dataset 1
#police data set
#link to info: https://github.com/stanford-policylab/opp/blob/master/data_readme.md

ri = pd.read_csv('~/Desktop/ri_statewide_2020_04_01.csv')

#question 4: why is search_type missing so often?
#check column names
print(ri.columns)

#checking search_basis and reason_for_search nan values
print(ri.shape)
print(ri.isna().sum())
print(ri.reason_for_search.isna().sum())
print(ri.search_basis.isna().sum())

#looking at search_basis and reason_for_search value_counts()
print(ri.search_basis.value_counts(dropna=False))
print()
print(ri.reason_for_search.value_counts(dropna=False))\

#was a search conducted?
print(ri.search_conducted.value_counts())

#so we see reason_for_search and search_basis are the same as the False values
#reason their nan values are so high is because a search wasn't conducted

#some filtering to check
print(ri.loc[ri.search_conducted == False, 'reason_for_search'].value_counts(dropna=False))
#so you see that all 491414 nan values are when search_conducted is False, confirms belief