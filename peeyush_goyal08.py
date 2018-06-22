# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:28:35 2018

@author: Peeyuh goyal
"""

str1=raw_input()

l1= list(str1)
letter=0
digit=0
for a in l1:
    if a.isdigit():
       digit+=1
    else:
        letter+=1


print "digit",digit

print "letter",letter