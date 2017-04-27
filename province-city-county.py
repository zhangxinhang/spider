# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
from bs4 import BeautifulSoup
import codecs

class PCC:
  """docstring for PCC"""
  def __init__(self):
    self.base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/'
    self.current_url='http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/index.html'
    self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    #初始化headers
    self.headers = { 'User-Agent' : self.user_agent }
    #存放数据
    self.datas = []
    self.grade = 1


  def writeToCVS(self,obj):
    with codecs.open('G:/pcc.csv', 'a','utf-8') as f:
        f.write(obj['code']+","+obj['name']+"\n")

  def getPageData(self,url):
    try:
        url = self.base_url+url
        #构建请求的request
        request = urllib2.Request(url,headers = self.headers)
        #利用urlopen获取页面代码
        response = urllib2.urlopen(request)
        #将页面转化为UTF-8编码
        pageData = response.read()
        return pageData

    except urllib2.URLError, e:
        if hasattr(e,"reason"):
            print u"connect error",e.reason
            return None
    
  def getAllData(self,url):
    pageData = self.getPageData(url)
    
    if not pageData:
        print "page loding...."
        return None
    soup = BeautifulSoup(pageData,"html.parser")
    for field in soup.find_all(href=re.compile("html")):
        city_href = field['href'];
        tempObj = {
          'code':city_href,
          'name':field.get_text()
        }
        print tempObj
        self.writeToCVS(tempObj)
        self.getCityData(field['href'],'citytr')
    return self.datas

  def getCityData(self,url,type):
    pageData = self.getPageData(url)
    
    if not pageData:
        print "page loding...."
        return None
    soup = BeautifulSoup(pageData,"html.parser")
    for tag in soup.find_all(class_=re.compile(type)):
        tempdata = []
        temphref = ''
        for itag in tag.children:
          if itag.a:
            temphref = itag.a['href']
          tempdata.append(itag.get_text())
        tempObj = {
            'code':tempdata[0],
            'name':tempdata[1]
        }
        print tempObj
        self.writeToCVS(tempObj)
        if type =='citytr' and temphref != '':
          self.getCityData(temphref,'countytr')
    return self.datas

spider = PCC()
spider.getAllData('index.html')