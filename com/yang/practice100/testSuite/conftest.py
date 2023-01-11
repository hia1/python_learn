# -- coding: utf-8 --
import time

import pytest
from py.xml import html
from selenium import webdriver
import base64

driver=None
#截图base64


@pytest.fixture(scope="function",autouse=True)
def browser(request):
    global driver
    driver_path=r'F:\pythonLearn\com\yang\practice100\POM\Utils\driver\chromedriver.exe'
    if driver is None:
        driver =webdriver.Chrome(executable_path=driver_path)
    def end():
        driver.quit()
    request.addfinalizer(end)
    return driver

#截图方法
def _capture_screenshot():
    if driver is not None:
        return driver.get_screenshot_as_base64()
    else:
        print("browrser auto设置为false，driver获取异常")
@pytest.fixture()
def login():
    print("输入账号密码")
    print("完成输入")
    # yield后执行用例
    yield
    print("退出登录")


@pytest.fixture()
def clear():
    print('清除用例数据内容！！')

@pytest.fixture()
def quit_browser():
    print('退出浏览器！！')


@pytest.fixture(autouse=True) ##autouse=True 指定默认作用域fixture的测试函数均执行
def back_index():
    print("返回首页，准备执行用例")
    yield
    print("执行完成")

def pytest_html_report_title(report):
    report.title="web自动化测试报告"

def pytest_configure(config):
    config._metadata["项目名称"]="测试demo"
    #删除java——home
    config._metadata.pop("JAVA_HOME")

@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("测试模块")])
    prefix.extend([html.p("测试人员")])


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item,call):
    pytest_html=item.config.pluginmanager.getplugin("html")
    outcome=yield
    report=outcome.get_result()
    extra=getattr(report,'extra',[])
    #截图操作
    if report.when == 'call':
        screen_img=_capture_screenshot()
        time.sleep(2)
        if screen_img is not None:
            html='<div><img src="data:image/png;base64,%s" alt="screenshot" stytle="width:600px;height:500px" align="right" /></div>' %screen_img
            extra.append(pytest_html.extras.html(html))
        report.extra=extra

