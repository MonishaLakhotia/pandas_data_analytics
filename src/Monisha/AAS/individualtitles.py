from glob import glob
import os
from numpy.core.numeric import NaN
import pandas as pd
import src.utils as u
import re
import toml
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
#make sure to pip install requests again code: python -m pip install requests
#make sure to pip install bs4 again code: pip install beautifulsoup4

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# get the directory path where this script is
this_dir = os.path.dirname(os.path.realpath(__file__))
# grab the config file from this directory
config = toml.load(os.path.join(this_dir, 'config.toml'))
# prefix partial file paths found in the config.toml with the full path
u.set_full_paths(config, this_dir)

individual_titles = config['file_locations']['individual_titles']
files = sorted(glob(individual_titles))
# reads every csv file that matches a text pattern and puts them all into 1 dataframe
book_data: pd.DataFrame = pd.concat((pd.read_csv(file) for file in files), ignore_index=True)

#separating Products into Title, Additional_Info, and Book_Series
book_data['Products'] = book_data.Products.str.replace('\(with bonus novel\)', '')
book_data[['Title', 'Series']] = book_data.Products.str.split('\(', expand=True)
book_data[['To_Drop', 'Additional_Info']] = book_data.Products.str.split('.*:', expand=True)

#dropping unneeded cols and formatting Title/Series/Additional Info
book_data.drop(['To_Drop', 'Products', 'State', 'SKU', 'ROAS', 'Status'], 1, inplace=True)
book_data['Title'] = book_data.Title.str.replace(':.*', '')
book_data['Series'] = book_data.Series.str.replace('\)', '')
book_data['Additional_Info'] = book_data.Additional_Info.str.replace('\(.*\)', '')

to_strip = ['Title', 'Series', 'Additional_Info']
for col in to_strip:
  book_data[col] = book_data[col].str.strip()

#separates Series from Series_Number
book_data['Series_Number'] = book_data.Series.str.replace('.*(?<!\d)', '')
book_data['Series'] = book_data.Series.str.replace(',\s\d|\sBook\s\d', '')

#renames columns
book_data.rename({'CTR': 'CTR', 
'Spend(USD)': 'Spend', 
'CPC(USD)': 'CPC', 
'Sales(USD)': 'Sales',
'ACOS': 'ACOS'}, axis=1, inplace=True)

#creates Format column
book_data['Format'] = NaN

for index in range(len(book_data.ASIN)):
  if book_data.ASIN[index].startswith('B'):
    book_data.Format[index] = 'eBook'
  elif book_data.ASIN[index].isnumeric() or book_data.ASIN[index].endswith('X'):
    book_data.Format[index] = 'Print'

"""
#ATTEMPTS AT SCRAPING - BREAKS THE CODE SO DON'T USE
#lists headers
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
'Accept-Language': 'en-US, en;q=0.5'})

#creates URL df and fills URL with ASINs
urls_df = pd.DataFrame(book_data.ASIN)
urls_df['URL'] = NaN

for index in range(len(urls_df.ASIN)):
  urls_df.URL[index] = 'https://www.amazon.com/gp/product/' + urls_df.ASIN[index]
#TEST - fetches url
page = requests.get(urls_df.URL[0], headers=HEADERS)

#TEST - creates the object that will contain all the info for the URL
soup = BeautifulSoup(page.content, 'lxml')

#TEST - to pull text
title = soup.find(id='productTitle').get_text().strip()
print(title)
"""

