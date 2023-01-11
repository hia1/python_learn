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

#验证码灰度处理，消除线条影响
def image_grayscale_deal(image):
    img=image.convert("L")
    # img.show()
    return img

#验证码二值化处理
def image_threashoding_method(image):
    threshold = 160
    table=[]
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image=image.point(table,"1")
    # image.show()
    return image

#pytresseract库识别
def captcha_crack(image):
    result=pytesseract.image_to_string(image)
    return result

try:
    driver=webdriver.Chrome(executable_path=driver_path)
    driver.get(target_url)
    driver.implicitly_wait(1)
    onclick_element=driver.find_element_by_link_text("我的")
    onclick_element.click()
    img_path = "../crawler/picLibs/imgCode.png"
    img_code=driver.find_element_by_id("imgCode")
    img_url=img_code.get_attribute("src")
    #获取验证码,验证码会刷新，出错
    # print(img_url)
    # img_data=requests.get(img_url,headers=UA).content
    # print(img_data)
    # with open(img_path,"wb") as fp:
    #     fp.write(img_data)
    #截图验证码
    img_code.screenshot(img_path)
    time.sleep(2)
    #写入本地
    img=get_img(img_path)
    img_gray=image_grayscale_deal(img)
    img_process=image_threashoding_method(img_gray)
    # with open(img_path,"wb") as fb:
    #     fb.write(img_process)

    #教程使用pytresseract库识别，需要下载exe文件和中文包
    text=captcha_crack(img_process)
    print(text)
    #使用开源 easyocr 库 初次运行需要在线下载检测模型和识别模型，建议在网速好点的环境运行
    # reader=easyocr.Reader(["ch_sim","en"])
    # result=reader.readtext(img_path,detail=0)
    # print(result[0])



except Exception as e:
    print(e)
finally:
    driver.quit()

