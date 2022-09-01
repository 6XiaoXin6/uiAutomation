#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""待优化:1.入参预选项;2.参数类型检查 """

__author__ = 'List.Xie'

from time import sleep

from selenium import webdriver


class Keys:
    # open
    # driver = webdriver.Edge()

    # driver = webdriver.Chrome
    def __init__(self, browser):
        self.driver = open_browser(browser)

    def open_web(self, url):
        self.driver.get(url)

    def locate(self, method, value):
        return self.driver.find_element(method, value)

    def locate_and_input(self, method, value, word):
        self.driver.find_element(method, value).send_keys(word)

    def search(self, method, value):
        self.driver.find_element(method, value).click()

    def quit(self, time='3'):
        sleep(int(time))
        self.driver.quit()

    def assert_text(self, method, value, expect):
        try:
            assert expect == self.locate(method, value).text, f"页面没找到{expect}"
            return True
        except Exception as e:
            print(e)
            return False
    def get_page_title(self):
        return self.driver.title

def open_browser(browser):
    driver = getattr(webdriver, browser, webdriver.Chrome)()
    return driver
