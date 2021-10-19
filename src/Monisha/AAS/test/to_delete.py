#what I had before we added the appending to d for all of these and then naming each of the sheets (pt.1)
"""
NOTE: Delete this part once you're sure agg functions are correct
#to groupby title and author (allows NaN) - KEEP THIS AFTER THE REST OF THE CLEANING
title_author = reordered.groupby(['Title', 'Author'], dropna=False).sum()


#to group by backlist and front list (allows NaN)- KEEP THIS AFTER THE REST OF THE CLEANING
six_months = date.today() - relativedelta(months=+6)
backlist = reordered.loc[reordered.Pub_Date < six_months]
backlist_asin_merge = backlist.groupby(['ASIN', 'Title', 'Author', 'Pub_Date'], dropna=False).sum()
frontlist = reordered.loc[reordered.Pub_Date >= six_months]
frontlist_asin_merge = frontlist.groupby(['ASIN', 'Title', 'Author', 'Pub_Date'], dropna=False).sum()

#sets index for reordered to Title
reordered.set_index(reordered.Title, inplace=True)
"""

#what I had before added appending to d and then naming each of the sheets (pt.2)
"""
NOTE: delete this part once you're sure all the agg functions are right, figureed out how to add names 
#for loop with agg_functions
dataframes = [reordered, title_author, d['assumed_subgenre'],
d['first_bisac_subject'], d['format'], d['author'], d['series_number'], 
backlist_asin_merge, frontlist_asin_merge]
for df in dataframes:
  agg_functions(df)

#to save as multisheet xlsx
file_location = ExcelWriter(config['file_locations']['output'])

def save_xls(list_dfs, xls_path):
  with ExcelWriter(xls_path) as writer:
    for n, df in enumerate(list_dfs):
      df.to_excel(writer,'sheet%s' % n)  
    writer.save()

save_xls(dataframes,file_location)

"""



#what I had original d for loop, that cycles through a list of these single groupbys (pt. 1)
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

#what I had original d for loop, that cycles through a list of these single groupbys (pt. 2)
""" 
NOTE: Delete this red bit once you've successfully saved dataframes, should not need
#for loop with agg_functions
dataframes = [reordered, title_author, d['assumed_subgenre'],
BISAC_subgenre, format, authors, backlist_asin_merge, frontlist_asin_merge]
for df in dataframes:
  agg_functions(df)
  """
