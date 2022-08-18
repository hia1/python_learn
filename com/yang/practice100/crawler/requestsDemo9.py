# -- coding: utf-8 --
'''古诗文验证码识别'''
import os
import time
from multiprocessing import Pool

import requests
from bs4 import BeautifulSoup
from lxml import etree
from crawler.util.HandleConfig import HandleConfig
import re

from crawler.util.verifyCode import recognize

if __name__ == '__main__':

    session=requests.Session()
    handle = HandleConfig("util/headers.ini")
    user_agent = eval(handle.get("request", "User-Agent"))
    proxyIP=eval(handle.get("param", "proxyIP"))

    '''线程池使用代理IP爬取梨视频最热短视频'''
    search_url= "https://www.pearvideo.com/panorama"
    pic_res=session.get(url=search_url, headers=user_agent)
    pic_res.encoding=pic_res.apparent_encoding
    pic_res_text=pic_res.text
    # print(pic_res_text)


    """使用xpath定位li标签，遍历图片href,生成列表，值为视频url和视频名称的字典"""
    src_list=etree.HTML(pic_res_text)
    hot_src_list=src_list.xpath('//*[@id="listvideoListUl"]/li')
    new_src_list=src_list.xpath('//*[@id="categoryList"]/li')
    video_download_list=[]
    def get_videoUrl_list(src_list):
        for hot_src in src_list:

            video_id=hot_src.xpath('./div/a/@href')[0]
            hot_video_detail_url="https://www.pearvideo.com/"+video_id
            hot_video_name=hot_src.xpath('./div/a/div[@class="vervideo-title"]/text()')[0]+".mp4"
            hot_video_name.replace(" ","_")
            # print(hot_video_detail_url,hot_video_name)
            "添加防盗链"
            headers = {"Referer": hot_video_detail_url}
            params = {'contId': video_id.split('_')[-1]}
            url = "https://www.pearvideo.com/videoStatus.jsp"
            video_src_text=requests.get(url=url,params=params,headers=headers)
            video_src_text.encoding=video_src_text.apparent_encoding
            data_dict=video_src_text.json()
            # print(data_dict)
            src_url = data_dict['videoInfo']['videos']['srcUrl']
            systemTime = data_dict['systemTime']
            real_url = src_url.replace(systemTime, 'cont-%s' % video_id.split('_')[-1])
            #打印真实地址
            print("----------------",real_url)
            video_info_dict={
                "video_name":hot_video_name,
                "video_url":real_url
            }
            video_download_list.append(video_info_dict)
    get_videoUrl_list(hot_src_list)
    # get_videoUrl_list(new_src_list)
    print(video_download_list)
    """获取视频对象方法"""
    def get_video_data(dic):
        video_url=dic["video_url"]
        print(dic["video_name"], "download begin")
        video_data=requests.get(url=video_url,headers=user_agent).content
        dir_path="./梨视频"
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        with open(dir_path+"/"+dic["video_name"],"wb") as fp:
            fp.write(video_data)
        print(dic["video_name"],"download complete")

    """创建线程池对象异步下载视频"""
    pool=Pool(4)
    pool.map(get_video_data,video_download_list)
    pool.close()
    pool.join()
