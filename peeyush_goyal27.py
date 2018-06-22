# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:55:33 2018

@author: Peeyush Goyal
"""

i=raw_input()
l1=i.split(" ")
count=0
pos=0
for a in l1:
    a=int(a)
    if a<0:
        pos+=1
for a in l1:
    if a[0::]==a[::-1]:
        count+=1
if count==0 or pos>0:
    print "False"
else:
    print "True"