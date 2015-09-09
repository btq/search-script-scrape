'''In the most recent FDA Adverse Events Reports quarterly extract,
 the number of patient reactions mentioning "Death"
http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm'''

import re
import zipfile
import requests
from io import BytesIO
from bs4 import BeautifulSoup

urlroot = 'http://www.fda.gov' #used later to get download link
url = 'http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm'
resp = requests.get(url) #get web page
soup = BeautifulSoup(resp.content) #soupify content
zipurl = soup.find_all(href=re.compile('.zip'))[0].attrs['href'] #find first href link to a .zip
zipmem = BytesIO(requests.get(urlroot+zipurl).content) #read zip file into memory
zipf = zipfile.ZipFile(zipmem) #open zipfile
for fn in zipf.namelist(): #go through files in zip file
 if fn.startswith('ascii/REAC'): # match our Reaction file name
  strdata = str(zipf.read(fn)) # read file and convert to string (from bytes)
deathmatch = re.findall('Death',strdata) # find all occurrences of 'Death'
print(len(deathmatch))
