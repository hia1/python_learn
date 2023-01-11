# -- coding: utf-8 --

import time
from selenium import webdriver
#加载浏览器驱动路径
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by  import By

driver_path="F:\SoftwareTest\chromedriver.exe"
#打开浏览器
driver=webdriver.Chrome(executable_path=driver_path)
#打开网页
driver.get("https://www.baidu.com")
sendkeys="新闻"
#定位网页元素
#操作网页元素
# input_key=driver.find_element_by_id("kw")

# driver.find_element("name","wd").send_keys(sendkeys)
# driver.find_element_by_class_name("s_ipt").send_keys(sendkeys)
# driver.find_element_by_tag_name()
#针对文本链接
# driver.find_element_by_link_text()
# 链接模糊匹配，多个为匹配第一个
# input_key=driver.find_element_by_partial_link_text()

#元素层级查找
# input_key=driver.find_element_by_xpath('//*[@id="kw"]')

input_key=driver.find_element_by_css_selector('#kw')
input_key.send_keys(sendkeys)


#隐式等待，设置最长等待时间，如果网页加载完成，即可执行，更加灵活
driver.implicitly_wait(2)

driver.find_element_by_id("su").click()
# 显式等待，强制等待时间网页刷新，相对耗时，不建议
# time.sleep(1)
try:
    locator=(By.XPATH,'//*[@id="2"]/div/div[1]/h3/a')
    # WebDriverWait显示等待
    WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located(locator))
    print("元素已经查找到")
    #断言-验证
    assert driver.title==sendkeys+"_百度搜索","断言错误，实际为"+driver.title
    print("pass")

    # 查找页面多个元素
    # key_list=driver.find_elements_by_xpath('//*[@class="rs-link_2DE3Q c-line-clamp1 c-color-link"]')
    # print(len(key_list))
    # for i in range(len(key_list)-1):
    #     #查找页面多个元素需要在循环内加入元素查找，不然会报异常
    #     key_list=driver.find_elements_by_xpath('//*[@class="rs-link_2DE3Q c-line-clamp1 c-color-link"]')
    #     key_list[i].click()
    #     time.sleep(1)
    #     print("test pass")
    #     # 网页回退
    #     driver.back()

    #多窗口控制_窗口句柄，handle标识窗口属性
    driver_find=driver.find_element_by_xpath('//*[@id="2"]/div/div/div[2]/div[1]/div[2]/div/a')
    driver_find.click()
    handle=driver.current_window_handle
    print("当前页面handle:{},title:{}".format(handle,driver.title))
    handles=driver.window_handles
    print("当前handles列表{}".format(handles))
    #切换窗口
    driver.switch_to.window(handles[1])
    handle=driver.current_window_handle
    time.sleep(2)

    print("切换后的窗口handle:{}".format(driver.title))
    print("切换后页面handle:{},title:{}".format(handle, driver.title))
    time.sleep(2)
    driver.close()
    driver.switch_to.window(handle)
    print("关闭后剩余的title:{}".format(driver.title))

    #多窗口打开控制——window.handles 为堆栈方式，先进后出



except Exception as e:
    print("{},元素不存在".format(e))
finally:

    # 关闭浏览器
    driver.quit()
