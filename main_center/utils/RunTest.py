import os
import unittest
from main_center.utils import readConfig
from main_center.utils import HTMLTestRunner
from main_center.utils import configEmail
from main_center.utils import common

localReadConfig = readConfig.ReadConfig()

class RunTest:
    def __init__(self):
        global resultPath, on_off
        resultPath = log.get_report_path  # TODO
        on_off = localReadConfig.get_email('on_off')
        self.caseRoot = readConfig.proDir # testAPI文件路径
        self.caseTest = ''
        self.email = configEmail.MyEmail.get_email()  # TODO

    def set_case_test(self):  # 设置测试py
        self.caseTest = 'testAPI.py'

    def set_case_suite(self):
        self.set_case_test()
        test_suite = unittest.TestSuite()
        suit_module = []

        