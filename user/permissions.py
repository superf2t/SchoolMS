from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

from rest_framework.exceptions import PermissionDenied

from .models import *


# 获取某个model的全部权限列表
# Receive ----------------------------------
# model: a model
# Return -----------------------------------
# permissions: all permission related to this model
def get_model_permission(model):
    content_type = ContentType.objects.get_for_model(model)
    permissions = Permission.objects.filter(content_type=content_type)
    return permissions


# 为用户分配组权限
# assign <--> revoke
# Receive ----------------------------------
# user: a user instance
# group: django group name
def assign_group(user, group):
    group, created = Group.objects.get_or_create(name=group)
    user.groups.add(group)


# 检查用户是否有某些权限
# Receive ----------------------------------
# user: a user instance
# perm_list: required permission list
# Return -----------------------------------
# None or raise PermissionDenied if permission not satisfy
def permission_required(user, perm_list):
    print('-------------------------------------------')
    for perm in perm_list:
        print("Permission_required: "+perm)
    print('-------------------------------------------')
    if user.has_perms(perm_list):
        pass
    else:
        raise PermissionDenied


# 检查用户是否有组权限
# Receive ----------------------------------
# user: a user instance
# group: required group permission name
# Return -----------------------------------
# True or False
def group_required(user, group):
    if user.groups.filter(name=group).exists():
        return True
    else:
        return False
