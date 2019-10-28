from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password,check_password
from . import models
import json
from . import serializer
from django.db.models import Q
import os
from cloudapi.settings import USER_INFO_MODEL
"""
JWT
"""
# from rest_framework_jwt.settings import api_settings
# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# jwy_encode_handler = api_settings.JWT_ENCODE_HANDLER
import time
from itsdangerous import TimedJSONWebSignatureSerializer as TJW
from django.conf import settings
ts_obj = TJW(settings.SECRET_KEY,expires_in=3000)
EXPIRE = 2000



class Signup(APIView):
      def post(self,request):
            username = request.data.get('username')
            password = request.data.get('password')
            if not all([username,password]):
                  return Response({
                        'code':0,
                        'message':'请输入完整信息'
                  })
            try :
                  user = models.User.objects.get(
                        username=username
                  )
            except:
                  nuser = serializer.UserSer(data=request.data)
                  if nuser.is_valid():
                        nuser.save()

                        os.mkdir('./data/%s'%username)

                        user = models.User.objects.get(
                              username=username
                        )
                        models.UserInfo.objects.create(
                              user=user,
                              data=json.dumps(USER_INFO_MODEL)
                        )
                        return Response({
                              'code':1,
                              'message':'注册成功'
                        })
                  else:
                        return Response({
                              'code':0,
                              'message':'注册失败',
                              'errors':nuser.errors
                        })
            else:
                  return Response({
                        'code':0,
                        'message':'用户名或邮箱已存在'
                  })

class Signin(APIView):
      def post(self,request):
            username = request.data.get('username')
            password = request.data.get('password')
            
            try:
                  user = models.User.objects.get(
                        username=username
                  )
            except:
                  return Response({
                        'code':0,
                        'message':'用户名不存在'
                  })
            else:
                  if check_password(password,user.password):
                        data = {
                              'username':username,
                              'password':password,
                              'expire':time.time() + EXPIRE
                        }
                        token = ts_obj.dumps(data)
                        token = token.decode()
                        
                        return Response({
                              'code':1,
                              'message':'登录成功',
                              'token':token,
                        })
                  return Response({
                        'code':0,
                        'message':'密码错误'
                  })


class UserInfo(APIView):
      def get(self,request):

            return Response({
                  'code':1
            })

      def post(self,request):
            qqnumber = request.data.get('qqnumber')
            phone = request.data.get('phone')
            address = request.data.get('address')
            email = request.data.get('email')

            USER_INFO_MODEL['QQ'] = qqnumber
            USER_INFO_MODEL['手机'] = phone
            USER_INFO_MODEL['地址'] = address
            USER_INFO_MODEL['EMAIL'] = email

            token = request.META.get('HTTP_AUTHORIZATION')
            token_data = ts_obj.loads(token)
            username = token_data['username']
            user = models.User.objects.get(
                  username=username
            )
            try:

                  userinfo = models.UserInfo.objects.get(
                        user=user
                  )
            except:
                  models.UserInfo.objects.create(
                        user=user,
                        data=USER_INFO_MODEL
                  )
            else: 
                  userinfo.data = USER_INFO_MODEL
                  userinfo.save()

            return Response({
                  'code':1,
                  'message':'修改成功'
            })
            