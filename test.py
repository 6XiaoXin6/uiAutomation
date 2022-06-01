#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

import json,time
# from excel_driver.excel_read import args2dict
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# element = driver.find_element("id", "kw")
# element.send_keys("UI自动化")
# driver.find_element("id", "su").click()
def args2dict(value):
    args={}
    for s in value.split(";"):
        d = s.split('=', 1)
        args[d[0]] = d[1]
    return args


s = args2dict("method=id;value=kw;word=接口自动化")
# if print(s) is not None:


# if nam:
time.sleep(7)