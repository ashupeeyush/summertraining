# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:08:14 2018

@author: Peeyush Goyal
"""
import numpy as np

x = np.random.random_integers(5,15,40)

count=np.bincount(x)
print np.argmax(count)

lst= x.tolist()

max(set(lst), key=lst.count)

