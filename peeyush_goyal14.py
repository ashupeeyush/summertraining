# -*- coding: utf-8 -*-
"""
Created on Tue May 15 12:22:49 2018

@author: Peeyuh goyal
"""

str1= input()


def fix_teen(n):
    count=0
    for i in str1.values():
         if (i not in range(13,15)) and i not in range(17,20):
              count= count+i
 
    return count  



print fix_teen(3)  