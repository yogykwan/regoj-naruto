# -*- coding: utf-8 -*-
# -*- by: Yogy Kwan -*-
# -*- Python: 3.4.0 -*-

import urllib.request
import urllib.error
import urllib.parse
import http.cookiejar
import string
import random
import sys

url1=r'http://acm.swjtu.edu.cn/JudgeOnline/problemlist'
url2=r'http://acm.swjtu.edu.cn/JudgeOnline/register'
cj=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPHandler,urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
headers={
    'User-Agent':r'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36',
    'Accept':r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Accept-Encoding':'gzip,deflate,sdch',
    'Connection':'keep-alive',
    'Origin':r'http://acm.swjtu.edu.cn',
    'Referer':r'http://acm.swjtu.edu.cn/JudgeOnline/registerpage',
    'Host':'acm.swjtu.edu.cn',
    'Content-Type':r'application/x-www-form-urlencoded',
    'Cache-Control':'max-age=0\r\n'
}
opener.open(url1)

def getUserid(x):
    name=str(x)
    if len(name)==1: name='00'+name
    elif len(name)==2: name='0'+name
    name=prefix+name
    return name

def getPasswd(length=8,chars=string.ascii_letters+string.digits):
    return ''.join([random.choice(chars) for i in range(length)])

#prefix='yogy_' #prefix of user_id
#tot=100 #the number competitors

prefix=input('prefix of user_id: ')
tot=int(input('the number competitors: '))
filename=input('filename of id/password: ')
file=open(filename,'w+') #file of id and passwd

for i in range(1,tot+1):
    user_id=getUserid(i)
    password=getPasswd(6) #the length of password
    file.write('%s %s\n\r\n\r'%(user_id,password))
    print('%s %s'%(user_id,password))
    postDict={
        'user_id':user_id,
        'nick':user_id,
        'password':password,
        'rptPassword':password,
        'school':'swjtu',
        'email':'',
        'submit':'Submit',
    }
    postData=urllib.parse.urlencode(postDict).encode('utf-8')
    req=urllib.request.Request(url2,postData,headers)
    trytime=0
    while True:
        try:
            resp=opener.open(req)
        except urllib.error.HTTPError:
            trytime+=1
            if trytime>20:
                print('Web Error. Please choose another prefix!')
                sys.exit(0)
            continue
        break
file.close()
