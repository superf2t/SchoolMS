# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_publish', models.BooleanField(default=True, verbose_name='是否发布')),
                ('is_top', models.BooleanField(default=False, verbose_name='置顶')),
                ('content', models.TextField(verbose_name='正文')),
                ('publish_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布时间')),
                ('always_useful', models.BooleanField(default=False, verbose_name='长期有效')),
                ('expiration_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='到期时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '公告',
                'verbose_name_plural': '公告',
            },
        ),
        migrations.CreateModel(
            name='NoticeTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='模板名称')),
                ('content', models.TextField(verbose_name='模板内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '公告模板',
                'verbose_name_plural': '公告模板',
            },
        ),
        migrations.CreateModel(
            name='SMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_users', models.TextField(verbose_name='接收用户')),
                ('content', models.TextField(verbose_name='短信内容')),
                ('signature', models.CharField(blank=True, max_length=255, null=True, verbose_name='短信签名')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '短信',
                'verbose_name_plural': '短信',
            },
        ),
        migrations.CreateModel(
            name='SMSAssign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assign_sum', models.IntegerField(default=0, verbose_name='本期分配条数')),
                ('used', models.IntegerField(default=0, verbose_name='已使用')),
                ('remain', models.IntegerField(default=0, verbose_name='剩余')),
                ('auto_reset', models.BooleanField(default=True, verbose_name='月底自动清零')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '短信分配',
                'verbose_name_plural': '短信分配',
            },
        ),
        migrations.CreateModel(
            name='SMSRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_user_name', models.CharField(max_length=255, null=True, verbose_name='接收人姓名')),
                ('to_user_tel', models.CharField(max_length=255, null=True, verbose_name='接收人电话')),
                ('content', models.TextField(verbose_name='短信内容')),
                ('word_count', models.IntegerField(blank=True, default=0, verbose_name='短信字数')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '短信记录',
                'verbose_name_plural': '短信记录',
            },
        ),
        migrations.CreateModel(
            name='SMSTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='模板名称')),
                ('content', models.TextField(verbose_name='模板内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '短信模板',
                'verbose_name_plural': '短信模板',
            },
        ),
    ]
