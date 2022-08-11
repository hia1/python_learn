# -- coding: utf-8 --

import os
import time
import requests
from bs4 import BeautifulSoup


class GetGirlImg():
    def __init__(self) -> None:
        self._baseUrl = "https://www.mzitu.com/245734/"
        self._headers = {
            "cookie": None,
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
        }
        self._basePath = "D:/性感图片/"

    def create_folder(self, path):  # 给爬取的图片创建存放文件
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            pass

    def getImgMsg(self):  # 获取图片的信息
        curUrl = self._baseUrl  # 当前图片的网址
        self.create_folder(self._basePath)  # 如果没有对应的图片存放路径,那么创建一个
        for i in range(54):  # 下载54张图片(这是同一个女孩的一组套图,如果读者有心,在这里可以把54改成更大的数,反正该网站有很多图片)
            response = requests.get(url=curUrl, headers=self._headers)  # 爬取出来这个网页的源代码
            soup = BeautifulSoup(response.text, 'lxml')  # 把源代码解析出来
            curImgUrl = soup.select_one(".main-image > p > a > img").attrs["src"]  # 获取这个图片的源文件链接
            self.downloadImg(imgUrl=curImgUrl, filePath=self._basePath)  # 下载这张图片
            curUrl = soup.select_one(".main-image > p > a").attrs["href"]  # 获取这张图片的下一页图片,作为下一次get图片的url

    def downloadImg(self, imgUrl, filePath):
        imgName = str(imgUrl).split('/')[-1]  # 从url中截取出最后的字符作为我们保存图片的文件名
        filePath = filePath + imgName  # 与我们存放图片的基础路径拼接一下
        response = requests.get(url=imgUrl, headers=self._headers)
        if 200 != response.status_code:  # status为200表示正确,为404表示错误
            pass
        else:
            with open(filePath, mode="wb") as f:
                f.write(response.content)  # 向我们预定义的文件中写入获取的图片内容


if __name__ == "__main__":
    image = GetGirlImg()
    image.getImgMsg()