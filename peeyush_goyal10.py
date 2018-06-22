# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:45:13 2018

@author: Peeyuh goyal
"""

l1=input("Enter comma saperated no.s")
l2=list(l1)
a=0
count=0
while a<len(l2):
    if l2[a]==13:
        a+=1
    elif l2[a-1]!=13:
        count=count+l2[a]
        a+=1
    else:
        a+=1

print count