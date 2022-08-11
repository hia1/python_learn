# -- coding: utf-8 --
'''使用xpath解析4k图片下载'''
import os
import requests
from bs4 import BeautifulSoup
from lxml import etree
from crawler.util.HandleConfig import HandleConfig
import re

handle = HandleConfig("util/headers.ini")
user_agent = handle.get("request", "User-Agent")
print(user_agent)
user_agent = eval(user_agent)  # 字符串转字典
pic_url="https://pic.netbian.com/4kmeinv/"
pic_res=requests.get(url=pic_url,headers=user_agent)
pic_res.encoding=pic_res.apparent_encoding
pic_res_text=pic_res.text
# print(pic_res_text)


# if not os.path.exists("../picLibs/biantuwang/"):
#     os.mkdir("./picLibs/biantuwang/")

# tree_html=etree.HTML(pic_res_text)
# pic_list=tree_html.xpatn('//div[@class="slist"]/ul/li')
# print(pic_list)
'''使用正则表达式爬取图片'''
def reCrawler():
    src_ex='<a href=.*?<img src="(.*?)" alt.*?</a>'
    imgsrc_list=re.findall(src_ex,pic_res_text,re.S)
    name_ex='<a href=.*?<img src=.*? alt="(.*?)"'
    imgname_list = re.findall(name_ex, pic_res_text, re.S)
    # print(imgsrc_list)
    # print(imgname_list)
    soup=BeautifulSoup(pic_res_text,"lxml")
    #使用bs4找到页码位置
    page_list=soup.select('.page >a')
    print(page_list)
    for page in page_list:
        page_url="https://pic.netbian.com/"+page["href"]
        print(page_url)
    if len(imgname_list)==len(imgsrc_list):
        for index in range(len(imgsrc_list)-1):
            img_url = "https://pic.netbian.com/" + imgsrc_list[index]
            img_data=requests.get(img_url,headers=user_agent).content
            file_name = imgname_list[index].replace(" ", "_")
            with open("./picLibs/biantuwang/" + file_name + ".jpg", "wb") as fp:
                # fp.write(img_data)
                print(file_name+".jpg","写入完成")
    else:
        print(len(imgname_list), len(imgsrc_list))
        print("正则表达式不正确")


reCrawler()