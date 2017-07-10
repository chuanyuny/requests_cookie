#-*- coding:utf-8 -*-
'''request 发送cookie'''
import requests

f=open('a.txt','r') #a.txt是要访问网站的cookie
cookies={}
for line in f.read().split(';'):
	name,value=line.strip().split('=',1)
	cookies[name]=value

res=requests.get("http://test.hackdata.cn/practice/",cookies=cookies)
print res.text