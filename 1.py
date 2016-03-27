#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/'+str(page)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
headers = {'User-Agent':user_agent}

req = urllib2.Request(url,headers=headers)
res = urllib2.urlopen(req)
print res.read()
