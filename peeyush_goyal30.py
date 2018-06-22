# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:18:55 2018

@author: Peeyush Goyal
"""

import urllib2
from bs4 import BeautifulSoup

icc="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

page= urllib2.urlopen(icc)

soup= BeautifulSoup(page)

right_table=soup.find('tbody')

a=[]
b=[]
c=[]
d=[]
e=[]
for row in right_table.findAll("tr"):
    cells=row.findAll("td")
    
    a.append(str(cells[0].text.strip()))
    b.append(str(cells[1].text.strip()))
    c.append(str(cells[2].text.strip()))
    d.append(str(cells[3].text.strip()))
    e.append(str(cells[4].text.strip()))

import pandas as pd

df = pd.DataFrame()
df["Position"]=a
df["team"]=b
df["matches"]=c
df["Points"]=d
df["Rating"]=e








