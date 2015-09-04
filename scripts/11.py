# How much did the state of California collect in property taxes, according to the U.S. Census 2013 Annual Survey of State Government Tax Collections?
# http://www.census.gov/govs/statetax/historical_data.html
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import re
import pandas as pd
year = 2013
state = 'CA'
url = 'http://www.census.gov/cgi-bin/geo/location' #the url used in the form on page
post_params = {'Location': 'govs/statetax/historical_data_%s.html' % year}
resp = requests.post(url, data = post_params) #post to the url with our parameters
soup = BeautifulSoup(resp.content) #soupify and find the link to the text file
tablelink = soup.find('a',attrs={'title':'Link to Flat Data File'})
resp2 = requests.get(tablelink.attrs['href']) #get text file
tablelines = re.split(',\n',re.sub(',R?,',',',resp2.text)) #remove the 'R's and extra commas, then split on newlines
d=defaultdict(list) #allows us to add keys as they come up
for idx,row in enumerate(tablelines):
 if idx == 0: #first row, use as index
  df_index = re.split(',',row)[1:]
 elif len(row) > 0: #rest of rows get added to defaultdict
  d[re.split(',',row)[0]]=[int(x) for x in re.split(',',row)[1:]]
df=pd.DataFrame(d,index=df_index) #convert to pandas dataframe
print(df['T01'][state])
