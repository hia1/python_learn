# -- coding: utf-8 --
# -- coding: utf-8 --
import time

import easyocr
import pytesseract
from PIL import Image
from selenium import webdriver
import requests
from selenium.webdriver.support import expected_conditions as EC
#古诗文网登陆验证码验证
from selenium.webdriver.support.wait import WebDriverWait

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
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get(target_url)
    driver.implicitly_wait(1)

    def login():
        onclick_element = driver.find_element_by_link_text("我的")
        onclick_element.click()
        # 获取cookides
        before_cookies = driver.get_cookies()
        print(before_cookies)
        img_path = "../crawler/picLibs/imgCode.png"
        img_code = driver.find_element_by_id("imgCode")
        img_url = img_code.get_attribute("src")
        img_code.screenshot(img_path)
        time.sleep(2)
        # 写入本地
        img = get_img(img_path)
        img_gray = image_grayscale_deal(img)
        img_process = image_threashoding_method(img_gray)
        # pytresseract库识别验证码
        code_text = captcha_crack(img_process)
        print(code_text)
        #用开源 easyocr库识别验证码
        # reader=easyocr.Reader(["ch_sim","en"])
        # result=reader.readtext(img_path,detail=0)
        # code_text=result[0]
        # print(result[0])

        time.sleep(1)
        # 输入账号
        username_ele = driver.find_element_by_id("email")
        username_ele.send_keys(username)
        # 输入密码
        password_ele = driver.find_element_by_id("pwd")
        password_ele.send_keys(password)
        # 输入验证码
        code_ele = driver.find_element_by_id("code")
        code_ele.send_keys(code_text)
        time.sleep(1)
        print("输入完成")

    login()
    # 检查验证码错误弹窗
    while True:
        login_alert = EC.alert_is_present()(driver)
        if (login_alert):
            print("弹窗", login_alert.text)
            print("验证失败")
            time.sleep(2)
            login_alert.accept()
            login()
        else:
            print("验证成功")
            after_cookies=driver.get_cookies()
            print(after_cookies)
            break

    #点击登录
    # login_ele=driver.find_element_by_xpath('//*[@id="denglu"]')
    # login_ele.click()
    time.sleep(2)
    assert driver.title=="我的收藏_古诗文网","期望是，{}".format(driver.title)
    assert driver.find_element_by_link_text("退出登录")
    print("密码登录测试成功")
    driver.quit()

    #验证登陆跳过验证码
    driver=webdriver.Chrome(executable_path=driver_path)
    driver.get(url="https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx")
    time.sleep(2)
    #删除cookies
    driver.delete_all_cookies()
    for cookie in after_cookies:
        if "expiry" in cookie.keys():
            cookie.pop("expiry")
        driver.add_cookie(cookie)
    time.sleep(2)
    driver.refresh()
    time.sleep(2)
    assert driver.find_element_by_link_text("退出登录")
    print("跳过验证码登录测试通过")

except Exception as e:
    print(e)
finally:
    driver.quit()
