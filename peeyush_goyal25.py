# -*- coding: utf-8 -*-
"""
Created on Mon May 21 10:51:57 2018

@author: Peeyush Goyal
"""

list1=[]
while True:
    a= raw_input("Enter comma saperated string")
    if not a:
        break
    l1=a.split(",")
    name=l1[0]
    age=l1[1]
    score=l1[2]
    list1.append((name,int(age),int(score)))
list1.sort()
print list1

    