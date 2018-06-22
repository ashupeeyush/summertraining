# -*- coding: utf-8 -*-
"""
Created on Thu Jun 07 10:15:34 2018

@author: Peeyush Goyal
"""

import pandas as pd
import numpy as np

df=pd.read_csv("mushrooms.csv")

features = df.iloc[:,[5,-1,-2]].values
label = df.iloc[:,0]

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder1=LabelEncoder()
labelencoder2=LabelEncoder()
label=labelencoder1.fit_transform(label)
for i in [0,1,2]:
    features[:,i]=labelencoder2.fit_transform(features[:,i])

onehotencoder=OneHotEncoder(categorical_features=[0])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]
onehotencoder=OneHotEncoder(categorical_features=[8])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]
onehotencoder=OneHotEncoder(categorical_features=[14])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]

from sklearn.model_selection import train_test_split
feature_train, feature_test, lab_train,lab_test= train_test_split(features,label,test_size=0.2,random_state=0)

from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5,p=2)
classifier.fit(feature_train,lab_train)

test=classifier.predict(feature_test)
print classifier.score(feature_train,lab_train)
print classifier.score(feature_test,lab_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(lab_test,test)




view=pd.DataFrame(features)
