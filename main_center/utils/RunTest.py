import os
import unittest
from main_center.utils import readConfig
from main_center.utils import HTMLTestRunner
from main_center.utils import HTMLTestRunner_cn
from main_center.utils import HTMLTestRunnerCN
from main_center.utils import configEmail
from main_center.utils import common

localReadConfig = readConfig.ReadConfig()

class RunTest:
    def __init__(self):
        global resultPath, on_off
        resultPath = common.get_report_path()  # TODO
        on_off = localReadConfig.get_email('on_off')
        self.caseRoot = os.path.join(readConfig.proDir, 'testCase')# testAPI文件路径
        self.caseTest = ''
        self.email = configEmail.MyEmail.get_email()  # TODO

    def set_case_test(self):  # 设置测试py
        self.caseTest = 'testAPI.py'

    def set_case_suite(self):
        self.set_case_test()   # 设置了 执行文件
        test_suite = unittest.TestSuite()
        suite_module = []
        discover = unittest.defaultTestLoader.discover(self.caseRoot, pattern=self.caseTest, top_level_dir=None)
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
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                # runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                # runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
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
                print('Unknow state.')

if __name__ == '__main__':
    la = RunTest()
    la.run()