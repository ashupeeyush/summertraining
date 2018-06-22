# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 12:45:39 2018

@author: Peeyush Goyal
"""

import pandas as pd
import matplotlib as plot

df=pd.read_csv("deliveryfleet.csv")
features = df.iloc[:,1:]

from sklearn.cluster import k_means

