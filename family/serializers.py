from collections import OrderedDict

from rest_framework import serializers
from rest_framework.fields import SkipField

from user.serializers import ModelSerializer, DynamicFieldsModelSerializer, UserListSerializer
from .models import *


# --------------------------------- 公告模板 ---------------------------------
# 创建公告模板
class NoticeTemplateCreateSerializer(ModelSerializer):
    class Meta:
        model = NoticeTemplate
        fields = ('branch', 'name', 'content')


# 列表公告模板
class NoticeTemplateListSerializer(ModelSerializer):
    class Meta:
        model = NoticeTemplate
        fields = ('id', 'branch', 'name', 'content')


# 公告模板
class NoticeTemplateSerializer(ModelSerializer):
    class Meta:
        model = NoticeTemplate
        fields = ('id', 'branch', 'name', 'content')


# --------------------------------- 公告 ---------------------------------
# 创建公告
class NoticeCreateSerializer(ModelSerializer):
    class Meta:
        model = Notice
        fields = ('from_user', 'branches', 'is_publish', 'is_top', 'content',
                  'publish_time', 'always_useful', 'expiration_time')


# 列表公告
class NoticeListSerializer(ModelSerializer):
    class Meta:
        model = Notice
        fields = ('id', 'from_user', 'branches', 'is_publish', 'is_top', 'content',
                  'publish_time', 'always_useful', 'expiration_time')


# 公告
class NoticeSerializer(ModelSerializer):
    class Meta:
        model = Notice
        fields = ('id', 'from_user', 'branches', 'is_publish', 'is_top', 'content',
                  'publish_time', 'always_useful', 'expiration_time')


# --------------------------------- 短信模板 ---------------------------------
# 创建短信模板
class SMSTemplateCreateSerializer(ModelSerializer):
    class Meta:
        model = SMSTemplate
        fields = ('branch', 'name', 'content')


# 列表短信模板
class SMSTemplateListSerializer(ModelSerializer):
    class Meta:
        model = SMSTemplate
        fields = ('id', 'branch', 'name', 'content')


# 短信模板
class SMSTemplateSerializer(ModelSerializer):
    class Meta:
        model = SMSTemplate
        fields = ('id', 'branch', 'name', 'content')


# --------------------------------- 短信 ---------------------------------
# 创建短信
class SMSCreateSerializer(ModelSerializer):
    class Meta:
        model = SMS
        fields = ('branch', 'from_user', 'to_users', 'content', 'signature')


# 列表短信
class SMSListSerializer(ModelSerializer):
    class Meta:
        model = SMS
        fields = ('id', 'branch', 'from_user', 'to_users', 'content', 'signature')


# 短信
class SMSSerializer(ModelSerializer):
    class Meta:
        model = SMS
        fields = ('id', 'branch', 'from_user', 'to_users', 'content', 'signature')


# --------------------------------- 短信记录 ---------------------------------
# 创建短信记录
class SMSRecordCreateSerializer(ModelSerializer):
    class Meta:
        model = SMSRecord
        fields = ('branch', 'from_user', 'to_user_name', 'to_user_tel', 'content', 'word_count')


# 列表短信记录
class SMSRecordListSerializer(ModelSerializer):
    class Meta:
        model = SMSRecord
        fields = ('id', 'branch', 'from_user', 'to_user_name', 'to_user_tel', 'content', 'word_count')


# 短信记录
class SMSRecordSerializer(ModelSerializer):
    class Meta:
        model = SMSRecord
        fields = ('id', 'branch', 'from_user', 'to_user_name', 'to_user_tel', 'content', 'word_count')


# --------------------------------- 短信分配 ---------------------------------
# 创建短信分配
class SMSAssignCreateSerializer(ModelSerializer):
    class Meta:
        model = SMSAssign
        fields = ('branch', 'user', 'assign_sum', 'used', 'remain', 'auto_reset')


# 列表短信分配
class SMSAssignListSerializer(ModelSerializer):
    class Meta:
        model = SMSAssign
        fields = ('id', 'user', 'assign_sum', 'used', 'remain', 'auto_reset')


# 短信分配
class SMSAssignSerializer(ModelSerializer):
    class Meta:
        model = SMSAssign
        fields = ('id', 'user', 'assign_sum', 'used', 'remain', 'auto_reset')

