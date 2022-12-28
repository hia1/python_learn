# -- coding: utf-8 --
import unittest

from POM.TestSuites.test_Unittest import TestCase01

test_suite=unittest.TestSuite()


test_suite.addTest(TestCase01("test_03"))
test_suite.addTest(TestCase01("test_05"))
runner=unittest.TextTestRunner()
runner.run(test_suite)
