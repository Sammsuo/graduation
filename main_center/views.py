from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
# Create your views here.


def public_post(req):
    print(req.method)
    print(req.body)
    if req.method == 'POST':
        res = json.loads(req.body)
        print(type(res))
        print(type(res['requestUrl']))
        print(res['params'])
        print(type(res['Headers']))
        get_conn = requests.post(res['requestUrl'], res['params'], headers=json.loads(res['Headers']))
        print('req-->', get_conn.json())
        return JsonResponse(_get_req_Json_dic(get_conn.json()))
    else:
        return JsonResponse(_get_req_Json_dic('', -1, '无效请求'))

def _get_req_Json_dic(data, code=0, msg='success'):
    result_data = {
        'code': code,
        'msg': msg,
        'data': data
    }
    return result_data

