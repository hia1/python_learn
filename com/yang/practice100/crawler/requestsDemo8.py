# -- coding: utf-8 --
# -- coding: utf-8 --
'''古诗文验证码识别'''
import os
import requests
from bs4 import BeautifulSoup
from lxml import etree
from crawler.util.HandleConfig import HandleConfig
import re

from crawler.util.verifyCode import recognize


session=requests.Session()
handle = HandleConfig("util/headers.ini")
user_agent = handle.get("request", "User-Agent")
print(user_agent)
user_agent = eval(user_agent)  # 字符串转字典
pic_url="https://so.gushiwen.cn/user/login.aspx?from=https://www.gushiwen.cn/"
pic_res=session.get(url=pic_url,headers=user_agent)
# pic_res.encoding=pic_res.apparent_encoding
pic_res_text=pic_res.text
# print(pic_res_text)

def verifyCode(res,url,xpath_ex,pic_path):
    tree=etree.HTML(res)
    code_url=url+tree.xpath(xpath_ex)[0]
    print(code_url)
    code_src=requests.get(url=code_url,headers=user_agent)
    with open(pic_path,"wb") as fp:
        fp.write(code_src.content)
        print("code.jpg","写入完成")


#解析验证码
verifyCode(pic_res_text,"https://so.gushiwen.cn/",'//*[@id="imgCode"]/@src',"./picLibs/codeLib/code.jpg")
code=recognize("./picLibs/codeLib/code.jpg",4)

#模拟登录古诗词网
login_url="http://so.gushiwen.cn/user/collect.aspx"
data={
    '__VIEWSTATE': '4ulEqrNwZnXOvUghf17XWl45jKpZOX+rqR/9xxMA3msmFQRg4CKphnCfCQLZRfIx6qcFzkuRg/HOySuYoIOOGnTjMdG3JswcEARCIUpoDeJ+iaGlnCJ+1Q20z0i4oE/7kaEZu1yu6VqSH3tO5fU/o0macMM=',
    '__VIEWSTATEGENERATOR': 'C93BE1AE',
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '424484631@qq.com',
    'pwd': 'YZY961201',
    'code': code,
    'denglu': '登录'
}


response=session.post(url=login_url,headers=user_agent,data=data)
status=response.status_code
print(status)
response.encoding=response.apparent_encoding
res_text=response.text
download_path="./download"
if not os.path.exists(download_path):
    os.makedirs(download_path)
with open(download_path+"/login1.html","w",encoding="utf-8") as fp:
    fp.write(res_text)
# print(res_text)








