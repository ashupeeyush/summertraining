# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:39:36 2018

@author: Peeyuh goyal
"""

str1= raw_input()

str2=list(str1)




def Translate(str):
    s=list("aeiou ")
    str3=""
    for i in str:
        if i not in s:
            str3=str3+i+"o"+i
        else:
            str3=str3+i
    return str3
            
            
Translate(str2)
    
    
    
    
    
    
    
    
    
    
    

