# -*- coding: utf-8 -*-
"""
Created on Fri May 18 11:19:17 2018

@author: Peeyush Goyal
"""

import oauth2
import time 
import urllib2
import json

params = {
        "oauth_version": "1.0",
        "oauth_nonce": oauth2.generate_nonce(),
        "oauth_timestamp": int(time.time())
    }

params["q"] ="Jaipur"
url1 = "https://api.twitter.com/1.1/search/tweets.json"
consumer=oauth2.Consumer(key ="Bl2SljEHeh8LXZ25ZPwGjLOup",secret= "Mv9lNCFRLapc5YzBTKobFEB8bvWV0N6rrN6zYevnXNmKOmEs4C")
token=oauth2.Token(key= "1330598460-w499snuDclDNAbtPHyOkGGG4t1kcQFccY7o8Hlx",secret= "vKmkam6cQJsvd2i4qVbSBlWXIeuelnyPNgiTUMaefPWZE")

req = oauth2.Request(method="GET", url=url1, parameters=params)
signature_method = oauth2.SignatureMethod_HMAC_SHA1() 
req.sign_request(signature_method, consumer, token)
url = req.to_url()
response = urllib2.Request(url)
data = json.load(urllib2.urlopen(response))

filename = params["q"]      
f = open(filename + "_File.txt", "w") 
json.dump(data["statuses"], f)
f.close()


