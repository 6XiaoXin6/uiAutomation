#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

import time
import unittest

from POM.page_objects.login import LoginPage


class TestLogin(unittest.TestCase):
    def test_login_1(self):
        lp = LoginPage("Edge")
        lp.login("520淘淘小新", "xyz307322186")
        time.sleep(3)
        title=lp.driver.title
        assert title == "淘宝网 - 淘！我喜欢"

    # def test_login_2(self):
    #     lp = LoginPage("Edge")
    #     lp.login("520淘淘小新", "xyz307322182")
# lp = LoginPage("Edge")
# lp.login("520淘淘小新", "xyz3073221861")
