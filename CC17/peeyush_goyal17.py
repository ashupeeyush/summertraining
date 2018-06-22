# -*- coding: utf-8 -*-
"""
Created on Wed May 16 12:05:51 2018

@author: Peeyuh goyal
"""

from PIL import Image
 

img= Image.open("E:\conda\sample.jpg")
img = img.convert('L')
img = img.rotate(-90)
img = img.crop((46,27,206,231))


img.thumbnail((75,75))
sr=raw_input("Enter name:")
img.show()


img.save(sr+".jpg")




