import unittest
import paramunittest
from testPlaform.main_center.utils import common
# from utils.customer_utils import customerConfigHttp as ConfigHttp
import json
API_list = req.body
localReadConfig = readConfig.customerReadConfig()

configHttp = ConfigHttp.customerConfigHttp()
localDB = customerConfigDB.CustomerDB()
flag = common.get_flag()
@paramunittest.parametrized(*API_list)
class TimeShare(unittest.TestCase):
    def __init__(self):
        self.flag = common

    def setParameters(self, case_name, url, method, headers, params, code, msg):
        """
        set Params
        :param case_name:
        :param url:
        :param method:
        :param headers:
        :param params:
        :param code:
        :param msg:
        :return:
        """
        self.case_name = str(case_name)
        self.url = str(url)
        self.method = str(method)
        self.headers = headers
        self.params = params
        self.code = str(code)
        self.msg = str(msg)
        self.return_json = None
        self.info = None

    def setUp(self):
        """
        :return:
        """
        # self.log = Log.MyLog.get_log()
        # self.logger = self.log.get_logger()
        # self.log.build_start_line(self.case_name)
        print("---接口用例" + self.case_name + "测试开始前准备---")

    def testTimeShare(self):
        """
        test body
        :return:
        """

        # --------------------- set url ---------------------
        if common.check_url(self.url) == True:  # 检查URL 是全的
            configHttp.set_all_url(self.url)
        else:
            configHttp.set_url(self.url)

        print("\n第一步：设置url:\t" + self.url)
        # --------------------- set headers ---------------------

        configHttp.set_headers(json.loads(self.headers))

        print("\n第二步：设置header:\t" + str(configHttp.headers))

        # --------------------- set params ---------------------

        dict_params = json.loads(self.params)
        configHttp.set_params(dict_params)

        print("\n第三步：设置发送请求的参数\t" + '\n' + json.dumps(configHttp.params, ensure_ascii=False, sort_keys=True,
                                                      indent=4))

        # --------------------- test interface ---------------------
        if self.method == "post":
            self.return_json = configHttp.post()
        elif self.method == "get":
            self.return_json = configHttp.get()

        # self.return_json = configHttp.post()
        localReadConfig.set_customer('return_json', json.dumps(self.return_json.json()['result']))
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
                "Request：\n" + json.dumps(configHttp.params, ensure_ascii=False, sort_keys=True, indent=4))

            # show return message
            common.show_return_msg(self.return_json)

            self.assertEqual(self.info['code'], self.code)
            self.assertEqual(self.info['msg'], self.msg)

            # DB check

        except Exception as ex:
            # insert bug    repr(e)
            print("弄上去禅道" + '\n' + '\n')

            '''insert_params = ['接口用例' + self.case_name + '报错', '接口地址：<br/>' + self.return_json.url + '<br/><br/>' +
                             '请求报文：<br/>' + json.dumps(
                configHttp.params) + '<br/><br/>' + '报错信息：<br/>' + r'<span style="color:red"><b>' + repr(
                ex) + '</b></span><br/><br/>' + '返回报文：<br/>' + json.dumps(self.return_json.json()),
                             datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                             datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
            MyDB().insert_zt_bug(*insert_params)

            self.logger.exception(ex)
            raise AssertionError(repr(ex))
        '''
        else:
            self.log.build_case_line(self.case_name, self.info['code'], self.info['msg'])
            self.log.build_end_line(self.case_name)
            print("\n第五步：检查结果:\t测试通过\t" + self.info['code'] + "\t" + self.info['msg'])
            print('\n' + '\n')
