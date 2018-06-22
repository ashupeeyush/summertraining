# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 11:01:20 2018

@author: Peeyush Goyal
"""

from havenondemand.hodclient import *
import json
import pandas as pd

client = HODClient("23e40f14-51b2-4478-8769-78a01c9397bf", "v1") #apikey

#params = {'url': 'https://www.havenondemand.com/sample-content/videos/gb-plates.mp4', 'source_location': 'GB'} ##if using url
params = {'file': 'E:\conda\car_plate.mp4', 'source_location': 'IN'} ## or if using a local file
response_async = client.post_request(params, 'recognizelicenseplates', async=True)
jobID = response_async['jobID']
#print jobID

## Wait some time afterwards for async call to process...

response = client.get_job_result(jobID)
print response

