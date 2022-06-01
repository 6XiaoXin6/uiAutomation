#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

from selenium.webdriver.common.by import By

from POM.base import Base


class BaiDu(Base.BasePage):
    url = "https://www.baidu.com/"

    shuru = (By.ID, "kw")
    sousuo = (By.ID, "su")

    def research(self, word):
        self.open_url(self.url)
        # self.locate_and_input(self.shuru[0],self.shuru[1],self.shuru[2])
        self.locate_and_input(*self.shuru, word)
        self.click(*self.sousuo)
