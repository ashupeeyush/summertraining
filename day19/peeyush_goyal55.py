# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 11:25:45 2018

@author: Peeyush Goyal
"""
import pandas as pd
import numpy as np

df=pd.read_csv("PastHires.csv")

features = df.iloc[:,0:-1]
label = df.iloc[:,-1].values

#features.loc['e'] = [10,'Y',4,'MS','Y','N']


from sklearn.preprocessing import LabelEncoder
labelencoder1=LabelEncoder()
#labelencoder2=LabelEncoder()
label=labelencoder1.fit_transform(label)
"""for i in [1,3,4,5]:
    features[:,i]=labelencoder2.fit_transform(features[:,i])
"""    
for i in (1,3,4,5):
    features.iloc[:,i] = features.iloc[:,i].astype('category')
    features.iloc[:,i] = features.iloc[:,i].cat.codes


from sklearn.tree import DecisionTreeRegressor
reg = DecisionTreeRegressor(random_state=0)
reg.fit(features,label)

print reg.score(features,label)

from sklearn.ensemble import RandomForestRegressor
regr = RandomForestRegressor(n_estimators=10,random_state=0)
regr.fit(features,label)
print regr.score(features,label)

features.loc['e'] = [10,'Y',4,'MS','Y','N']
features.iloc[:,1] = features.iloc[:,1].astype('category')
features.iloc[-1,1] = features.iloc[-1,1].cat.codes

for i in (1,3,4,5):
    features.iloc[-1,i] = features.iloc[-1,i].astype('category')
    features.iloc[-1,i] = features.iloc[-1,i].cat.codes



#test= np.array([10,'Y',4,'MS','Y','N']).reshape(1,-1)
"""for i in [1,3,4,5]:
    test[:,i]=labelencoder2.transform(test[:,i])
test[:,1]=labelencoder2.transform(test[:,1])
test[:,3]=labelencoder2.transform(test[:,3])
test[:,4]=labelencoder2.transform(test[:,4])
test[:,5]=labelencoder2.transform(test[:,5])
"""

