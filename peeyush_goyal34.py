# -*- coding: utf-8 -*-
"""
Created on Wed May 23 13:17:57 2018

@author: Peeyush Goyal
"""

import requests

URL="https://api.mlab.com/api/1/databases/db_university/collections/student?apiKey=WK7iJqbZsfGO_vBz4aA53ZrKUgw-bfb3"

Name=raw_input("enter name")
Age=raw_input("enter Age")
Roll_No=raw_input("enter rollno")
Branch=raw_input("enter branch")
data={
      "Student Name":Name,
      "Student Age":Age,
      "Student Roll No":Roll_No,
      "Student Branch":Branch 
     }
p=requests.post(url = URL,json=data)

print p.text

