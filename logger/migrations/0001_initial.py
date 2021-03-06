# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 06:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(0, '查看'), (1, '新增'), (2, '修改'), (3, '删除'), (4, '其他')], null=True, verbose_name='操作类型')),
                ('content', models.CharField(max_length=255, null=True, verbose_name='日志内容')),
                ('is_abandon', models.BooleanField(default=False, verbose_name='是否作废')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logger_user', to=settings.AUTH_USER_MODEL, verbose_name='操作人')),
            ],
            options={
                'verbose_name': '操作日志',
                'verbose_name_plural': '操作日志',
            },
        ),
    ]
