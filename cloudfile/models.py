from django.db import models
from cloudapp.models import Base,UserInfo,User
# Create your models here.


class Storage(Base,models.Model):
      # 用户存储节点信息
      user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='关联用户')
      # 存储节点路径
      file_path = models.CharField(max_length=100,verbose_name='文件路径')
      # 配额
      size = models.FloatField(verbose_name='节点大小')
      # 已使用大小
      size_used = models.FloatField(verbose_name='已使用大小')
      # 节点状态(0,1)
      is_active = models.BooleanField(default=True,verbose_name='节点状态')
      # 将其变为一个属性不存储在数据库中
      @property
      def used_percent(self):
            return ('%.2f'%(self.size_used/self.size))

class MimeType(Base,models.Model):
      # 文件mimetype类型
      type_choices = (
            (1,''),

      )
      # 类型
      mtype = models.IntegerField(choices=type_choices,verbose_name='文件mimetype类型')      

      def __str__(self):
            return self.mtype


class File(Base,models.Model):
      # 文件
      # User
      user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='关联用户')
      # UserStorgae
      storage = models.ForeignKey(Storage,on_delete=models.CASCADE,verbose_name='所属节点')
      # 文件名
      filename = models.CharField(max_length=40,verbose_name='文件名')
      # 文件大小
      file_size = models.FloatField(verbose_name='文件大小')
      # 文件md5 唯一
      file_md5 = models.CharField(verbose_name='文件md5',max_length=255)
      # MimeType
      mime_type = models.CharField(max_length=100,verbose_name='mimetype')
      # 文件状态(trash)
      status_choices = (
            (0,'已删除'),
            (1,'正常显示')
      )
      file_status = models.IntegerField(choices=status_choices,verbose_name='文件状态') 
      # Directory(父级)
      directory = models.ForeignKey(
            'self',on_delete=models.SET_NULL,null=True,blank=True,verbose_name='文件父级目录')
      # PATH
      addr = models.CharField(max_length=180,verbose_name='文件存储路径')
      # 文件类型: 文件还是目录
      type_choices = (
            (1,'文件'),
            (2,'目录')
      )
      file_type = models.IntegerField(choices=type_choices,verbose_name='文件类型')
      def __str__(self):
            return self.filename



class Share(Base,models.Model):
      # 文件共享
      # token
      token = models.CharField(max_length=255,verbose_name='token')

      timestamp = models.DateTimeField()
      
      is_trash = models.BooleanField(default=False,verbose_name='是否删除分享')
      from_user = models.ForeignKey(
            User,on_delete=models.CASCADE,related_name='from_user',verbose_name='分享者')
      # User 接收分享用户
      recv_user = models.ForeignKey(
            User,on_delete=models.CASCADE,related_name='recv_user',verbose_name='接收者')
      # File      
      file = models.ForeignKey(File,on_delete=models.CASCADE,verbose_name='分享文件')
      permission_choices = (
            (1,'读'),
            (2,'写'),
      )
      permission = models.IntegerField(choices=permission_choices,verbose_name='分享权限')
      def __str__(self):
            return self.from_user.username


class Liked(Base,models.Model):
      # 文件收藏
      # File
      file = models.ForeignKey(File,on_delete=models.CASCADE,verbose_name='文件')
      # User
      user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
      is_activce = models.BooleanField(default=False,verbose_name='收藏现状')

      class Meta:
            unique_together = ('file','user')
      def __str__(self):
            return self.user.username + ':' + self.file.filename




