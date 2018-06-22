# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:07:08 2018

@author: Peeyush Goyal
"""

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("crime_data.csv")
df=data.iloc[:,[1,2,4]]
"""from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
df["State"]=labelencoder.fit_transform(df["State"])

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
df=sc.fit_transform(df)
"""
from sklearn.decomposition import PCA
pca= PCA(n_components=2)
df= pca.fit_transform(df)

from sklearn.cluster import KMeans
"""wcss=[]
for i in range(3):
    kmeans=KMeans(n_clusters=i, init='k-means++',random_state=0)
    kmeans.fit(df)
    wcss.append(kmaens.inertia_)
"""
kmeans=KMeans(n_clusters=3, init='k-means++',random_state=0)
y_kmeans=kmeans.fit_predict(df)

plt.scatter(df[y_kmeans==0,0],df[y_kmeans==0,1],s=100,c='red')
plt.scatter(df[y_kmeans==1,0],df[y_kmeans==1,1],s=100,c='blue')
plt.scatter(df[y_kmeans==2,0],df[y_kmeans==2,1],s=100,c='green')
plt.legend()
plt.xlabel('Crimes')
plt.ylabel('cities')
plt.show()