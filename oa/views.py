from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status, viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.permissions import IsAuthenticated

from user.views import success_response, error_response, logger
from user.permissions import permission_required, group_required
from .models import *
from .serializers import *
from logger.views import add_log, queryset_str


# 邮件模板视图集
class EmailTemplateViewSet(viewsets.ModelViewSet):
    queryset = EmailTemplate.objects.all()
    serializer_class = EmailTemplateCreateSerializer
    permission_classes = (IsAuthenticated,)

    # override POST /email_template/
    # 添加邮件模板
    # Receive ----------------------------------
    # name: 邮件模板名称
    # Return -----------------------------------
    # 200 添加成功 400-1 数据格式错误
    def create(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.add_emailtemplate'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # 添加邮件模板
            email_template = serializer.create(serializer.validated_data)

            add_log(request.user, 1, '添加邮件模板 %s' % email_template.name)
            return success_response('添加成功')
        else:
            return error_response(1, serializer.errors)

    # override GET /email_template/
    # 查看邮件模板
    def list(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_emailtemplate'])
        email_templates = EmailTemplate.objects.all()
        serializer = EmailTemplateListSerializer(email_templates, context={'request': request}, many=True)
        return success_response(serializer.data)

    # override GET /email_template/email_template_id/
    # 获取邮件模板详情
    # Return -----------------------------------
    # 200 查看成功 400-1 邮件模板不存在
    def retrieve(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_emailtemplate'])
        try:
            email_template = EmailTemplate.objects.get(pk=kwargs['pk'])
            serializer = EmailTemplateSerializer(email_template, context={'request': request})
            return success_response(serializer.data)
        except ObjectDoesNotExist:
            return error_response(1, '邮件模板不存在')

    # override PUT /email_template/email_template_id/
    # 部分更新邮件模板
    # Return -----------------------------------
    # 200 邮件模板信息 400-1 数据格式错误
    def update(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.change_emailtemplate'])
        email_template = EmailTemplate.objects.get(pk=kwargs['pk'])
        serializer = EmailTemplateSerializer(email_template, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            add_log(request.user, 2, '修改邮件模板 %s，%s' % (email_template.name, queryset_str(request.data)))
            return success_response(serializer.data)
        else:
            return error_response(1, serializer.errors)

    # override Delete /email_template/email_template_id/
    # 删除邮件模板
    # Return -----------------------------------
    # 200 删除成功 400-1 邮件模板不存在
    def destroy(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.delete_emailtemplate'])
        try:
            email_template = EmailTemplate.objects.get(pk=kwargs['pk'])
            add_log(request.user, 3, '删除邮件模板 %s' % email_template.name)
            email_template.delete()
            return success_response('删除成功')
        except ObjectDoesNotExist:
            return error_response(1, '邮件模板不存在')


# 邮件视图集
class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailCreateSerializer
    permission_classes = (IsAuthenticated,)

    # override POST /email/
    # 添加邮件
    # Receive ----------------------------------
    # name: 邮件名称
    # Return -----------------------------------
    # 200 添加成功 400-1 数据格式错误
    def create(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.add_email'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # 添加邮件
            email = serializer.create(serializer.validated_data)

            add_log(request.user, 1, '添加邮件 %s' % email.name)
            return success_response('添加成功')
        else:
            return error_response(1, serializer.errors)

    # override GET /email/
    # 查看邮件
    def list(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_email'])
        email = Email.objects.all()
        serializer = EmailListSerializer(email, context={'request': request}, many=True)
        return success_response(serializer.data)

    # override GET /email/email_id/
    # 获取邮件详情
    # Return -----------------------------------
    # 200 查看成功 400-1 邮件不存在
    def retrieve(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_email'])
        try:
            email = Email.objects.get(pk=kwargs['pk'])
            serializer = EmailSerializer(email, context={'request': request})
            return success_response(serializer.data)
        except ObjectDoesNotExist:
            return error_response(1, '邮件不存在')

    # override PUT /email/email_id/
    # 部分更新邮件
    # Return -----------------------------------
    # 200 邮件信息 400-1 数据格式错误
    def update(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.change_email'])
        email = Email.objects.get(pk=kwargs['pk'])
        serializer = EmailSerializer(email, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            add_log(request.user, 2, '修改邮件 %s，%s' % (email.name, queryset_str(request.data)))
            return success_response(serializer.data)
        else:
            return error_response(1, serializer.errors)

    # override Delete /email/email_id/
    # 删除邮件
    # Return -----------------------------------
    # 200 删除成功 400-1 邮件不存在
    def destroy(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.delete_email'])
        try:
            email = Email.objects.get(pk=kwargs['pk'])
            add_log(request.user, 3, '删除邮件 %s' % email.name)
            email.delete()
            return success_response('删除成功')
        except ObjectDoesNotExist:
            return error_response(1, '邮件不存在')


# 通知模板视图集
class NotificationTemplateViewSet(viewsets.ModelViewSet):
    queryset = NotificationTemplate.objects.all()
    serializer_class = NotificationTemplateCreateSerializer
    permission_classes = (IsAuthenticated,)

    # override POST /notification_template/
    # 添加通知模板
    # Receive ----------------------------------
    # name: 通知模板名称
    # Return -----------------------------------
    # 200 添加成功 400-1 数据格式错误
    def create(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.add_notificationtemplate'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # 添加通知模板
            notification_template = serializer.create(serializer.validated_data)

            add_log(request.user, 1, '添加通知模板 %s' % notification_template.name)
            return success_response('添加成功')
        else:
            return error_response(1, serializer.errors)

    # override GET /notification_template/
    # 查看通知模板
    def list(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_notificationtemplate'])
        notification_templates = NotificationTemplate.objects.all()
        serializer = NotificationTemplateListSerializer(notification_templates, context={'request': request}, many=True)
        return success_response(serializer.data)

    # override GET /notification_template/notification_template_id/
    # 获取通知模板详情
    # Return -----------------------------------
    # 200 查看成功 400-1 通知模板不存在
    def retrieve(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_notificationtemplate'])
        try:
            notification_templates = NotificationTemplate.objects.get(pk=kwargs['pk'])
            serializer = NotificationTemplateSerializer(notification_templates, context={'request': request})
            return success_response(serializer.data)
        except ObjectDoesNotExist:
            return error_response(1, '通知模板不存在')

    # override PUT /notification_template/notification_template_id/
    # 部分更新通知模板
    # Return -----------------------------------
    # 200 通知模板信息 400-1 数据格式错误
    def update(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.change_notificationtemplate'])
        notification_template = NotificationTemplate.objects.get(pk=kwargs['pk'])
        serializer = NotificationTemplateSerializer(notification_template, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            add_log(request.user, 2, '修改通知模板 %s，%s' % (notification_template.name, queryset_str(request.data)))
            return success_response(serializer.data)
        else:
            return error_response(1, serializer.errors)

    # override Delete /notification_template/notification_template_id/
    # 删除通知模板
    # Return -----------------------------------
    # 200 删除成功 400-1 通知模板不存在
    def destroy(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.delete_notificationtemplate'])
        try:
            notification_template = NotificationTemplate.objects.get(pk=kwargs['pk'])
            add_log(request.user, 3, '删除通知模板 %s' % notification_template.name)
            notification_template.delete()
            return success_response('删除成功')
        except ObjectDoesNotExist:
            return error_response(1, '通知模板不存在')


# 通知视图集
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationCreateSerializer
    permission_classes = (IsAuthenticated,)

    # override POST /notification/
    # 添加通知
    # Receive ----------------------------------
    # Return -----------------------------------
    # 200 添加成功 400-1 数据格式错误
    def create(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.add_notification'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # 添加通知
            notification = serializer.create(serializer.validated_data)

            add_log(request.user, 1, '添加通知 %s' % notification.name)
            return success_response('添加成功')
        else:
            return error_response(1, serializer.errors)

    # override GET /notification/
    # 查看通知
    def list(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_notification'])
        notifications = Notification.objects.all()
        serializer = NotificationListSerializer(notifications, context={'request': request}, many=True)
        return success_response(serializer.data)

    # override GET /notification/notification_id/
    # 获取通知详情
    # Return -----------------------------------
    # 200 查看成功 400-1 通知不存在
    def retrieve(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_notification'])
        try:
            notification = Notification.objects.get(pk=kwargs['pk'])
            serializer = NotificationSerializer(notification, context={'request': request})
            return success_response(serializer.data)
        except ObjectDoesNotExist:
            return error_response(1, '通知不存在')

    # override PUT /notification/notification_id/
    # 部分更新通知
    # Return -----------------------------------
    # 200 通知信息 400-1 数据格式错误
    def update(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.change_notification'])
        notification = Notification.objects.get(pk=kwargs['pk'])
        serializer = NotificationSerializer(notification, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            add_log(request.user, 2, '修改通知 %s，%s' % (notification.name, queryset_str(request.data)))
            return success_response(serializer.data)
        else:
            return error_response(1, serializer.errors)

    # override Delete /notification/notification_id/
    # 删除通知
    # Return -----------------------------------
    # 200 删除成功 400-1 通知不存在
    def destroy(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.delete_notification'])
        try:
            notification = Notification.objects.get(pk=kwargs['pk'])
            add_log(request.user, 3, '删除通知 %s' % notification.from_user.name)
            notification.delete()
            return success_response('删除成功')
        except ObjectDoesNotExist:
            return error_response(1, '通知不存在')


# 工作报告模板
class WorkReportTemplateViewSet(viewsets.ModelViewSet):
    queryset = WorkReportTemplate.objects.all()
    serializer_class = WorkReportTemplateCreateSerializer
    permission_classes = (IsAuthenticated,)

    # override POST /work_report_template/
    # 添加工作报告模板
    # Receive ----------------------------------
    # name: 工作报告模板名称
    # Return -----------------------------------
    # 200 添加成功 400-1 数据格式错误
    def create(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.add_workreporttemplate'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # 添加工作报告模板
            work_report_template = serializer.create(serializer.validated_data)

            add_log(request.user, 1, '添加工作报告模板 %s' % work_report_template.name)
            return success_response('添加成功')
        else:
            return error_response(1, serializer.errors)

    # override GET /work_report_template/
    # 查看工作报告模板
    def list(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_workreporttemplate'])
        work_report_template = WorkReportTemplate.objects.all()
        serializer = WorkReportTemplateListSerializer(work_report_template, context={'request': request}, many=True)
        return success_response(serializer.data)

    # override GET /work_report_template/work_report_template_id/
    # 获取工作报告模板
    # Return -----------------------------------
    # 200 查看成功 400-1 工作报告模板不存在
    def retrieve(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_workreporttemplate'])
        try:
            work_report_template = WorkReportTemplate.objects.get(pk=kwargs['pk'])
            serializer = WorkReportTemplateSerializer(work_report_template, context={'request': request})
            return success_response(serializer.data)
        except ObjectDoesNotExist:
            return error_response(1, '工作报告模板不存在')

    # override PUT /work_report_template/work_report_template_id/
    # 部分工作报告模板
    # Return -----------------------------------
    # 200 工作报告模板信息 400-1 数据格式错误
    def update(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.change_workreporttemplate'])
        work_report_template = WorkReportTemplate.objects.get(pk=kwargs['pk'])
        serializer = WorkReportTemplateSerializer(work_report_template, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            add_log(request.user, 2, '修改工作报告模板 %s，%s' % (work_report_template.name, queryset_str(request.data)))
            return success_response(serializer.data)
        else:
            return error_response(1, serializer.errors)

    # override Delete /work_report_template/work_report_template_id/
    # 删除工作报告模板
    # Return -----------------------------------
    # 200 删除成功 400-1 工作报告模板不存在
    def destroy(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.delete_workreporttemplate'])
        try:
            work_report_template = WorkReportTemplate.objects.get(pk=kwargs['pk'])
            add_log(request.user, 3, '删除工作报告模板 %s' % work_report_template.name)
            work_report_template.delete()
            return success_response('删除成功')
        except ObjectDoesNotExist:
            return error_response(1, '工作报告模板不存在')


# 工作报告
class WorkReportViewSet(viewsets.ModelViewSet):
    queryset = WorkReport.objects.all()
    serializer_class = WorkReportCreateSerializer
    permission_classes = (IsAuthenticated,)

    # override POST /work_report/
    # 添加工作报告
    # Receive ----------------------------------
    # name: 工作报告名称
    # Return -----------------------------------
    # 200 添加成功 400-1 数据格式错误
    def create(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.add_workreport'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # 添加工作报告
            work_report = serializer.create(serializer.validated_data)

            add_log(request.user, 1, '添加工作报告 %s' % work_report.name)
            return success_response('添加成功')
        else:
            return error_response(1, serializer.errors)

    # override GET /work_report/
    # 查看工作报告
    def list(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_workreport'])
        work_report = WorkReport.objects.all()
        serializer = WorkReportListSerializer(work_report, context={'request': request}, many=True)
        return success_response(serializer.data)

    # override GET /work_report/work_report_id/
    # 获取工作报告
    # Return -----------------------------------
    # 200 查看成功 400-1 工作报告不存在
    def retrieve(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_workreport'])
        try:
            work_report = WorkReport.objects.get(pk=kwargs['pk'])
            serializer = WorkReportSerializer(work_report, context={'request': request})
            return success_response(serializer.data)
        except ObjectDoesNotExist:
            return error_response(1, '工作报告不存在')

    # override PUT /work_report/work_report_id/
    # 部分工作报告
    # Return -----------------------------------
    # 200 工作报告信息 400-1 数据格式错误
    def update(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.change_workreport'])
        work_report = WorkReport.objects.get(pk=kwargs['pk'])
        serializer = WorkReportSerializer(work_report, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            add_log(request.user, 2, '修改工作报告 %s，%s' % (work_report.name, queryset_str(request.data)))
            return success_response(serializer.data)
        else:
            return error_response(1, serializer.errors)

    # override Delete /work_report/work_report_id/
    # 删除工作报告
    # Return -----------------------------------
    # 200 删除成功 400-1 工作报告不存在
    def destroy(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.delete_workreport'])
        try:
            work_report = WorkReport.objects.get(pk=kwargs['pk'])
            add_log(request.user, 3, '删除工作报告 %s' % work_report.report_user.name)
            work_report.delete()
            return success_response('删除成功')
        except ObjectDoesNotExist:
            return error_response(1, '工作报告不存在')
