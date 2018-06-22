# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:34:16 2018

@author: Peeyush Goyal
"""
import pandas as pd

df = pd.read_csv("training_titanic.csv")
df = df.fillna(df["Age"].mean())

df['child']=0
df['child'][df['Age']<18]=1

comp =  df.groupby(['child'])
print comp["Survived"].value_counts(normalize=True)

