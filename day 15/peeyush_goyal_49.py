# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:33:15 2018

@author: Peeyush Goyal
"""

import pandas as pd
import numpy as np
df=pd.read_csv("Red_Wine.csv")
df.iloc[:,0]=df.iloc[:,0].fillna(df.iloc[:,0].value_counts().index[0])
df=df.fillna(np.mean(df))

features = df.iloc[:,0:-1].values
labels = df.iloc[:,-1].values
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,StandardScaler
labelencoder=LabelEncoder()
features[:,0]=labelencoder.fit_transform(features[:,0])


onehotencoder=OneHotEncoder(categorical_features=[0])
features=onehotencoder.fit_transform(features).toarray()

sc = StandardScaler()
features=sc.fit_transform(features)

from sklearn.model_selection import train_test_split
feature_train, feature_test, label_train,label_test= train_test_split(features,labels,test_size=0.2,random_state=0)

view=pd.DataFrame(features)