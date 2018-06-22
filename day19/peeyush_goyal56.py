# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 11:12:11 2018

@author: Peeyush Goyal
"""

import pandas as pd
import numpy as np
import statistics

df=pd.read_csv("Auto_mpg.txt",delim_whitespace=True,header=None,names=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" ])

features = df.iloc[:,1:-1]
label = df.iloc[:,0]

features.iloc[:,2]=features.iloc[:,2].replace('?',np.NAN)
features.iloc[:,2]=features.iloc[:,2].fillna(statistics.mode(features.iloc[:,2]))
features.iloc[:,2]=pd.to_numeric(features.iloc[:,2])
from sklearn.model_selection import train_test_split
feature_train, feature_test, lab_train,lab_test= train_test_split(features,label,test_size=0.2,random_state=0)

mmpg=max(df.iloc[:,0])
print df["car name"][df["mpg"]==mmpg]

from sklearn.tree import DecisionTreeRegressor
reg = DecisionTreeRegressor(random_state=0)
reg.fit(feature_train,lab_train)
print reg.score(feature_test,lab_test)

from sklearn.ensemble import RandomForestRegressor
regr = RandomForestRegressor(n_estimators=10,random_state=0)
regr.fit(feature_train,lab_train)
print regr.score(feature_test,lab_test)

print reg.predict(np.array([6,215,100,2630,22.2,80,3]).reshape(1,-1))
print regr.predict(np.array([6,215,100,2630,22.2,80,3]).reshape(1,-1))
