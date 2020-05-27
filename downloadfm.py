# coding: UTF-8
# !/usr/bin/python

import urllib
import urllib2
import json
import os
import time
import random
import cookielib


localpath="E:\\m\\"
url="https://douban.fm/j/v2/playlist"

textmod ={'sid':'1480150','client':'s:mainsite|y:3.0','channel':'0','app_name':'radio_website','version':'100','type':'s'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36','Cookie':'flag="ok"; bid=ETgXWca8WcA; dbcl2="2052674:XnoHHJknDCY"; ck=_M0j; _ga=GA1.2.1710167474.1590557785; _gid=GA1.2.1479044468.1590557785'}
textmod['sid']="1548236"

def downloadfm(url,headers,textmod):
	param = urllib.urlencode(textmod)	
	req = urllib2.Request(url = '%s%s%s' % (url,'?',param), headers=headers)
	res = urllib2.urlopen(req)
	res = res.read()
	alm = json.loads(res)
	songs= alm["song"]
	for song in songs:
		url=song["url"]
		filename=song["title"]+"."+song["file_ext"]
		sid=song["sid"]
		textmod['sid']=sid
		try:
			print sid+"-"+unicode(filename)
		except:
			print "ignore..."
		filePath=localpath+filename
		if not os.path.exists(filePath):
			f = urllib2.urlopen(url)
			data = f.read()
			try:
				with open(filePath, "wb") as code:
					code.write(data)
			except:
				print "write file exception ignore it!"
			finally:
				f.close()
	return True

while True:
	downloadfm(url,headers,textmod)

