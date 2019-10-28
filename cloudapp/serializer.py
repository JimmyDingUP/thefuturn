from rest_framework import serializers
from . import models
from django.contrib.auth.hashers import make_password

class UserSer(serializers.ModelSerializer):

      def create(self,value):
            n = models.User.objects.create(
                  username=value['username'],
                  password=make_password(value['password'])
            )
            return n
      class Meta:
            fields = '__all__'
            model = models.User



class UserInfoSer(serializers.ModelSerializer):

      def create(self,value):
            n = models.UserInfo.objects.create(
                  **value
            )
            return n
      class Meta:
            fields = '__all__'
            model = models.UserInfo












