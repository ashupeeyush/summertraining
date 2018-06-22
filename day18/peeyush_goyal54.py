# -*- coding: utf-8 -*-
"""
Created on Mon Jun 04 11:26:35 2018

@author: Peeyush Goyal
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plot

df=pd.read_csv("bluegills.csv")

features = df.iloc[:,0:1].values
label = df.iloc[:,1].values

reg= LinearRegression()
reg.fit(features,label)

plot.scatter(features,label,color='red')
plot.plot(features,reg.predict(features),color='blue')
plot.show()
print reg.score(features,label)
print reg.predict(5)

poly_obj=PolynomialFeatures(degree=4)
features_poly=poly_obj.fit_transform(features)
reg.fit(features_poly,label)
plot.scatter(features,label,color='red')
plot.plot(features,reg.predict(poly_obj.fit_transform(features)),color='blue')
plot.show()
print reg.score(features_poly,label)

print (reg.predict(poly_obj.fit_transform(5)))

fea_grid=np.arange(min(features),max(features),0.1)
fea_grid=fea_grid.reshape(-1,1)
plot.scatter(features,label,color='red')
plot.plot(fea_grid,reg.predict(poly_obj.fit_transform(fea_grid)),color='blue')
plot.show()