# -*- coding: utf-8 -*-
"""
Created on Tue May 29 19:20:22 2018

@author: Peeyush Goyal
"""

import pandas as pd

df=pd.read_csv("Loan.csv")

features = df.iloc[:,1:-1]
labels = df.iloc[:,-1]

l1=list(features)

for i in l1:
    features[i] = features[i].astype('category')
    features[i] = features[i].cat.codes

labels = labels.astype('category')
labels = labels.cat.codes


features =pd.get_dummies(features, columns=["Property_Area"])

