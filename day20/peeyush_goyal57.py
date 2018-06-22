# -*- coding: utf-8 -*-
"""
Created on Wed Jun 06 12:11:23 2018

@author: Peeyush Goyal
"""

import pandas as pd
import numpy as np

df=pd.read_csv("affairs.csv")

features = df.iloc[:,:-1].values
label = df.iloc[:,-1]
features1=features

from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[6])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]
onehotencoder=OneHotEncoder(categorical_features=[11])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]

from sklearn.model_selection import train_test_split
feature_train, feature_test, lab_train,lab_test= train_test_split(features,label,test_size=0.2,random_state=0)

from sklearn.linear_model import LogisticRegression
reg= LogisticRegression(random_state=0)
reg.fit(feature_train,lab_train)
print reg.score(feature_train,lab_train)
print reg.score(feature_test,lab_test)
label_pre=reg.predict(feature_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(lab_test,label_pre)

label.value_counts(normalize=True)

print reg.predict([[1,0,0,0,0,0,0,1,0,0,3,25,3,1,4,16]])

import statsmodels.formula.api as sm
features1= np.append(arr=np.ones((6366,1)).astype(int),values=features1, axis=1)
features_opt=features1[:,:]
reg_ols=sm.OLS(endog=label,exog=features_opt).fit()
print reg_ols.summary()

features_opt=features1[:,[0,1,2,3,5,6,7,8]]
reg_ols=sm.OLS(endog=label,exog=features_opt).fit()
print reg_ols.summary()

features_opt=features[:,[0,1,2,3,5,6,7]]
reg_ols=sm.OLS(endog=label,exog=features_opt).fit()
print reg_ols.summary()
