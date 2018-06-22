# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:14:02 2018

@author: Peeyush Goyal
"""

import pandas as pd

df=pd.read_csv("Automobile.csv")

print df.dtypes

df1=pd.DataFrame(df).select_dtypes(include=[object])
df=df.values
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder=LabelEncoder()
df[:,5]=labelencoder.fit_transform(df[:,5])
df[:,6]=labelencoder.fit_transform(df[:,6])
df[:,7]=labelencoder.fit_transform(df[:,7])
df[:,2]=labelencoder.fit_transform(df[:,2])
df[:,3]=labelencoder.fit_transform(df[:,3])
df[:,4]=labelencoder.fit_transform(df[:,4])
df[:,8]=labelencoder.fit_transform(df[:,8])
df[:,14]=labelencoder.fit_transform(df[:,14])
df[:,15]=labelencoder.fit_transform(df[:,15])
df[:,17]=labelencoder.fit_transform(df[:,17])

from sklearn.preprocessing import Imputer

imputer =Imputer(missing_values="NaN",strategy="most_frequent",axis=0)

imputer=imputer.fit(df[ : , :])
df[ : , : ]=imputer.transform(df[ : , :])


onehotencoder=OneHotEncoder(categorical_features=[6,7])
df=onehotencoder.fit_transform(df).toarray()

view=pd.DataFrame(df)
