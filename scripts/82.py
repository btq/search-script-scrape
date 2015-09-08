'''In the most recent FDA Adverse Events Reports quarterly extract,
 the number of patient reactions mentioning "Death"
http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm'''

import re
import requests
from bs4 import BeautifulSoup

url = 'http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm'
