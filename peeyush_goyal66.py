# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 12:39:50 2018

@author: Peeyush Goyal
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("banknotes.csv")
features = df.iloc[:,1:-1]
label = df.iloc[:,-1]

from sklearn.model_selection import train_test_split
feature_train, feature_test, lab_train,lab_test= train_test_split(features,label,test_size=0.2,random_state=0)


"""from sklearn.ensemble import RandomForestClassifier
regr = RandomForestClassifier(n_estimators=10,random_state=0)
regr.fit(feature_train,lab_train)
print regr.score(feature_train,lab_train)
"""
from sklearn.neighbors import KNeighborsClassifier
regr=KNeighborsClassifier(n_neighbors=5,p=2)
regr.fit(feature_train,lab_train)
print regr.score(feature_test,lab_test)
lab_pred=regr.predict(feature_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(lab_test, lab_pred)


from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = regr, X = feature_test, y = lab_test, cv = 10)
print ("mean accuracy is",accuracies.mean())
print (accuracies.std())
