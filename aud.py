#!/usr/bin/python 
 
import HTMLParser 
import urlparse 
import urllib 
import urllib2 
import cookielib 
import string 
import re 
 
hosturl = 'http://manage.aud.dx.com/' 

posturl = 'http://manage.aud.dx.com/user/login'

synurl = 'http://manage.aud.dx.com/product/auto_dxsyn' 

cj = cookielib.LWPCookieJar() 
cookie_support = urllib2.HTTPCookieProcessor(cj) 
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler) 
urllib2.install_opener(opener) 
 
 
h = urllib2.urlopen(hosturl) 
 
 
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1', 
           'Referer' : '******'} 

postData = {'username' : 'admin', 
            'password' : '' 
 
            } 
 
postData = urllib.urlencode(postData) 
 

request = urllib2.Request(posturl, postData, headers) 
print request 
response = urllib2.urlopen(request) 
text = response.read() 
print text 

 

response = urllib2.urlopen(synurl)
html = response.read()