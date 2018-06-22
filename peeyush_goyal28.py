# -*- coding: utf-8 -*-
"""
Created on Mon May 21 13:18:30 2018

@author: Peeyush Goyal
"""
web=""

list1=[]
while True:
    e=0
    w=0
    n=0
    a= raw_input()
    if not a:
        break
    if a.count("@")==1:
        l1=a.split("@")
    else:
        continue
    l=l1[1]
    l0=l1[0]
    if l.count(".")==1:
        l2=l1[1].split(".")
    else:
        continue
    web=l2[0]
    web2=l2[1]
    if len(web2)<=3:
        e=1
        if web.isalnum():
            w=1
            for key in l0:
                if key.isalnum() or key=="_" or key=="-":
                    n+=1
    if all([e==1,w==1,n==len(l0)]):
        list1.append(a)
            
list1.sort()
print list1
   