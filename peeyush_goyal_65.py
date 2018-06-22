# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:19:37 2018

@author: Peeyush Goyal
"""

import pandas as pd
import matplotlib.pyplot as plt
import statistics
import numpy as np

df=pd.read_csv("breast_cancer.csv")
features = df.iloc[:,1:-1]
label = df.iloc[:,-1]

features['G']=features['G'].fillna(statistics.mode(features["G"]))
features=features.values

from sklearn.model_selection import train_test_split
feature_train, feature_test, lab_train,lab_test= train_test_split(features,label,test_size=0.2,random_state=0)

from sklearn.decomposition import PCA
pca= PCA(n_components=2)
feature_train= pca.fit_transform(feature_train)
feature_test= pca.transform(feature_test)

from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(feature_train, lab_train)

lab_pred = classifier.predict(feature_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(lab_test, lab_pred)

score = classifier.score(feature_test,lab_test)

classifier.predict(pca.transform([[6,2,5,3,2,7,9,2,4]]))


from matplotlib.colors import ListedColormap
features_set, labels_set = feature_test, lab_test
X1, X2 = np.meshgrid(np.arange(start = features_set[:, 0].min() - 1, stop = features_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = features_set[:, 1].min() - 1, stop = features_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(labels_set)):
    plt.scatter(features_set[labels_set == j, 0], features_set[labels_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('SVM (Test set)')
plt.legend()
plt.show()