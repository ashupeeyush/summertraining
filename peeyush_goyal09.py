# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:45:13 2018

@author: Peeyuh goyal
"""

l1=input("Enter comma saperated no.s")
l2=list(l1)

l2.sort()

a=1
count=0
sum=0
while a<len(l2)-1:
    sum=sum+l2[a]
    count+=1
    a+=1
    
print sum/count