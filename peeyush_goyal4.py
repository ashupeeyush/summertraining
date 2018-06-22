# -*- coding: utf-8 -*-
"""
Created on Fri May 11 11:30:40 2018

@author: Peeyuh goyal
"""

str1=raw_input()

str1=str1.strip()
a=str1.find(" ")

print(str1[a+1::]+" "+str1[:a+1:])


