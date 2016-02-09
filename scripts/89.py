'''In fiscal year 2013, the short description of the most frequently cited type of FDA's inspectional observations related to food products. 
http://www.fda.gov/ICECI/Inspections/ucm250720.htm
'''
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

urlroot = 'http://www.fda.gov'
url = 'http://www.fda.gov/ICECI/Inspections/ucm250720.htm'
resp = requests.get(url) #get web page
soup = BeautifulSoup(resp.content) #soupify content
linktitles = soup.find_all('linktitle') #identify the linktitles
for lnk in linktitles:
 if lnk.string.startswith('FY 2013'): #if it's the 2013 linktitle
  yearlink = lnk.parent.attrs['href'] #take the href attribute of that linktitle's parent (<a>)
  break
resp2 = requests.get(urlroot+yearlink) #get that page
df = pd.read_html(urlroot+yearlink,attrs={'summary':"Foods"}) #it only parses the first row correctly due to the Food td spanning all rows
print(df[0]['Short Description'][0])
