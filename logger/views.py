from django.shortcuts import render

from .models import *


# 新建系统日志
def add_log(user, category, content):
    Logger.objects.create(user=user, category=category, content=content)


# 将request转为为str
def queryset_str(data):
    ''.join(i + ':' + data[i] + ' ' for i in data)