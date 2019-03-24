from django.shortcuts import render
import os
import requests
import request
import json
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from main_center.utils import RunTest
import unittest
import paramunittest
import main_center.utils.common
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
        return JsonResponse(_get_req_json_dic("", 0, '成功'))
    else:
        return JsonResponse(_get_req_json_dic('', -1, '无效请求'))


def run_check_ddl(req):
    pass


def handle_upload_file(req):  # TODO 完善处理上传的文件
    if req.method == 'POST':
        file = req.FILES.get('file')  # 前端返回是文件
        print(file)


def testUp(req):
    if req.method == 'POST':
        # print("进来了")
        excel = req.FILES.get('file')
        excel_name = req.FILES.get('file').name
        path = default_storage.save('/Users/sam/PycharmProjects/graduation/main_center/utils/testFile/' + excel_name, ContentFile(excel.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        return JsonResponse(_get_req_json_dic(""))
    else:
        return JsonResponse(_get_req_json_dic('', -1, '无效请求'))


def _get_req_json_dic(data, code=0, msg="success"):
    result_data = {
        "code": code,
        "msg": msg,
        "data": data
    }
    return result_data


def testAPI(file_url):  #  代替runall
    pass  # TODO:接收前端信息



