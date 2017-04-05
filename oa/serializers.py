from collections import OrderedDict

from rest_framework import serializers
from rest_framework.fields import SkipField

from user.serializers import ModelSerializer, DynamicFieldsModelSerializer, UserListSerializer
from .models import *


# --------------------------------- 邮件模板 ---------------------------------
# 创建邮件模板
class EmailTemplateCreateSerializer(ModelSerializer):
    class Meta:
        model = EmailTemplate
        fields = ('branch', 'name', 'content')


# 列表邮件模板
class EmailTemplateListSerializer(ModelSerializer):
    class Meta:
        model = EmailTemplate
        fields = ('id', 'branch', 'name', 'content')


# 邮件模板
class EmailTemplateSerializer(ModelSerializer):
    class Meta:
        model = EmailTemplate
        fields = ('id', 'branch', 'name', 'content')


# --------------------------------- 邮件 ---------------------------------
# 创建邮件
class EmailCreateSerializer(ModelSerializer):
    class Meta:
        model = Email
        fields = ('from_user', 'to_user', 'content')


# 列表邮件
class EmailListSerializer(ModelSerializer):
    class Meta:
        model = Email
        fields = ('id', 'from_user', 'to_user', 'content', 'is_read')


# 邮件
class EmailSerializer(ModelSerializer):
    class Meta:
        model = Email
        fields = ('id', 'from_user', 'to_user', 'content', 'is_read')


# --------------------------------- 通知模板 ---------------------------------
# 创建通知模板
class NotificationTemplateCreateSerializer(ModelSerializer):
    class Meta:
        model = NotificationTemplate
        fields = ('branch', 'name', 'content')


# 列表通知模板
class NotificationTemplateListSerializer(ModelSerializer):
    class Meta:
        model = NotificationTemplate
        fields = ('id', 'branch', 'name', 'content')


# 通知模板
class NotificationTemplateSerializer(ModelSerializer):
    class Meta:
        model = NotificationTemplate
        fields = ('id', 'branch', 'name', 'content')


# --------------------------------- 通知 ---------------------------------
# 创建通知
class NotificationCreateSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ('from_user', 'content', 'is_active', 'groups')


# 列表通知
class NotificationListSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'from_user', 'content', 'is_active', 'groups')


# 通知
class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'from_user', 'content', 'is_active', 'groups')


# --------------------------------- 工作报告模板 ---------------------------------
# 创建工作报告模板
class WorkReportTemplateCreateSerializer(ModelSerializer):
    class Meta:
        model = WorkReportTemplate
        fields = ('branch', 'name', 'content')


# 列表工作报告模板
class WorkReportTemplateListSerializer(ModelSerializer):
    class Meta:
        model = WorkReportTemplate
        fields = ('id', 'branch', 'name', 'content')


# 工作报告模板
class WorkReportTemplateSerializer(ModelSerializer):
    class Meta:
        model = WorkReportTemplate
        fields = ('id', 'branch', 'name', 'content')


# --------------------------------- 工作报告 ---------------------------------
# 创建工作报告
class WorkReportCreateSerializer(ModelSerializer):
    class Meta:
        model = WorkReport
        fields = ('report_user', 'content')


# 列表工作报告
class WorkReportListSerializer(ModelSerializer):
    class Meta:
        model = WorkReport
        fields = ('id', 'report_user', 'content')


# 工作报告
class WorkReportSerializer(ModelSerializer):
    class Meta:
        model = WorkReport
        fields = ('id', 'report_user', 'content')