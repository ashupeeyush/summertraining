# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:15:58 2018

@author: Peeyush Goyal
"""


from twython import Twython





APP_KEY ="Bl2SljEHeh8LXZ25ZPwGjLOup"
APP_secret= "Mv9lNCFRLapc5YzBTKobFEB8bvWV0N6rrN6zYevnXNmKOmEs4C"
OAUTH_TOKEN= "1330598460-w499snuDclDNAbtPHyOkGGG4t1kcQFccY7o8Hlx"
Oauth_TOKEN_SECRET= "vKmkam6cQJsvd2i4qVbSBlWXIeuelnyPNgiTUMaefPWZE"


twitter = Twython(APP_KEY, APP_secret,OAUTH_TOKEN, Oauth_TOKEN_SECRET)
twitter.update_status(status='At forsk')
