from django.http import StreamingHttpResponse
import os
import requests
import json
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from main_center.utils import RunTest
from main_center.utils import common
import re
from main_center.utils.checkDB import cut_sql
from main_center.utils import readConfig

localReadconfig = readConfig.ReadConfig()

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


def build_case(req):
    """
    获取请求中的用例列表，然后获取模板，写进模板，保存下载
    用 openpyxl
    :param req:
    :return:
    """
    if req.method == 'post' or 'POST':
        print(req.body)
        print(json.loads(req.body)['list'])
        d_list = json.loads(req.body)['list']
        flag = json.loads(req.body)['flag']
        a = re.findall(re.compile(r"{.*?}"), d_list)
        b = []
        print(type(a))
        print(json.loads(a[0]))
        for i in a:
            k = json.loads(i)
            del k['name']
            b.append(list(k.values()))
        print(b)  # 传列表
        k = common.download_file(b, flag)
        print(k)
        return JsonResponse(_get_req_json_dic(k, 0, '成功'))


def download_case(req):
    def file_iterator(file_name, chunk_size=512):
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    flag = json.loads(req.body)['flag']
    if flag == '1':
        res = StreamingHttpResponse(file_iterator(r'D:\pycharm\graduation\main_center\utils\download_template\Func_case.xlsx'))
    if flag == '2':
        res = StreamingHttpResponse(file_iterator(r'D:\pycharm\graduation\main_center\utils\download_template\API_case.xlsx'))
    if flag == '3':
        res = StreamingHttpResponse(file_iterator(r'D:\pycharm\graduation\main_center\utils\checkDB\DDL_file\Template-DDL.sql'))
    res['Content-Type'] = 'aaplication/octet.stream'
    res['Content-Dispositon'] = 'attachment;'
    # print('aaaaa')
    return res
    # else:
    #     return JsonResponse(_get_req_json_dic('', -1, '无效请求'))


def handle_remove(req):
    if req.method == 'post' or 'POST':
        print('进来啦')
        file = json.loads(req.body)
        common.delete_file_by_name(file['name'], file['path'])
        return JsonResponse(_get_req_json_dic('', 0, '成功'))
    else:
        return JsonResponse(_get_req_json_dic('', -1, '无效请求'))


def testUp(req):
    if req.method == 'POST' or 'post':
        # print("进来了")
        excel = req.FILES.get('file')
        excel_name = req.FILES.get('file').name
        path = default_storage.save('D:/pycharm/graduation/main_center/utils/testFile/' + excel_name, ContentFile(excel.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)  # TODO
        return JsonResponse(_get_req_json_dic(""))
    else:
        return JsonResponse(_get_req_json_dic('', -1, '无效请求'))


def save_DDL(req):
    print('进来了')
    DDL = req.FILES.get('file')
    DDL_name = req.FILES.get('file').name
    path = default_storage.save('D:/pycharm/graduation/main_center/utils/checkDB/DDL_file/' + DDL_name, ContentFile(DDL.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT, path)
    localReadconfig.set_path('ddl_path', path)
    # print(r)
    return JsonResponse(_get_req_json_dic('', 0, '成功'))


def upload_DDL(req):
    if req.method == 'get' or 'GET':
        path = localReadconfig.get_path('ddl_path')
        c = cut_sql.SQLCut()
        sql_content = c.open_sql_file(path)
        # print(sql_content)
        return JsonResponse(_get_req_json_dic(sql_content, 0, '成功'))
    else:
        return JsonResponse(_get_req_json_dic('', -1, '无效请求'))


def resole_DDL(req):
    if req.method == 'post' or 'POST':
        sql = cut_sql.SQLCut()
        sql_content = json.loads(req.body)['data']
        # print(sql_content)
        result = sql.resole_all(sql_content)
        print('result:', result)
        after_result = sql.change_show_style(result)
        return JsonResponse(_get_req_json_dic(after_result, 0, '成功'))
    else:
        return JsonResponse(_get_req_json_dic('', -1, '成功'))


def upload_case_to_zt(req):
    if req.method == 'post' or 'POST':
        req_dict = json.loads(req.body)
        print(req_dict)
        print(type(req_dict))
        upload_params = req.dict['list']
        common.change_params_style(upload_params, req_dict['module'])
        common.execute_upload()
        return JsonResponse(_get_req_json_dic('', 0, '成功'))
    else:
        return JsonResponse(_get_req_json_dic('', -1, '无效请求'))


def _get_req_json_dic(data, code=0, msg="success"):  # 封装返回信息
    """
    封装返回信息
    :param data:
    :param code:
    :param msg:
    :return:
    """
    result_data = {
        "code": code,
        "msg": msg,
        "data": data
    }
    return result_data





