# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:27:57 2018

@author: Peeyush Goyal
"""
import requests

URL="http://13.127.155.43/api_v0.1/sending"
URL2="http://13.127.155.43/api_v0.1/receiving?Phone_Number=9239120013"
p=requests.post(url = URL,json={"Phone_Number":"9239120013","Name":"Peeyush","College_Name":"skit","Branch":"it"})
print p.text

r=requests.get(URL2)

print r.text
