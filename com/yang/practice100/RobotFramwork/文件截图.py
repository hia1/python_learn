# -- coding: utf-8 --
# -- coding: utf-8 --

import time
import base64
from selenium import webdriver
# 加载浏览器驱动路径
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver_path = r"F:\SoftwareTest\chromedriver.exe"
# 打开浏览器
driver = webdriver.Chrome(executable_path=driver_path)
# 打开网页
driver.get("https://www.baidu.com")
sendkeys = "新闻"
input_key = driver.find_element_by_css_selector('#kw')
input_key.send_keys(sendkeys)


# 隐式等待，设置最长等待时间，如果网页加载完成，即可执行，更加灵活
driver.implicitly_wait(2)

driver.find_element_by_id("su").click()
# 显式等待，强制等待时间网页刷新，相对耗时，不建议
# time.sleep(1)
try:
    locator = (By.XPATH, '//*[@id="2"]/div/div[1]/h3/a')
    # WebDriverWait显示等待
    WebDriverWait(
        driver, 10).until(
        expected_conditions.presence_of_element_located(locator))
    print("元素已经查找到")
    # 断言-验证
    assert driver.title == sendkeys + "_百度搜索", "断言错误，实际为" + driver.title
    print("pass")
    # 截图方法1
    time.sleep(2)
    picture1 = driver.get_screenshot_as_file("../crawler/picLibs/picture1.png")
    print("截图 %s" % picture1)
    driver.back()
    time.sleep(2)
    # 截图方法2
    picture2 = driver.save_screenshot("../crawler/picLibs/picture2.png")
    print("截图 %s" % picture2)

    #base64截图
    picture_base64=driver.get_screenshot_as_base64()
    print(picture_base64)
    time.sleep(2)
    pictureBase=base64.b64decode(picture_base64)
    fp=open("../crawler/picLibs/base.png","wb")
    fp.write(pictureBase)
    fp.close()






except Exception as e:
    print("{},元素不存在".format(e))
finally:

    # 关闭浏览器
    driver.quit()
