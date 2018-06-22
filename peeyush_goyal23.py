# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:29:21 2018

@author: Peeyush Goyal
"""

import facebook as fb

access_token="EAACEdEose0cBANpmM8ZAbm4uFus7zkQtYxnboLaxCIzpGPpcZArhMg1X3FLPhECAqNZAEuR1m8RNDdQXXF4tkZCsJ5jYX2YkZAeEvMCmbpAZCT5Aq76ezzKHPRUHmTESykj3aSL2OZBSZBrrBwoBp5fuPV1W5ZCo7WDnHyYEZAFqtNN3IEkEZCQ8iDwolglprLzz3neikOIGUM12gZDZD"
status= "At trainning"


graph= fb.GraphAPI(access_token=access_token)

post_id= graph.put_wall_post(status)
img="ashu.jpg"
graph.put_photo(image=open(img,'rb'))
