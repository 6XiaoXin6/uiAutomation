#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

import unittest
from time import sleep, time

from ddt import ddt, data, unpack, file_data
from selenium.webdriver.common.by import By

from POM.page_objects.baidu import BaiDu


@ddt
class BaiDuTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # cls.bd = BaiDu(browser="Chrome")
        cls.bd = BaiDu(browser="Chrome")

    def test_10(self):
        self.bd.research("UI自动化")
        sleep(3)
        title = self.bd.driver.title
        text = 'UI自动化_百度搜索'
        assert text == title

    # def setUp(self):
    #     print("正在打开浏览器...")
    #
    # @data("刘亦菲", "刘德华", "蓝洁瑛")
    # def test_0(self, name):
    #     self.bd.research(name)
    #     sleep(3)
    #     text = self.bd.locate(By.LINK_TEXT,
    #                           "更多").text
    #     print(text)
    #     assert text == "更多"
    #
    # @data(("a", 1), ("b", 2))
    # @unpack
    # def test_1(self, char, value):
    #     # self.bd.research("selenium1")
    #     assert value == 1
    #
    # @file_data("../data/research.yaml")
    # @unpack
    # def test_2(self, name, age):
    #     print(name)
    #     print(age)
    #     self.bd.research(name)
    #     sleep(3)
    #     text = self.bd.locate(By.LINK_TEXT,
    #                           "更多").text
    #     print(text)
    #     assert age == 32
    #     assert text == "更多"
    #
    # def test_3(self):
    #     self.bd.research("selenium2")
    #
    #     sleep(3)
    #     text = self.bd.locate(By.LINK_TEXT,
    #                           "更多").text
    #     print(text)
    #     assert text == "Selenium"
    #
    # @unittest.skip("我要跳过")
    # def test_4(self):
    #     print("skip")
    #     # assert text == "Selenium"
    #     assert True
    #
    # @unittest.skipIf(2 > 1, 'ture执行跳过')
    # def test_5(self):
    #     print("no skip")
    #     # assert text == "Selenium"
    #     assert True
    #
    # @unittest.skipUnless(2 < 1, "false执行跳过")
    # def test_6(self):
    #     print("no skip")
    #     # assert text == "Selenium"
    #     assert True
    #
    # @unittest.expectedFailure
    # def test_7(self):
    #     print("no skip")
    #     # assert text == "Selenium"
    #     # assert 1/0
    #     assert 2 < 1
    # # def tearDown(self) -> None:
    # #     print("正在关闭浏览器...")
    # def test_8(self):
    #     # self.bd.research("selenium2")
    #     #
    #     # sleep(3)
    #     # text = self.bd.locate(By.LINK_TEXT,
    #     #                       "更多").text
    #     text='Selenium'
    #     print(text)
    #     assert text == "Selenium"
    #
    # def test_9(self):
    #     # self.bd.research("selenium2")
    #     #
    #     # sleep(3)
    #     # text = self.bd.locate(By.LINK_TEXT,
    #     #                       "更多").text
    #     text='Selenium'
    #     print(text)
    #     assert text == "Selenium"
