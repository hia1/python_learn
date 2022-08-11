# -- coding: utf-8 --
import json

import requests

from crawler.util.HandleConfig import HandleConfig

handle = HandleConfig("util/headers.ini")
user_agent = handle.get("request", "User-Agent")
print(user_agent)


#获取url
url=handle.get("request", "baudu_translate")
#获取翻译单词
query_input=input("please input a word: ")
queryData={"kw":query_input}
#反爬
ua=handle.get("request", "user-agent")
ua=eval(ua)#字符串转字典
#post请求
res=requests.post(url,params=queryData,headers=ua)
res_json=res.json()
filename=query_input+".json"
fp=open(filename,"w",encoding="UTF-8")
json.dump(res_json,fp=fp,ensure_ascii=False,indent=4, sort_keys=True)

# print(res_json["data"][i]["v"] for i in range(len(res_json["data"])-1))
# for i in range(len(res_json["data"])-1):
#     print(res_json["data"][i]["v"])

list1=[res_json["data"][i]["v"] for i in range(len(res_json["data"])-1)]
print(list1)
