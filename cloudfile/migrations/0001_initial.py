# Generated by Django 2.0.4 on 2019-10-24 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cloudapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('filename', models.CharField(max_length=40, verbose_name='文件名')),
                ('file_size', models.FloatField(verbose_name='文件大小')),
                ('file_md5', models.CharField(max_length=255, verbose_name='文件md5')),
                ('file_status', models.IntegerField(choices=[(0, '已删除'), (1, '正常显示')], verbose_name='文件状态')),
                ('addr', models.CharField(max_length=180, verbose_name='文件存储路径')),
                ('file_type', models.IntegerField(choices=[(1, '文件'), (2, '目录')], verbose_name='文件类型')),
                ('directory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cloudfile.File', verbose_name='文件父级目录')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Liked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_activce', models.BooleanField(default=False, verbose_name='收藏现状')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloudfile.File', verbose_name='文件')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloudapp.User', verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='MimeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('mtype', models.IntegerField(choices=[(1, '')], verbose_name='文件mimetype类型')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('token', models.CharField(max_length=255, verbose_name='token')),
                ('timestamp', models.DateTimeField()),
                ('is_trash', models.BooleanField(default=False, verbose_name='是否删除分享')),
                ('permission', models.IntegerField(choices=[(1, '读'), (2, '写')], verbose_name='分享权限')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloudfile.File', verbose_name='分享文件')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='cloudapp.User', verbose_name='分享者')),
                ('recv_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recv_user', to='cloudapp.User', verbose_name='接收者')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('file_path', models.CharField(max_length=100, verbose_name='文件路径')),
                ('size', models.FloatField(verbose_name='节点大小')),
                ('size_used', models.FloatField(verbose_name='已使用大小')),
                ('is_active', models.BooleanField(default=True, verbose_name='节点状态')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cloudapp.User', verbose_name='关联用户')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='file',
            name='mime_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloudfile.MimeType', verbose_name='mimetype'),
        ),
        migrations.AddField(
            model_name='file',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloudfile.Storage', verbose_name='所属节点'),
        ),
        migrations.AddField(
            model_name='file',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloudapp.User', verbose_name='关联用户'),
        ),
        migrations.AlterUniqueTogether(
            name='liked',
            unique_together={('file', 'user')},
        ),
    ]
