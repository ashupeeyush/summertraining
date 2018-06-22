# -*- coding: utf-8 -*-
"""
Created on Thu May 17 11:18:20 2018

@author: Peeyush Goyal
"""
import string
str1= raw_input("enter a string")
str2=list(str1)
str3=list(string.ascii_lowercase)
def pangram(str2):
    
    for i in str2:
        if i in str3:
            str3.remove(i)
    if not str3:
        return "Pangram"
    else:
        return "Not Pangram"
pangram(str2)    

str1= raw_input("enter a string")            
count=0  
st=set(str1)
for i in st:
    if(i>='a' and i<='z'):
        count+=1
if count == 26:
    print "Pangram"
else:
    print "Not Pangram"

          
    