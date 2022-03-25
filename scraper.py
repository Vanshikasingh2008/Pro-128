import requests
from bs4 import BeautifulSoap as b
import time
import csv
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = requests.get(START_URL)
page = b(browser.test, "html.parser")
table = page.find("table")

temp_list = []
table_rows = table.find_all("tr")
for tr in table_rows:
  td = tr.find_all("td")
  row = [i.text.rstrip() for i in td]
  temp_list.append(row)

names=[]
distance=[]
bayer=[]
spectral_g=[]
mass=[]
radius=[]
luminous=[]

for i in range(1,len(temp_list)):
  names.append(temp_list[i][1])
  distance.append(temp_list[i][3])
  bayer.append(temp_list[i][2])
  spectral_g.append(temp_list[i][4])
  mass.append(temp_list[i][5])
  radius.append(temp_list[i][6])
  luminous.append(temp_list[i][7])

df = pd.DataFrame(list(zip(names,bayer,distance,spectral_g,mass,radius,luminous)), columns=['Star_name','Bayer designation','Distance','Spectral_Glass','Mass','Radius','Luminosity'])
df.to_csv("bright_stars.csv")