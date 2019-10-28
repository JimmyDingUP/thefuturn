from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import reverse
from django.http import JsonResponse
import json
import time
from .views import ts_obj,TJW


# 需要登录的页面列表，反向解析得到连接 
LOGIN_REQUIRE_LIST = [reverse(var) for var in ['userinfo',]]
class LoginRequired(MiddlewareMixin):
      def process_request(self,request):
            if request.path in LOGIN_REQUIRE_LIST:
                  token = request.META.get('HTTP_AUTHORIZATION')
                        # js空值用null表示，python会识别为字符串
                  if not token or token == 'null':
                        return JsonResponse({
                              'code' : 6207,
                              'message' : '未认证'
                        })
                  else:
                        token_data = ts_obj.loads(token)
                        
                        # eval()函数会将字符串转换为可用python数据类型，相对于的函数repr()
                        if token_data['expire'] < time.time():
                              return JsonResponse({
                                    'code': 70001,
                                    'message' : 'token过期'
                              })