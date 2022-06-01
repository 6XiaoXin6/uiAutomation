#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from app_automation.bases.base import Base


# from appium.webdriver import


class LoginPage(Base):
    # desired_capabilities = {
    #     "platformName": "Android",
    #     "platformVersion": "6.0.1",
    #     "deviceName": "localhost:7555",
    #     "appPackage": "com.tencent.mobileqq",
    #     "appActivity": "com.tencent.mobileqq.activity.LoginActivity",
    #     "NoReset": True
    # }
    #
    # driver = webdriver.Remote("http://localhost:7555/wd/hub", desired_capabilities)

    login_btn = (MobileBy.ID, "com.tencent.mobileqq:id/btn_login")
    username_input = (MobileBy.ID, "com.tencent.mobileqq:id/em2", "2585174552")
    password_input = (MobileBy.ID, "com.tencent.mobileqq:id/password", "xyz307322327186")
    login_btn_1 = (MobileBy.ID, "com.tencent.mobileqq:id/login")

    def login(self):
        self.click(*self.login_btn)
        self.locate2input(*self.username_input)
        self.locate2input(*self.password_input)
        self.click(*self.login_btn_1)
