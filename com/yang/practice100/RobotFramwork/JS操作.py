# -- coding: utf-8 --
import time

import easyocr
import pytesseract
from PIL import Image
from selenium import webdriver
import requests
#古诗文网登陆验证码验证

username="424484631@qq.com"
password="YZY961201"
UA={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
target_url="https://www.gushiwen.cn/"
driver_path = r"F:\SoftwareTest\chromedriver.exe"

#获取img
def get_img(img_path):
    img=Image.open(img_path)
    return img
driver=webdriver.Chrome(executable_path=driver_path)
try:
    driver.get(target_url)
    print(driver.current_url)
    # driver.implicitly_wait(1)
    time.sleep(2)
    search_js='document.querySelector("body > div.main3 > div.right > div:nth-child(1) > img").style.display=="none"'
    driver.execute_script(search_js)
    time.sleep(5)
    #拖动滚动条
    scroll_ctrl='window.scrollTo(0,document.body.scrollHeight)'
    driver.execute_script(scroll_ctrl)


except Exception as e:
    print(e)
finally:
    driver.quit()

