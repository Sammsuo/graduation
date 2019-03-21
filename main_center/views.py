from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
import unittest
import paramunittest
import main_center.utils.common

# Create your views here.


def public_post(req):
    print(req.method)
    print(req.body)
    if req.method == 'POST':
        res = json.loads(req.body)
        get_conn = requests.post(res['requestUrl'], res['params'], headers=json.loads(res['Headers']))
        print('req-->', get_conn.json())
        return JsonResponse(_get_req_json_dic(get_conn.json()))
    else:
        return JsonResponse(_get_req_json_dic('', -1, '无效请求'))


def get_post(req):
    print(req.method)
    print(req.body)
    if req.method == 'GET':
        res = json.loads(req.body)
        get_conn = requests.get(res['requestUrl'], headers=json.loads(res['Header']), params=res['params'])
        print('req-->', get_conn.json())
        return JsonResponse(_get_req_json_dic(get_conn.json()))
    else:
        return JsonResponse(_get_req_json_dic('', -1, '无效请求'))


def runAPITest(req):
    pass

def _get_req_json_dic(data, code=0, msg='success'):
    result_data = {
        'code': code,
        'msg': msg,
        'data': data
    }
    return result_data


def testAPI(file_url):  #  代替runall
    pass  # TODO:接收前端信息



