# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:36:38 2018

@author: Peeyush Goyal
"""
import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
web="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"

page= urllib2.urlopen(web)

soup= BeautifulSoup(page)

table=soup.find("table",class_="wikitable")
b=[]
e=[]
count=0
for row in table.findAll("tr"):
    count+=1
    if count>1:
        cells=row.findAll("td")
        b.append(str(cells[1].text.strip()))
        
        e.append(str(cells[4].text.strip()))
        
df = pd.DataFrame()
df["State"]=b
df["National Share"]=e
ax1 = plt.subplot()
df=df.iloc[:6]
sizes=df.iloc[:,1].values
ax1.axis('equal') 
exp=[.2,0,0,0,0,0]
ax1.pie(sizes,exp, labels=df.iloc[:,0].values, autopct='%1.2f%%')
plt.show()

