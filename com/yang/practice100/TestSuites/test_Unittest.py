import time
import unittest

from ddt import ddt, data, unpack

from POM.BASE.BasePage import BasePage
from POM.BASE.Browser_driver import BrowserDriver
from POM.Flow.loginFlow import loginFlow
from POM.Utils.readTestData import readTestData
from POM.pageObjects import GushiwenIndex




#数据驱动-测试数据的参数化
@ddt
class TestCase01(unittest.TestCase):
    driver = BrowserDriver()
    flag=True


    def setUp(self) -> None:
        print("用例执行前执行")
        driver=self.driver.open_browser("Chrome")


        # driver.get("https://www.baidu.com")
        time.sleep(2)

    def tearDown(self) -> None:
        print("用例执行后执行")

    #测试用例方法名需要以test开头,
    @data(*readTestData())
    @unpack #装饰器用来解包的值
    def test_01(self,text,text1):
        print("{}用例运行后执行".format(text))
        print("{}用例运行后执行".format(text1))
        # self.assertEqual(True, False)

    @unittest.skip("skip装饰器用来跳过执行")
    def test_02(self):
        print("test02")


    @unittest.skipIf(1<2,"判断skip装饰器用来跳过执行")
    def test_03(self):
        print("test03")

    def test_04(self):
        print("test04")

    def test_05(self):
        print("test_05")

    def test_06(self):
        print("test_06")
        self.assertEqual(1,2,msg="06terror")


if __name__ == '__main__':
    unittest.main()
