# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:32:55 2018

@author: Peeyush Goyal
"""

import pandas as pd
df=pd.read_csv("Bahubali2_vs_Dangal.csv")

features = df.iloc[:,0:1].values
lab_bahu = df.iloc[:,1:2].values
lab_dan = df.iloc[:,2].values

from sklearn.model_selection import train_test_split
feature_train, feature_test, lab_bahu_train,lab_bahu_test= train_test_split(features,lab_bahu,test_size=0.2,random_state=0)

from sklearn.model_selection import train_test_split
feature_train, feature_test, lab_dan_train,lab_dan_test= train_test_split(features,lab_dan,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
reg= LinearRegression()

reg.fit(feature_train,lab_bahu_train)
lab_bahu_pre=reg.predict(feature_test)
print reg.score(feature_test,lab_bahu_test)
print reg.predict(10)

reg.fit(feature_train,lab_dan_train)
lab_dan_pre=reg.predict(feature_test)
print reg.score(feature_test,lab_dan_test)
print reg.predict(10)
