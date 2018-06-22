# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:35:52 2018

@author: Peeyuh goyal
"""
#This program accepts a sequence of comma separated numbers from user and generates a list and tuple with those numbers
Str1= raw_input("enter comma saperated numbers")

l1=Str1.split(",")

print(l1)

T1=tuple(l1)

print T1