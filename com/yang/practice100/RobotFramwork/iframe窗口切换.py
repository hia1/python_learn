# -- coding: utf-8 --
from selenium import webdriver



#页面内嵌窗口 （html内嵌套html。多窗口就是有多个html文件，所以iframe也要窗口切换）
# 1.   driver.switch_to.frame(0)
# 2.   driver.switch_to.frame("iframe的name属性")
# 3.   webElement=driver.find.....先定位元素
#      driver.switch_to.frame(webElement)

driver = webdriver.Chrome()     # 初始化一个浏览器
driver.implicitly_wait(10)      # 设置隐性等待
driver.maximize_window()        # 浏览器窗口最大化

# 1、进入网页
url = 'https://ke.qq.com/'
driver.get(url)      # 打开一个网页

# 2、主页面，点击“登录”按钮
el = driver.find_element('xpath', '//div/a[@id="js_login"]')
el.click()

# 3、切换到 iframe
iframe = driver.find_element('xpath', '//div/div/iframe')
driver.switch_to.frame(iframe)
# 4、点击“账号密码登录”
el = driver.find_element('xpath', '//a[text()="帐号密码登录"]')
el.click()
