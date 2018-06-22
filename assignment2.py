# -*- coding: utf-8 -*-
"""
Created on Thu May 31 21:35:27 2018

@author: Peeyush Goyal
"""

from bs4 import BeautifulSoup
import requests

Zodiac=raw_input("Enter your Zodiac name")

url = "https://www.astrology.com/horoscope/daily/"+Zodiac+".html"


r  = requests.get(url)

data = r.text
soup = BeautifulSoup(data, 'html.parser')
right=soup.find_all("p")
print right[0].text


