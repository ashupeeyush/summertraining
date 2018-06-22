# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 11:15:15 2018

@author: Peeyush Goyal
"""

import pandas as pd
import numpy as np
import statistics

df=pd.read_csv("tree_addhealth.csv")

features = df.iloc[:,[0,1,2,3,4,5,6,8,9,10,11,12,13,14,15]]
label = df.iloc[:,7]

features.iloc[:,6]=features.iloc[:,6].fillna(features.iloc[:,6].mean(),axis=0)
features.iloc[:,14]=features.iloc[:,14].fillna(statistics.mode(features.iloc[:,14]))
features=features.values

from sklearn.model_selection import train_test_split
feature_train, feature_test, lab_train,lab_test= train_test_split(features,label,test_size=0.2,random_state=0)

from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier(criterion='entropy',random_state=0)
classifier.fit(feature_train,lab_train)
test=classifier.predict(feature_test)
print classifier.score(feature_train,lab_train)
print classifier.score(feature_test,lab_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(lab_test,test)


features1 = df.iloc[:,[0,16]]
label1 = df.iloc[:,-4]

features1.iloc[:,1]=features1.iloc[:,1].fillna(statistics.mode(features1.iloc[:,1]))
features1=features1.values
label1=label1.fillna(statistics.mode(label1))

from sklearn.model_selection import train_test_split
feature1_train, feature1_test, lab1_train,lab1_test= train_test_split(features1,label1,test_size=0.2,random_state=0)

from sklearn.ensemble import RandomForestClassifier
classifier1=RandomForestClassifier(n_estimators=10,criterion='entropy',random_state=0)
classifier1.fit(feature1_train,lab1_train)
test1=classifier1.predict(feature1_test)
print classifier1.score(feature1_train,lab1_train)
print classifier1.score(feature1_test,lab1_test)

from sklearn.metrics import confusion_matrix
cm1 = confusion_matrix(lab1_test,test1)


features2 = df.iloc[:,[1,2,3,4,5]]
label2 = df.iloc[:,7]
from sklearn.model_selection import train_test_split
feature2_train, feature2_test, lab2_train,lab2_test= train_test_split(features2,label2,test_size=0.2,random_state=0)

classifier2=RandomForestClassifier(n_estimators=10,criterion='entropy',random_state=0)
classifier2.fit(feature2_train,lab2_train)
test2=classifier2.predict(feature2_test)
print classifier2.score(feature2_train,lab2_train)
print classifier2.score(feature2_test,lab2_test)

from sklearn.metrics import confusion_matrix
cm2 = confusion_matrix(lab2_test,test2)
