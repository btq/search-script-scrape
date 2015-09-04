'''For the most recently posted TSA.gov customer satisfication survey, 
post the percentage of respondents who rated their "overall experience today"
 as "Excellent"
http://www.tsa.gov/web-metrics'''
import re
import requests
import warnings
from io import BytesIO
from bs4 import BeautifulSoup
from openpyxl import load_workbook

url = 'http://www.tsa.gov/web-metrics'
warnings.filterwarnings("ignore") #openpyxl issues pesky warning

resp = requests.get(url) #get web page
soup = BeautifulSoup(resp.content) #soupify content
xlsxurl = soup.find_all(href=re.compile('xlsx'))[0].attrs['href'] #find first href link
xlsx = BytesIO(requests.get(xlsxurl).content) #read xlsx file into memory
wb = load_workbook(xlsx,data_only=True) #load workbook, only values (no formulas)
ws=wb.get_sheet_by_name('Expanded') #select "Expanded" sheet, the name of the 1st sheet
total_count = 0
for row in ws.rows: # go through each row
 for idx,c in enumerate(row): # each cell in the row
  if c.value == 'Excellent': # Excellent is in column B, value in C
   exc_count = row[idx+1].value
  if c.value == 'Total': # Total is in column A, value in C
   total_count = row[idx+2].value
   break
 if total_count != 0: # when we have the total, print the answer and break the loop
  print(((exc_count+0.)/total_count) * 100)
  break
