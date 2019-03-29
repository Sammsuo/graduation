from django.shortcuts import render, HttpResponse
from django.http import StreamingHttpResponse
import os
import requests
import request
import json
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from main_center.utils import RunTest
from main_center.utils import common
import re
import xlrd
import openpyxl

# Create your views here.

def choose_method(req):
    # print(json.loads(req.body))
    params = json.loads(req.body)
    if params['method'] == 'post' or 'POST':
        return public_post(params)
    elif params['method'] == 'get' or 'GET':
        return public_get(params)
    else:
        return JsonResponse(_get_req_json_dic('', -1, '无效请求'))


def public_post(req):
    print(type(req))
    if req['method'] == 'POST' or 'post':
        # res = json.loads(req.body)
        print('进来啦')
        get_conn = requests.post(req['requestUrl'], req['params'], headers=json.loads(req['Headers']))
        print('req-->', get_conn.json())
        return JsonResponse(_get_req_json_dic(get_conn.json()))
    else:
        return JsonResponse(_get_req_json_dic('', -1, '无效请求'))


def public_get(req):
    if req['method'] == 'GET' or 'get':
        # res = json.loads(req.body)
        get_conn = requests.get(req['requestUrl'], headers=json.loads(req['Header']), params=req['params'])
        print('req-->', get_conn.json())
        return JsonResponse(_get_req_json_dic(get_conn.json()))
    else:
        return JsonResponse(_get_req_json_dic('', -1, '无效请求'))


def run_api_test(req):  # 上传
    if req.method == 'get' or 'GET':
        print('进来啦')
        hey = RunTest.RunTest()
        hey.run()
        common.delete_file()
        return JsonResponse(_get_req_json_dic("", 0, '成功'))
    else:
        return JsonResponse(_get_req_json_dic('', -1, '无效请求'))


def run_check_ddl(req):
    pass


def download_case(req):
    """
    获取请求中的用例列表，然后获取模板，写进模板，保存下载
    用 openpyxl
    :param req:
    :return:
    """
    # if req.method == 'post' or 'POST':
        # print(req.body)
    # print(json.loads(req.body)['list'])
    # d_list = json.loads(req.body)['list']
    # flag = json.loads(req.body)['flag']
    # a = re.findall(re.compile(r"{.*?}"), d_list)
    # b = []
    # print(type(a))
    # print(json.loads(a[0]))
    # for i in a:
    #     k = json.loads(i)
    #     del k['name']
    #     b.append(list(k.values()))
    # print(b)  # 传列表
    # k = common.download_file(b, flag)
    k = '/Users/sam/PycharmProjects/graduation/main_center/utils/download_template/Func_case.xlsx'
    def file_iterator(file_name, chunk_size=512):
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    res = StreamingHttpResponse(file_iterator(k))
    res['Content-Type'] = 'aaplication/vnd.ms-excel'
    res['Content-Dispositon'] = 'attachment;filename="Func_case.xlsx"'
    # print('aaaaa')
    return res
    # else:
    #     return JsonResponse(_get_req_json_dic('', -1, '无效请求'))


def handle_remove(req):
    if req.method == 'post' or 'POST':
        print('进来啦')
        file = json.loads(req.body)
        common.delete_file_by_name(file['name'])
        return JsonResponse(_get_req_json_dic('', 0, '成功'))
    else:
        return JsonResponse(_get_req_json_dic('', -1, '无效请求'))


def testUp(req):
    if req.method == 'POST':
        # print("进来了")
        excel = req.FILES.get('file')
        excel_name = req.FILES.get('file').name
        path = default_storage.save('/Users/sam/PycharmProjects/graduation/main_center/utils/testFile/' + excel_name, ContentFile(excel.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)  # TODO
        return JsonResponse(_get_req_json_dic(""))
    else:
        return JsonResponse(_get_req_json_dic('', -1, '无效请求'))


def _get_req_json_dic(data, code=0, msg="success"):  # 封装返回信息
    result_data = {
        "code": code,
        "msg": msg,
        "data": data
    }
    return result_data






