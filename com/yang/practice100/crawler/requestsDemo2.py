# -- coding: utf-8 --
import requests

from crawler.util.HandleConfig import HandleConfig

handle = HandleConfig("util/headers.ini")
user_agent = handle.get("request", "User-Agent")
print(user_agent)



url=handle.get("request", "requesturl")
queryData=handle.get("param","query")
#字符串转字典

queryData=eval(queryData)
ua=handle.get("request", "user-agent")
ua=eval(ua)
res=requests.get(url,params=queryData,headers=ua)
res.encoding=res.apparent_encoding
res_text=res.text


file_name="query.html"
with open(file_name,"w",encoding="UTF-8") as fp:
    fp .write(res_text)


print(res_text)