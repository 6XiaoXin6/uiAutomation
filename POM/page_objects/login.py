#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

from selenium.webdriver.common.by import By

from POM.base.Base import BasePage


class LoginPage(BasePage):
    url = 'https://login.taobao.com/member/login.jhtml'

    username = (By.NAME, "fm-login-id")
    password = (By.NAME, "fm-login-password")
    login_btn = (By.CLASS_NAME, "fm-button fm-submit password-login")

    def login(self, username, password):
        self.open_url(self.url)
        # self.locate_and_input(self.username[0], self.username[1],username)
        # self.locate_and_input(self.password[0], self.password[1],password)
        self.locate_and_input(*self.username, username)
        self.locate_and_input(*self.password, password)
        # self.click(*self.login_btn)



