from django.db import models


class Base(models.Model):
      create_time = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')
      update_time = models.DateTimeField(auto_now=True,verbose_name='修改时间')

      class Meta:
            abstract = True

class User(Base):
      username = models.CharField(unique=True,max_length=50,verbose_name='用户名')
      display_name = models.CharField(max_length=50,verbose_name='昵称',default='')
      password = models.CharField(max_length=255,verbose_name='密码')
      def __str__(self):
            return self.username


class UserInfo(Base):
      user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='关联用户')
      data = models.TextField(verbose_name='个人信息')
      def __str__(self):
            return self.user.username
      




