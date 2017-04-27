# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
from bs4 import BeautifulSoup
import codecs

url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/13/1301.html'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response.read(),"html.parser")
    #items = soup.find_all(href=re.compile("html"))
    
    for tag in soup.find_all(class_=re.compile("countytr")):
        tempdata = []
        temphref = ''
        for itag in tag.children:
            if itag.a:
                temphref = itag.a['href']
            tempdata.append(itag.get_text())
        #title.get_text().isdigit()
        aa = {
            'code':tempdata[0],
            'name':tempdata[1]
        }
        print aa
        with codecs.open('G:/hello.csv', 'a','utf-8') as f:
            f.write(aa['code']+","+aa['name']+"\n")
    #print soup.title;
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
