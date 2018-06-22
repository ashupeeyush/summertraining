# -*- coding: utf-8 -*-
"""
Created on Fri Jun 01 12:27:25 2018

@author: Peeyush Goyal
"""

import pandas as pd
import numpy as np
df=pd.read_csv("stats_females.csv")

features = df.iloc[:,1:].values
label = df.iloc[:,0].values

from sklearn.linear_model import LinearRegression

reg= LinearRegression()
reg.fit(features,label)

lab_pre=reg.predict(features)

print reg.score(features,label)

import statsmodels.formula.api as sm
features= np.append(arr=np.ones((214,1)).astype(int),values=features, axis=1)

features_opt=features[:,[0,1,2]]
reg_ols=sm.OLS(endog=label,exog=features_opt).fit()
print reg_ols.summary()

print "coeffcient of mother's height: ",reg_ols.params[1]
print "coeffcient of fathers's height: ",reg_ols.params[2]

