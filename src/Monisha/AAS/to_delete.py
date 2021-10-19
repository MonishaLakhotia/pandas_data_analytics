"""
NOTE: Delete this red bit once you've successfully saved dataframes, should not need
#to group by subgenre (both assumed and BISAC) (allows NaN)
assumed_subgenre = reordered.groupby('Assumed_Subgenre', dropna=False).sum()
BISAC_subgenre = reordered.groupby('First_BISAC_Subject', dropna=False).sum()

#to group by format (allows NaN)
format = reordered.groupby('Format', dropna=False).sum()

#to group by authors (allows NaN)
authors = reordered.groupby('Author', dropna=False).sum()
"""

""" 
NOTE: Delete this red bit once you've successfully saved dataframes, should not need
#for loop with agg_functions
dataframes = [reordered, title_author, d['assumed_subgenre'],
BISAC_subgenre, format, authors, backlist_asin_merge, frontlist_asin_merge]
for df in dataframes:
  agg_functions(df)
  """