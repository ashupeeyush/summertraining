# -*- coding: utf-8 -*-
"""
Created on Tue May 22 23:57:41 2018

@author: Peeyush Goyal
"""

import re
lst=[]
while True:
    a= raw_input()
    if not a:
        break
    if re.match(r'^[\w-]+@[a-zA-Z0-9]+?\.[a-zA-Z]{2,4}$',a):
       lst.append(a)
       
print lst
        