# -*- coding: utf-8 -*-
"""
Created on Mon May 28 14:01:48 2018

@author: Peeyush Goyal
"""

import pandas as pd
rcsv= pd.read_csv("cars.csv")
col = list(rcsv.columns)

features = rcsv.iloc[:,1:].values
labels = rcsv.iloc[:,0].values

from sklearn.model_selection import train_test_split

feature_train, feature_test, label_train,label_test= train_test_split(features,labels,test_size=0.2,random_state=0)

print feature_train
print feature_test
print label_train
print label_test

df1 = pd.DataFrame(feature_train,columns=col[1:])
df1.to_csv("feature_train.csv",index=False)

df1 = pd.DataFrame(feature_test,columns=col[1:])
df1.to_csv("feature_test.csv",index=False)

df1 = pd.DataFrame(label_train)
df1.to_csv("label_train.csv")

df1 = pd.DataFrame(label_test)
df1.to_csv("label_test.csv")