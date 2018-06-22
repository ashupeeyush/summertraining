# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:51:42 2018

@author: Peeyush Goyal
"""

import pandas as pd
df=pd.read_csv("Foodtruck.csv")

features = df.iloc[:,0:1].values
labels = df.iloc[:,1].values

from sklearn.model_selection import train_test_split
feature_train, feature_test, label_train,label_test= train_test_split(features,labels,test_size=0.4,random_state=0)

from sklearn.linear_model import LinearRegression

reg= LinearRegression()
reg.fit(feature_train,label_train)

lab_pre=reg.predict(feature_test)


import matplotlib.pyplot as plot
plot.scatter(feature_train,label_train,color='red')
plot.plot(feature_train,reg.predict(feature_train),color='blue')
plot.show()

import matplotlib.pyplot as plot
plot.scatter(feature_test,label_test,color='red')
plot.plot(feature_test,reg.predict(feature_test),color='blue')
plot.show()

print reg.predict(3.073)

print reg.score(feature_test,label_test)




