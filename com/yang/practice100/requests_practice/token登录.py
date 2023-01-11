# -- coding: utf-8 --
import requests


headers={}
loginData={}
loginurl=''
s=requests.session()
login_resp =s.post(url=loginurl,headers=headers,data=loginData)
# 这里token在返回的json里，可以直接提取
token=login_resp.json()['token']
#登陆后访问url
post_url=''
#token添加到请求头
headers['token']=token
body={}
post_resp=s.post(post_url,headers=headers,data=body)
print(post_resp.content)