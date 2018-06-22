# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:26:51 2018

@author: Peeyush Goyal
"""

import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import datetime
df = pd.DataFrame()

today=int(datetime.date.today().strftime("%y%m%d"))
l1 = ["Meerut","Muzaffarnagar","Ghaziabad","Faridabad","Gurgaon","Karnal","Alwar","Bharatpur","Delhi"]
for i in l1:
    b=[]
    c=[]
    d=[]
    for a in range(0,6):
        day=str(today+a)
        url="https://www.timeanddate.com/weather/india/"+i+"/hourly?hd="+day
        page= urllib2.urlopen(url)
        
        soup= BeautifulSoup(page,"lxml")
        
        table=soup.find_all("table",class_="zebra")
        
        for row in table:
            row=row.find("tbody")
            rows=row.find_all("tr")
            for cells in rows:
                cells=cells.find_all("td")
                b.append((cells[1].text.encode('utf-8')))
                c.append((cells[4].text.encode('utf-8')))
                d.append((cells[6].text.encode('utf-8')))
    df["temp of "+i]=b
    df["wind speed in "+i]=c
    df["humidity in "+i]=d



from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

features = df.iloc[:,0:-3].values
lab1 = df.iloc[:,-3:].values
"""lab2 = df.iloc[:,-2].values
lab3 = df.iloc[:,-1].values"""

from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()

for i in range(0,24):
    features[:,i]=labelencoder.fit_transform(features[:,i])
    
for i in range(0,3):
    lab1[:,i]=labelencoder.fit_transform(lab1[:,i])    

"""lab1=labelencoder.fit_transform(lab1)
lab2=labelencoder.fit_transform(lab2)
lab3=labelencoder.fit_transform(lab3)
"""
from sklearn.model_selection import train_test_split
feature_train, feature_test, lab1_train,lab1_test= train_test_split(features,lab1,test_size=0.2,random_state=0)
reg= LinearRegression()
reg.fit(feature_train,lab1_train)

print reg.score(feature_test,lab1_test)

poly_obj=PolynomialFeatures(degree=4)
features_poly=poly_obj.fit_transform(features)
reg.fit(features_poly,lab1)

view=pd.DataFrame(features)

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = reg, X = feature_train, y = lab1_train, cv = 10)
print ("mean accuracy is",accuracies.mean())
print (accuracies.std())




        
