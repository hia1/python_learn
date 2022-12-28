# -- coding: utf-8 --

import unittest


class TestModule2(unittest.TestCase):
    def setUp(self) -> None:
        print("start")

    def tearDown(self) -> None:
        print('teardown')

    def test01(self):
        print("1")

    def test02(self):
        print("2")