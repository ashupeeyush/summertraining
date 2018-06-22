# -*- coding: utf-8 -*-
"""
Created on Thu May 24 11:59:06 2018

@author: Peeyush Goyal
"""

import pandas as pd

df= pd.read_csv("training_titanic.csv")

print df["Survived"].value_counts()

print df["Survived"].value_counts(normalize=True)


train= df.groupby(['Sex'])

print train["Survived"].value_counts()
