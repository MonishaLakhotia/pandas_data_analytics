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

#NNNNNNEEEEWWWWWWWWWW
#lists headers
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
'Accept-Language': 'en-US, en;q=0.5'})

#creates URL df and fills URL with ASINs
urls_df = pd.DataFrame(book_data.ASIN)
urls_df['URL'] = NaN

for index in range(len(urls_df.ASIN)):
  urls_df.URL[index] = 'https://www.amazon.com/gp/product/' + urls_df.ASIN[index]

#TEST - fetches url
page = requests.get(urls_df.URL[0], headers=HEADERS).text

#TEST - creates the object that will contain all the info for the URL
soup = BeautifulSoup(page, 'lxml')

#TEST - to pull text
title = soup.find(id='productTitle').get_text().strip()
print(title)

"""
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