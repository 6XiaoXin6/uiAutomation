#!/usr/bin/env python3
# -*- coding:utf-8 -*-

""" """

__author__ = 'List.Xie'

from unittest import TestSuite

from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner

# from  import TestSuite
from POM.cases.baidu_test import BaiDuTest
from POM.cases.login_test import TestLogin

ts = TestSuite()
# 1
# ts.addTest(BaiDuTest('test_8'))
# 2
tests = [BaiDuTest('test_10'), TestLogin('test_login_1')]
ts.addTests(tests)
# 3
# tests=defaultTestLoader.discover(start_dir='../cases/',pattern='*test.py')
# 4
# ts.addTests(unittest.TestLoader().loadTestsFromTestCase(BaiDuTest))
# ts.addTests(unittest.TestLoader().loadTestsFromName('POM.cases.baidu_test.BaiDuTest'))
# tr=TextTestRunner()
# tr.run(ts)
p = "../reports/htmltestrunner_reports/report.html"
with open(p, "w", encoding="utf-8") as f:
    runner = HTMLTestRunner(stream=f, title="我的测试报告", description="我的测试报告描述", )
    runner.run(ts)
