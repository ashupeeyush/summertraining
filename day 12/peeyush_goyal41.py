# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:11:59 2018

@author: Peeyush Goyal
"""

import pandas as pd
import numpy as np

rcsv= pd.read_csv("Automobile.csv")

rcsv["price"]=rcsv["price"].fillna(rcsv["price"].mean())

array=np.array(rcsv["price"])
print array.mean()
print array.max()
print array.min()
print array.std()


