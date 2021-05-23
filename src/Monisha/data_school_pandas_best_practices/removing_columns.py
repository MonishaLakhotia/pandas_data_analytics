import pandas as pd
import matplotlib.pyplot as plt

#Dataset 1
#police data set
#link to info: https://github.com/stanford-policylab/opp/blob/master/data_readme.md

ri = pd.read_csv('~/Desktop/ri_statewide_2020_04_01.csv')

#exercise 1: remove the column that only contains missing values

print(ri.shape)
#print(ri.isna().sum())
print(ri.dropna(how='all', axis=1, inplace=True))
#this did not make a difference for mine because none of my columns are entirely empty