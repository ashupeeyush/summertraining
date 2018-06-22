# -*- coding: utf-8 -*-
"""
Created on Tue May 15 10:13:42 2018

@author: Peeyuh goyal
"""

l1 = input("Enter comma saperated 3 no.s")
l2=list(l1)

def Check():
    if l2[2]/5<=l2[1]:
        if (l2[2]%5)<=l2[0]:
            return "True"
        else:
            return "False"
    else:
        return "False"
    
print Check()
