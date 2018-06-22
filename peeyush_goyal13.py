# -*- coding: utf-8 -*-
"""
Created on Tue May 15 13:09:32 2018

@author: Peeyuh goyal
"""

pat=input()

def pattern():
    for item in range(1,pat):
        print item*"*"
    for item in range(pat,0,-1):
        print item*"*"
     


pattern()        
        