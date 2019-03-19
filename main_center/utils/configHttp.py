import requests
from main_center.utils import readConfig

readconfig = readConfig.ReadConfig()


class configHttp:
    def __init__(self):
        global scheme, host, port, timeout
        scheme = readconfig.get_http('scheme')
        host = readconfig.get_http('host')
        port = readconfig.get_http('port')
        timeout = readconfig.get_http('timeout')
        self.url = None
        self.headers = {}
        self.params = {}

    def set_all_url(self, url):
        self.url = url

    def set_url(self, url):
        self.url = scheme + '://' + host + ':' + port + url

    def set_params(self, *param):
        self.params = param

    def set_headers(self, headers):
        self.headers = headers

    def post(self, cookies=''):
        """
        定义 post
        :param cookies:
        :return:
        """
        try:
            response = requests.post(self.url, json = self.params, headers = self.headers, cookies = cookies, timeout=float(timeout))

            return response
        except TimeoutError:
            return None

    def get(self):
        """
        定义 get
        :return:
        """
        try:
            response = requests.post(self.url, headers = self.headers, params = self.params, timeout = float(timeout))
            return response
        except TimeoutError:
            return None
