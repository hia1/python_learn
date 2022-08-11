# -- coding: utf-8 --
"""使用正则表达式爬取pixabay图片"""

import requests

from crawler.util.HandleConfig import HandleConfig

handle = HandleConfig("util/headers.ini")
user_agent = handle.get("request", "User-Agent")
print(user_agent)
user_agent = eval(user_agent)  # 字符串转字典

piaxbay_url="https://pixabay.com/zh/"
res=requests.get(url=piaxbay_url,headers=user_agent)
# res.encoding = res.apparent_encoding
res=res.text
print(res)
with open("./piaxbay.html","w",encoding="utf-8") as fp:
    fp.write(res)