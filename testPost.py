# -*- coding:utf-8 -*-

import requests
import json

host = "http://127.0.0.1:8000/"
endpoint = "post"

url = ''.join([host,endpoint])
data = {'key1':'value1','key2':'value2'}

r = requests.post(url,data=data)
print (r.text)
print r.url