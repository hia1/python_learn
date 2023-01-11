# -- coding: utf-8 --

import unittest


class TestModule1(unittest.TestCase):
    def setUp(self) -> None:
        print("start")

    def tearDown(self) -> None:
        print('teardown')

    def test01(self):
        print("11")
        # self.assertEqual(200,401)
    def test02(self):
        print("22")