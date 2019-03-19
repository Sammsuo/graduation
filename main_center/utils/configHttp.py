import requests
from testPlaform.main_center.utils import readConfig

class configHttp:
    def __init__(self):
        global scheme, host, port
        scheme = readConfig.ReadConfig.get_http('scheme')
        host = readConfig.ReadConfig.get_http('host')
        port = readConfig.ReadConfig.get_http('port')
        self.url = None
        self.header = {}
        self.params = {}

    def set_all_url(self,url):
        self.url = url

    def set_url(self, url):
        self.url = scheme + '://' + host + ':' + port + url

    def set_params(self, *param):
        pass

    def set_header(self, header):
        pass
