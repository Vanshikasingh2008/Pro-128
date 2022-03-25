import requests
from bs4 import BeautifulSoap as b
import time
import csv
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = requests.get(START_URL)
page = b(browser.test, "html.parser")
table = page.find_all("table")

temp_list = []
table_rows = table[7].table.find_all("tr")
for tr in table_rows:
  td = tr.find_all("td")
  row = [i.text.rstrip() for i in td]
  temp_list.append(row)

names=[]
distance=[]
mass=[]
radius=[]

for i in range(1,len(temp_list)):
  names.append(temp_list[i][0])
  distance.append(temp_list[i][5])
  mass.append(temp_list[i][8])
  radius.append(temp_list[i][9])

df = pd.DataFrame(list(zip(names,distance,mass,radius)), columns=['Star_name','Distance','Mass','Radius'])
df.to_csv("brown_dwarfs.csv")