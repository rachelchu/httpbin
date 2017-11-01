# -*- coding:utf-8 -*-
#Get method: headers, param

import requests
import json
import glob,os

host = "http://httpbin.org/"
endpoint = "get"

url = ''.join([host,endpoint])
headers = {"User-Agent":"test request headers"}
params = {"show_env":"1"}
r = requests.get(url=url,headers=headers,params=params)

print (r.text)
print ((eval(r.text))['headers']['User-Agent'])

