# -*- coding: utf-8 -*-
"""
Created on Wed May 23 00:53:35 2018

@author: Peeyush Goyal
"""

import re
lst=[]
while True:
    a= raw_input()
    if not a:
        break
    lst.append(a)
for i in lst:    
    if re.match(r'^[456][0-9]{3}[-]?[0-9]{4}[-]?[0-9]{4}[-]?[0-9]{4}[-]?',i):
        print "valid"
    else:
        print "invalid"
        
        