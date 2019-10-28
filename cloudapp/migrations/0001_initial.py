# Generated by Django 2.0.4 on 2019-10-24 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='用户名')),
                ('display_name', models.CharField(default='', max_length=50, verbose_name='昵称')),
                ('password', models.CharField(max_length=30, verbose_name='密码')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('data', models.TextField(verbose_name='个人信息')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloudapp.User', verbose_name='关联用户')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