"""
#lists headers
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
'Accept-Language': 'en-US, en;q=0.5'})

#creates URL df and fills URL with ASINs
urls_df = pd.DataFrame(book_data.ASIN)
urls_df['URL'] = NaN

for index in range(len(urls_df.ASIN)):
  urls_df.URL[index] = 'https://www.amazon.com/gp/product/' + urls_df.ASIN[index]

tracker_log = pd.DataFrame()
interval = 0

while interval < 1:
  for url_index, url in enumerate(urls_df.URL):
    #page = requests.get(urls_df.URL[url_index], headers=HEADERS)
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, features='lxml')

    #TEST - title
    title = soup.find(id='productTitle').get_text().strip()

    log = pd.DataFrame({'url': url, 'title': title}, index=url_index)
    tracker_log = tracker_log.append(log)
    sleep(5)
    
  interval +=1

"""
"""
urls_df = pd.DataFrame(book_data.ASIN)

titles = [] #TEST

for ASIN in urls_df.ASIN:
  page = requests.get('https://www.amazon.com/gp/product/' + ASIN, headers=HEADERS)
  soup = BeautifulSoup(page.text, 'html.parser')
  title = soup.find(id='productTitle').get_text().strip()
  sleep(randint(2,10))
  titles.append(title)

#creates URL df and fills URL with ASINs
urls_df = pd.DataFrame(book_data.ASIN)
urls_df['URL'] = NaN

for index in range(len(urls_df.ASIN)):
  urls_df.URL[index] = 'https://www.amazon.com/gp/product/' + urls_df.ASIN[index]

tracker_log = pd.DataFrame()
interval = 0

while interval < 1:
  for url_index, url in enumerate(urls_df.URL):
    #page = requests.get(urls_df.URL[url_index], headers=HEADERS)
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, features='lxml')

    #TEST - title
    title = soup.find(id='productTitle').get_text().strip()

    log = pd.DataFrame({'url': url, 'title': title}, index=url_index)
    tracker_log = tracker_log.append(log)
    
  interval +=1

#print(tracker_log)

def search_product_list(interval_count=1):
  #creates URL df and fills URL with ASINs
  urls_df = pd.DataFrame(book_data.ASIN)
  urls_df['URL'] = NaN
  for index in range(len(urls_df.ASIN)):
    urls_df.URL[index] = 'https://www.amazon.com/gp/product/' + urls_df.ASIN[index]

  tracker_log = pd.DataFrame()
  interval = 0

  while interval < interval_count:
    for url_index, url in enumerate(urls_df.URL):
      #page = requests.get(urls_df.URL[url_index], headers=HEADERS)
      page = requests.get(url, headers=HEADERS)
      soup = BeautifulSoup(page.content, features='lxml')

      #TEST - title
      title = soup.find(id='productTitle').get_text().strip()

      log = pd.DataFrame({'url': url, 'title': title}, index=url_index)
      tracker_log = tracker_log.append(log)
    
    interval +=1
    print('end')

search_product_list(1)

#print(tracker_log)
  #log = pd.DataFrame({'url': url, 'title': title})
  #print(log)
  #print()
  #urls_df.Title_Test[url_index].fillna(title)
  #log = pd.DataFrame({'url': url, 'title': title}, index=url_index)

#print(urls_df.Title_Test) 
"""
"""
#TEST - fetches url
page = requests.get(urls_df.URL[0], headers=HEADERS)

#TEST - creates the object that will contain all the info for the URL
soup = BeautifulSoup(page.content, 'lxml')

#TEST - to pull text
title = soup.find(id='productTitle').get_text().strip()
print(title)
#title = soup.find('span', attrs={'id': 'productTitle'})
#title_value = title.string
#title_string = title_value.strip()
#print(title_string)
#.get_text().strip()
"""

#creates function to fix CTR, CPC, and ACOS when merging - KEEP THIS AFTER THE REST OF THE CLEANING FOR NOW
def agg_functions(df):
  df['CTR'] = df.Clicks / df.Impressions
  df['CPC'] = df.Spend / df.Clicks
  df['ACOS'] = df.Spend / df.Sales

#to merge duplicates (allows NaN) - KEEP THIS AFTER THE REST OF THE CLEANING
merge_titles = book_data.groupby(['Title'], dropna=False).sum()
agg_functions(merge_titles)

print(merge_titles)
"""
NOTE on merge: will have to add Author to the list when you have it 
Decide on whether to include any other non-int information to this one 
Or if you just want to create a new df for that info as well

"""

"""
TO DO:
-Figure out next steps - 
  -figure out how to add author names and pub dates
  -try to figure out subgenres as well
  -try to figure out what to do about books missing the Series_Number
  -also figure out if any columns need to be changes to int
  -also deal with reordering cols
  -decide if you want to create new dfs for other info like subgenre or ebook v print
  or if you want to merge some of the into the merge df as well
NOTE
the CTR and ACOS are not in % form, need to multiply by 100 and add percent sign

"""