#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'


# from appium import

class Base:
    # @classmethod
    # def setUpClass(cls):
    #     desired_capabilities = {
    #         "platformName": "Android",
    #         "platformVersion": "6.0.1",
    #         "deviceName": "localhost:7555",
    #         "appPackage": "com.tencent.mobileqq",
    #         "appActivity": "com.tencent.mobileqq.activity.LoginActivity",
    #         "NoReset": True
    #     }
    #     # self.username = username
    #     # self.password = password
    #
    #     cls.driver = webdriver.Remote("http://localhost:7555/wd/hub", desired_capabilities)

    # desired_capabilities = {
    #     "platformName": "Android",
    #     "platformVersion": "6.0.1",
    #     "deviceName": "localhost:7555",
    #     "appPackage": "com.tencent.mobileqq",
    #     "appActivity": "com.tencent.mobileqq.activity.LoginActivity",
    #     "NoReset": True
    # }
    # # self.username = username
    # # self.password = password
    #
    # driver = webdriver.Remote("http://localhost:7555/wd/hub", desired_capabilities)
    def __init__(self, driver):
        self.driver = driver

    def locate(self, by, value):
        return self.driver.find_element(by, value)

    def locate2input(self, by, value, text):
        self.driver.find_element(by, value).send_keys(text)

    def click(self, by, value):
        self.driver.find_element(by, value).click()

    def slide(self, start_x, start_y, end_x, end_y, duration=1000):
        size = self.driver.get_window_size()
        x = size["width"]
        y = size["height"]
        self.driver.swipe(start_x=start_x * x, start_y=start_y * y, end_x=end_x * x, end_y=end_y * y, duration=duration)
