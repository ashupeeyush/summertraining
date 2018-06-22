# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:00:55 2018

@author: Peeyush Goyal
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler
df= pd.read_csv("https://raw.githubusercontent.com/rasbt/pattern_classification/master/data/wine_data.csv",
     header=None,
     usecols=[0,1,2])


df.columns = ['Class label', 'Alcohol', 'Malic acid']

sc = StandardScaler()

df1=sc.fit_transform(df)

mm=MinMaxScaler()

df2=mm.fit_transform(df)

