# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:05:49 2018

@author: Peeyuh goyal
"""
d1={}
str1=raw_input("Enter String")
for letter in set(str1):
     d1[letter] = str1.count(letter)

print d1