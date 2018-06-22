# -*- coding: utf-8 -*-
"""
Created on Tue May 29 12:51:41 2018

@author: Peeyush Goyal
"""

import pandas as pd

df=pd.read_csv("Loan.csv")

features = df.iloc[:,1:-1].values
labels = df.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder=LabelEncoder()
for i in [0,1,2,3,4,-1]:
    features[:,i]=labelencoder.fit_transform(features[:,i])



from sklearn.model_selection import train_test_split
feature_train, feature_test, label_train,label_test= train_test_split(features,labels,test_size=0.2,random_state=0)

onehotencoder=OneHotEncoder(categorical_features=[-1])
feature_train=onehotencoder.fit_transform(feature_train).toarray()
feature_test=onehotencoder.fit_transform(feature_test).toarray()

label_train=labelencoder.fit_transform(label_train)
label_test=labelencoder.fit_transform(label_test)

