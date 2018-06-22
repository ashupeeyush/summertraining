# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:11:32 2018

@author: Peeyush Goyal
"""

import pandas as pd
import matplotlib.pyplot as plt
rcsv= pd.read_csv("Automobile.csv")



df = pd.DataFrame()
df=rcsv["make"].value_counts()

make_val = df.head(10)
make_name = list(make_val.index)
comp = max(make_val)
exp=[]
for i in make_val:
    if i==comp:
        exp.append(0.2)
    else:
        exp.append(0)


ax1 = plt.subplot()
ax1.axis('equal') 
ax1.pie(make_val,exp, labels=make_name, autopct='%1.2f%%')
plt.show()

#---------------------------------------------------------------------
df=rcsv["make"].value_counts()
df1=pd.DataFrame({'make':df.index,'values':df.values})
ax1 = plt.subplot()
sizes=df1.iloc[0:10,1].values
ax1.axis('equal') 
ax1.pie(sizes,exp, labels=df1.iloc[0:10,0].values, autopct='%1.2f%%')
plt.show()
