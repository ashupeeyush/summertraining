# -*- coding: utf-8 -*-
"""
Created on Fri Jun 01 11:40:34 2018

@author: Peeyush Goyal
"""

import pandas as pd
import numpy as np
df=pd.read_csv("iq_size.csv")

features = df.iloc[:,1:].values
label = df.iloc[:,0].values
from sklearn.linear_model import LinearRegression

reg= LinearRegression()
reg.fit(features,label)

lab_pre=reg.predict(features)

print reg.score(features,label)

print reg.predict(np.array([90,70,150]).reshape(1,-1))

import statsmodels.formula.api as sm
features= np.append(arr=np.ones((38,1)).astype(int),values=features, axis=1)

features_opt=features[:,[0,1,2,3]]
reg_ols=sm.OLS(endog=label,exog=features_opt).fit()
reg_ols.summary()

features_opt=features[:,[0,1,2]]
reg_ols=sm.OLS(endog=label,exog=features_opt).fit()
reg_ols.summary()

features_opt=features[:,[1,2]]
reg_ols=sm.OLS(endog=label,exog=features_opt).fit()
reg_ols.summary()

features_opt=features[:,[1]]
reg_ols=sm.OLS(endog=label,exog=features_opt).fit()
reg_ols.summary()





