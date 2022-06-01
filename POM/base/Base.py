#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

from selenium import webdriver


class BasePage:
    def __init__(self, browser):
        self.driver = getattr(webdriver, browser, webdriver.Edge)()
        self.driver.implicitly_wait(5)
        # if browser=="Chrome":
        #     self.driver = webdriver.Chrome()
        # elif browser=="Edge":
        #     self.driver = webdriver.Edge()
        # else:
        #     self.driver = webdriver.Edge()

    def open_url(self, url):
        self.driver.get(url)

    def locate(self, method, value):
        return self.driver.find_element(method, value)

    def locate_and_input(self, method, value, text):
        self.driver.find_element(method, value).send_keys(text)

    def click(self, method, value):
        self.driver.find_element(method, value).click()



# element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, "kw")))
