# -- coding: utf-8 --
"""使用正则表达式爬取豆瓣250"""
import csv
import re

import requests

from crawler.util.HandleConfig import HandleConfig

handle = HandleConfig("util/headers.ini")
user_agent = handle.get("request", "User-Agent")
print(user_agent)
user_agent = eval(user_agent)  # 字符串转字典

douban_url="https://movie.douban.com/top250"
res=requests.get(url=douban_url,headers=user_agent)
# res.encoding = res.apparent_encoding
res_text=res.text
# print(res_text)

#生成正则表达式预加载对象
# ex_obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">(?P<director>.*?)&nbsp.*?;&nbsp;(?P<star>.*?)<br>(?P<year>.*?)&nbsp;/&nbsp;(?P<country>.*?)&nbsp;/nbsp.*?<span class="rating_num" preperty="v:average">(?P<score>.*?)</span>.*?<span>(?P<man_num>.*?)人评价</span>.*?<span class="inq">(?P<comment>.*?)</span>',re.S)

ex_obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">(?P<director>.*?)&nbsp;&nbsp;&nbsp;(?P<star>.*?)<br>(?P<year>.*?)&nbsp;/&nbsp;(?P<country>.*?)&nbsp;/&nbsp;(?P<type>.*?)</p>.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<man_num>.*?)人评价</span>.*?<span class="inq">(?P<comment>.*?)</span>',re.S)
result=ex_obj.finditer(res_text)
fp= open("./doubanTop250.csv","w",encoding="utf-8")
csvwriter=csv.writer(fp)
for it in result:
    print(it.group("name"))

    dict=it.groupdict()
    dict["name"]=dict["name"].strip()
    dict["director"]=dict["director"].strip()
    dict["star"]=dict["star"].strip()
    dict["year"]=dict["year"].strip()
    dict["country"]=dict["country"].strip()
    dict["type"]=dict["type"].strip()
    dict["score"]=dict["score"].strip()
    dict["comment"]=dict["comment"].strip()
    csvwriter.writerow(dict.values())
fp.close()
print("over")
