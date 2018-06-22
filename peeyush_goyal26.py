# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:51:24 2018

@author: Peeyush Goyal
"""
from collections import OrderedDict
dd1=OrderedDict()
while True:
    a= raw_input()
    if not a:
        break
    l1=a.split(" ")
    value=l1[-1]
    key=' '.join(l1[0:-1])
    if key in dd1:
        dd1[key]+=int(value)
    else:
        dd1[key]=int(value)

    
for i,j in dd1.items():
    print i, j     
    
    
    