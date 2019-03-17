from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib import auth
import json
from django.shortcuts import render
from django.http import JsonResponse
import logging
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

logger = logging.getLogger('log')
# Create your views here.


def register(request):  # 注册函数
    User.objects.create_user(username='admin', password='123456')


def index(request):          # 返回登录页
    return render(request, 'index.html')

@csrf_exempt
def logging_in(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        user_name = body.get('username')
        pass_word = body.get('password')

        user = authenticate(username=user_name, password=pass_word)  # 做校验，返回user对象

        if user is not None:
            auth.login(request, user)
            data = {'username': user.username, 'lastlogin': user.last_login}
            return JsonResponse(_get_responese_json_dic(data))
        else:
            logger.warning('{}登陆失败，用户名或密码错误'.format(user_name))
            return JsonResponse(_get_responese_json_dic('', -1, u'用户名或密码错误'))
    return JsonResponse(_get_responese_json_dic('', -1, u'请求无效'))


def _get_responese_json_dic(data, code=0, message='success'):
    result_data = {
        'code': code,
        'message': message,
        'data': data
    }
    return result_data


def log_user_out(request):
    auth.logout(request)
    return JsonResponse(_get_responese_json_dic('', -1, u'请求无效'))

