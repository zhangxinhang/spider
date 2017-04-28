# -*- coding: UTF-8 -*-     
import requests
import json
import urllib

headers = {}
payload = {"corpcode":"xxx","username":"xxx","password":"xxx","source":"xxx"}
r = requests.post("xxx", data=json.dumps(payload))
r.encoding = 'utf-8'
ret = json.loads(r.text)
aa = ret['message']['personnelName']
print aa
headers = {
 
}
#针对中文header的处理存在问题
#print urllib.quote(aa,'utf-8')

pr = requests.get('xxx',headers=headers)
pr.encoding = 'utf-8'
ret = json.loads(pr.text)
print pr.text