# Web scraping

> Web Scraping

```python
import csv
import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
url = 'https://wuzzuf.net/search/jobs/?q=python&a=navbg'
connect = requests.get(url)

content = connect.content

soup = BeautifulSoup(content,'lxml')
# job title
titles_class = 'css-m604qf'
jop_titles = soup.find_all('h2',{'class':titles_class})

# company names 
company_class ='css-17s97q8'
company_name = soup.find_all('a',{'class':company_class})

# time published 
time_class_active = 'css-4c4ojb'
time_published_active = soup.find_all('div',{'class':time_class_active})

# time published not active 
time_class_not_active ='css-do6t5g'
time_published_not_active = soup.find_all('div',{'class':time_class_not_active})


# info 
info_class = 'css-1ve4b75'
info = soup.find_all('span',{'class':info_class})

# skills 
skills_class = 'css-nn640c'
skills = soup.find_all('a',{'class':skills_class})

lens = len(jop_titles)
title = []
skille = []
company = []
time_active = []
all_info = []
time_not_active = []
for inofrmation in range(lens):
    title.append(jop_titles[inofrmation].text)
    company.append(company_name[inofrmation].text)
    skille.append(skills[inofrmation].text)
    all_info.append(info[inofrmation].text)
    try:
        time_active.append(time_published_active[inofrmation].text)
        time_not_active.append(time_published_not_active[inofrmation].text)
    except IndexError as a:
        continue
file_list = [title,company,time_active,time_not_active,skille,all_info]
exported = zip_longest(*file_list)

# you must insert data to file 
```
