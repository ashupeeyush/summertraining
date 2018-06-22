# -*- coding: utf-8 -*-
"""
Created on Tue May 22 11:57:23 2018

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
     if re.match(r'^[+-]?[0-9]*\.[0-9]+$',i):
        print "true"
     else:
        print "false"
        
        
        