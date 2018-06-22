# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 12:13:59 2018

@author: Peeyush Goyal
"""

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
iris=iris.data

from sklearn.decomposition import PCA
pca= PCA(n_components=2)
df= pca.fit_transform(iris)

from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=3, init='k-means++',random_state=0)
y_kmeans=kmeans.fit_predict(df)

plt.scatter(df[y_kmeans==0,0],df[y_kmeans==0,1],s=100,c='red',label='Iris_setosa')
plt.scatter(df[y_kmeans==1,0],df[y_kmeans==1,1],s=100,c='blue',label='Iris_versicolor')
plt.scatter(df[y_kmeans==2,0],df[y_kmeans==2,1],s=100,c='green',label='Iris_virginica')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=200,c='yellow',label='Centroid')
plt.legend()
plt.show()