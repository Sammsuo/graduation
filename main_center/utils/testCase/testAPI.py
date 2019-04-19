import unittest
import paramunittest
from main_center.utils import common
from main_center.utils import readConfig
from main_center.utils import configHttp
from main_center.utils.configDB import MyDB
# from utils.customer_utils import customerConfigHttp as ConfigHttp
from main_center.utils import Log
import json
import datetime

API_list = common.get_xlsx_sheets(common.get_file())
localReadConfig = readConfig.ReadConfig()

localConfigHttp = configHttp.configHttp()
localDB = MyDB()

@paramunittest.parametrized(*API_list)
class APITest(unittest.TestCase):
    def setParameters(self, case_name, url, method, headers, params, check_param):
        """
        set params
        :param case_name:
        :param url:
        :param method:
        :param headers:
        :param params:
        :param code:
        :param msg:
        :param check_param:
        :return:
        """
        self.case_name = str(case_name)
        self.url = str(url)
        self.method = str(method)
        self.headers = headers
        self.params = params
        self.check_param = str(check_param)
        self.return_json = None
        self.info = None

    def setUp(self):
        """
        :return:
        """
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        self.log.build_start_line(self.case_name)
        print("---接口用例" + self.case_name + "测试开始前准备---")

    def testAPI(self):
        """
        test body
        :return:
        """

        # --------------------- set url ---------------------
        if common.check_url(self.url) is True:  # 检查URL 是全的
            localConfigHttp.set_all_url(self.url)
        else:
            localConfigHttp.set_url(self.url)

        print("\n第一步：设置url:\t" + self.url)
        # --------------------- set headers ---------------------

        localConfigHttp.set_headers(json.loads(self.headers))

        print("\n第二步：设置header:\t" + str(localConfigHttp.headers))

        # --------------------- set params ---------------------

        dict_params = json.loads(self.params)
        localConfigHttp.set_params(dict_params)

        print("\n第三步：设置发送请求的参数\t" + '\n' + json.dumps(localConfigHttp.params, ensure_ascii=False, sort_keys=True,
                                                      indent=4))

        # --------------------- test interface ---------------------
        if self.method == "post":
            self.return_json = localConfigHttp.post()
        elif self.method == "get":
            self.return_json = localConfigHttp.get()

        # self.return_json = configHttp.post()
        request_type = str(self.return_json.request)[
                       int(str(self.return_json.request).find('[')) + 1:int(
                           str(self.return_json.request).find(']'))]
        print("\n第四步：发送请求:\t请求类型\t" + request_type)

        # --------------------- check result ---------------------
        self.checkResult()

    def tearDown(self):
        """
        :return:
        """

    def checkResult(self):
        """
        check test result
        :return:
        """

        try:

            self.info = self.return_json.json()

            self.logger.info("URL：\n" + self.return_json.url)
            self.logger.info(
                "Request：\n" + json.dumps(localConfigHttp.params, ensure_ascii=False, sort_keys=True, indent=4))

            # show return message
            common.show_return_msg(self.return_json)

            check_dic = common.changge_check_params(self.check_param)
            for key in check_dic:
                print(str(self.info[key]))
                self.assertEqual(str(self.info[key]), check_dic[key])
            # DB check

        except Exception as ex:
            # insert bug    repr(e)
            print(ex)
            print("弄上去禅道" + '\n' + '\n')

            insert_params = ['接口用例' + self.case_name + '报错', '接口地址：<br/>' + self.return_json.url + '<br/><br/>' +
                             '请求报文：<br/>' + json.dumps(
                localConfigHttp.params) + '<br/><br/>' + '报错信息：<br/>' + r'<span style="color:red"><b>' + repr(
                ex) + '</b></span><br/><br/>' + '返回报文：<br/>' + json.dumps(self.return_json.json()),
                             datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                             datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
            localDB.insert_zt_bug(*insert_params)

            self.logger.exception(ex)
            raise AssertionError(repr(ex))

        else:
            self.log.build_case_line(self.case_name, self.check_param)
            self.log.build_end_line(self.case_name)
            print("\n第五步：检查结果:\t测试通过\t" + self.check_param)
            print('\n' + '\n')


if __name__ == '__main__':
    unittest.main(verbosity=2)