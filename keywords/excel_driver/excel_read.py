#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

import openpyxl

from keywords.keys.keys import Keys

excel = openpyxl.load_workbook("../data/new_data.xlsx")


def args2dict(value):
    args = {}

    if value[2]:
        for s in value[2].split(";"):
            d = s.split('=', 1)
            args[d[0]] = d[1]
    return args


for sheet in excel:
    print(f"-------------case:{sheet.title}------------")
    for value in sheet.values:
        if isinstance(value[0], int):
            print(f"======{value[1]}:正在{value[3]}======")
            # data = {"arg1": value[2], "arg2": value[3], "arg3": value[4]}
            data = args2dict(value)
            for key in list(data.keys()):
                if not data[key]:
                    del data[key]
            if value[1] == "open_browser":
                k = Keys(**data)
            elif "assert" in value[1]:
                if getattr(k, value[1])(**data):
                    print('断言成功')
                else:
                    print('断言失败')
            else:
                getattr(k, value[1])(**data)
    print()
