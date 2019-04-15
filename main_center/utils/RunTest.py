import os
import unittest
from main_center.utils import readConfig
from main_center.utils import HTMLTestRunner
from main_center.utils import HTMLTestRunner_cn
from main_center.utils import HTMLTestRunnerCN
from main_center.utils import configEmail
from main_center.utils import common
import re
from main_center.utils.Log import MyLog as Log

localReadConfig = readConfig.ReadConfig()

class RunTest:
    def __init__(self):
        global log, logger, resultPath, on_off
        log = Log.get_log()
        logger = log.get_logger()
        resultPath = log.get_report_path()  # TODO
        on_off = localReadConfig.get_email('on_off')
        self.caseRoot = os.path.join(readConfig.proDir, 'testCase')# testAPI文件路径
        self.caseTest = ''
        self.email = configEmail.MyEmail.get_email()  # TODO

    def set_case_test(self):  # 设置测试py
        """
        设置测试类
        :return:
        """
        self.caseTest = 'testAPI.py'

    def set_case_suite(self):
        """
        设置用例集
        :return:
        """
        self.set_case_test()   # 设置了 执行文件
        test_suite = unittest.TestSuite()
        suite_module = []
        discover = unittest.defaultTestLoader.discover(self.caseRoot, pattern=self.caseTest, top_level_dir=None)

        after_sort_list = self.deal_sort(discover)
        discover = after_sort_list

        suite_module.append(discover)
        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return "没有找到执行文件"

        return test_suite

    def run(self):
        """
        执行用例集，生成报告
        run test
        :return:
        """
        try:
            suit = self.set_case_suite()
            # print(suit)
            if suit is not None:
                # logger.info("********** TEST START ***********")
                print(resultPath)
                fp = open(resultPath, 'wb')
                # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                # runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=fp, title='Test Report', description='Test Description')
                runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                runner.run(suit)
                return '完成'
            else:
                return '没有用例可测试'
        except Exception as ex:
            print(str(ex))
            return ex
        finally:
            print('########  Test End ##########')
            fp.close()

            # send email
            if on_off == 'on':
                self.email.send_email()
            elif on_off == 'off':
                print('不发送邮件')
            else:
                print('未定义状态')

    def deal_sort(self, discover):
        """
        处理 paramunittest 框架ascII码顺序执行问题
        :param discover:
        :return:
        """
        x = 0
        for i in discover._tests:
            v, s, k = [], [], []
            [v.append(int(re.findall("(\d+)", str(i._tests[0]))[0])) for i in i]
            [s.append(i) for i in i]
            for e in range(len(v)):
                k.append(s[v.index(e)])
            discover._tests[x]._tests = k
            x += 1
        return discover
if __name__ == '__main__':
    la = RunTest()
    la.run()