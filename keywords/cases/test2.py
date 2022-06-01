#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

from keywords.keys.keys import Keys

k = Keys("Edge")
k.open_web('https://www.baidu.com/')
k.input("id", "kw", "UI自动化")
k.search("id", "su")
k.quit()
