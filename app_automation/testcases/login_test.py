#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

import pytest
from appium import webdriver

from app_automation.object_pages.login_page import LoginPage


class TestLogin():

    def test_login(self):
        desired_capabilities = {
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "deviceName": "localhost:7555",
            "appPackage": "com.tencent.mobileqq",
            "appActivity": "com.tencent.mobileqq.activity.LoginActivity",
            "NoReset": False
            # "NoReset": True
        }
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
        driver.implicitly_wait(7)

        lp = LoginPage(driver)
        lp.login()


if __name__ == '__main__':
    pytest.main()
