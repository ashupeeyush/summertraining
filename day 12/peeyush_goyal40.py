# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:02:21 2018

@author: Peeyush Goyal
"""

import numpy as np

inp=raw_input()
lst=inp.split(" ")
arr=np.array(lst,np.int32)
arr=arr.reshape(3,3)
print arr

