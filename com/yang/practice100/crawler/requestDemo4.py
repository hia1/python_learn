# -- coding: utf-8 --

'''爬取豆瓣排行版'''
import json

import requests
from bs4 import BeautifulSoup

from crawler.util.HandleConfig import HandleConfig

handle = HandleConfig("util/headers.ini")
user_agent = handle.get("request", "User-Agent")
print(user_agent)


# 获取url
url = handle.get("request", "doubanTop")

# 反爬
ua = handle.get("request", "user-agent")
ua = eval(ua)  # 字符串转字典
# post请求
res = requests.get(url, headers=ua)
res_content = res.content
res.encoding = res.apparent_encoding
res_text = res.text

bs = BeautifulSoup(res_content, "html.parser")
menu_tag = bs.find_all("div", class_="types")[0]
# print(menu_tag) #获取类型列表
#定义电影类型，id，排序
select_type = "动作"
select_id=""
for item in menu_tag.find_all("a"):
    movie_action = item.get_text()
    movie_type = item.get("href")
    if "https://movie.douban.com/" not in movie_type:
        movie_type = "https://movie.douban.com/" + movie_type
    movie_sorted = movie_type.split("id=")[1].split("&")[0]  # 电影前排行百分比
    if select_type==movie_action:
        #匹配对应电影类型，获取ID
        select_id=movie_type_id
    movie_type_id = movie_type.split("type=")[1].split("&")[0]
    print( movie_action, movie_sorted, movie_type_id)

select_url="https://movie.douban.com/j/chart/top_list"
query_params ={
    'type': select_id,
    'interval_id': '100:90',
    'action':'',
    'start': '0',
    'limit': '30'
 }

movie_resposne = requests.get(url=select_url, params=query_params, headers=ua)
movie_resposne_json= movie_resposne.json()
print(movie_resposne_json)
#保存json文件
with open(select_type + ".json", "w", encoding="utf-8") as fp:
    json.dump(movie_resposne_json,fp=fp,ensure_ascii=False,indent=4)
movie_top={}
for i in movie_resposne_json:
    movie_name=i["title"]
    movie_namescore=i["score"]
    movie_top.update({movie_name:movie_namescore})
#获取豆瓣排行并生成字典
print(len(movie_top),movie_top)

