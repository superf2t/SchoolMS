from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status, viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.permissions import IsAuthenticated

from user.views import success_response, error_response, logger
from user.permissions import permission_required, group_required
from .models import *
from .serializers import *
from logger.views import add_log, queryset_str


# 公告模板视图集
class NotificationTemplateViewSet(viewsets.ModelViewSet):
    queryset = NoticeTemplate.objects.all()
    serializer_class = NoticeTemplateCreateSerializer
    permission_classes = (IsAuthenticated,)

    # override POST /notice_template/
    # 添加公告模板
    # Receive ----------------------------------
    # name: 公告模板名称
    # Return -----------------------------------
    # 200 添加成功 400-1 数据格式错误
    def create(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.add_noticetemplate'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # 添加公告模板
            notice_template = serializer.create(serializer.validated_data)

            add_log(request.user, 1, '添加公告模板 %s' % notice_template.name)
            return success_response('添加成功')
        else:
            return error_response(1, serializer.errors)

    # override GET /notice_template/
    # 查看公告模板
    def list(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_noticetemplate'])
        notice_template = NoticeTemplate.objects.all()
        serializer = NoticeTemplateListSerializer(notice_template, context={'request': request}, many=True)
        return success_response(serializer.data)

    # override GET /notice_template/notice_template_id/
    # 获取公告模板详情
    # Return -----------------------------------
    # 200 查看成功 400-1 公告模板不存在
    def retrieve(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_noticetemplate'])
        try:
            notice_template = NoticeTemplate.objects.get(pk=kwargs['pk'])
            serializer = NoticeTemplateSerializer(notice_template, context={'request': request})
            return success_response(serializer.data)
        except ObjectDoesNotExist:
            return error_response(1, '公告模板不存在')

    # override PUT /notice_template/notice_template_id/
    # 部分更新公告模板
    # Return -----------------------------------
    # 200 公告模板信息 400-1 数据格式错误
    def update(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.change_noticetemplate'])
        notice_template = NoticeTemplate.objects.get(pk=kwargs['pk'])
        serializer = NoticeTemplateSerializer(notice_template, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            add_log(request.user, 2, '修改公告模板 %s，%s' % (notice_template.name, queryset_str(request.data)))
            return success_response(serializer.data)
        else:
            return error_response(1, serializer.errors)

    # override Delete /notice_template/notice_template_id/
    # 删除公告模板
    # Return -----------------------------------
    # 200 删除成功 400-1 公告模板不存在
    def destroy(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.delete_noticetemplate'])
        try:
            notice_template = NoticeTemplate.objects.get(pk=kwargs['pk'])
            add_log(request.user, 3, '删除公告模板 %s' % notice_template.name)
            notice_template.delete()
            return success_response('删除成功')
        except ObjectDoesNotExist:
            return error_response(1, '公告模板不存在')


# 公告视图集
class EmailTemplateViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeCreateSerializer
    permission_classes = (IsAuthenticated,)

    # override POST /notice/
    # 添加公告
    # Receive ----------------------------------

    # Return -----------------------------------
    # 200 添加成功 400-1 数据格式错误
    def create(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.add_notice'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # 添加公告
            notice = serializer.create(serializer.validated_data)

            add_log(request.user, 1, '添加公告 %s' % notice.content)
            return success_response('添加成功')
        else:
            return error_response(1, serializer.errors)

    # override GET /notice/
    # 查看公告
    def list(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_notice'])
        notice = Notice.objects.all()
        serializer = NoticeListSerializer(notice, context={'request': request}, many=True)
        return success_response(serializer.data)

    # override GET /notice/notice_id/
    # 获取公告详情
    # Return -----------------------------------
    # 200 查看成功 400-1公告不存在
    def retrieve(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_notice'])
        try:
            notice = Notice.objects.get(pk=kwargs['pk'])
            serializer = NoticeSerializer(notice, context={'request': request})
            return success_response(serializer.data)
        except ObjectDoesNotExist:
            return error_response(1, '公告不存在')

    # override PUT /notice/notice_id/
    # 部分更新公告
    # Return -----------------------------------
    # 200 公告信息 400-1 数据格式错误
    def update(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.change_notice'])
        notice = Notice.objects.get(pk=kwargs['pk'])
        serializer = NoticeSerializer(notice, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            add_log(request.user, 2, '修改公告 %s，%s' % (notice.content, queryset_str(request.data)))
            return success_response(serializer.data)
        else:
            return error_response(1, serializer.errors)

    # override Delete /notice/notice_id/
    # 删除公告
    # Return -----------------------------------
    # 200 删除成功 400-1 公告不存在
    def destroy(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.delete_notice'])
        try:
            notice = Notice.objects.get(pk=kwargs['pk'])
            add_log(request.user, 3, '删除公告 %s' % notice.name)
            notice.delete()
            return success_response('删除成功')
        except ObjectDoesNotExist:
            return error_response(1, '公告不存在')


# 短信模板视图集
class SMSTemplateViewSet(viewsets.ModelViewSet):
    queryset = SMSTemplate.objects.all()
    serializer_class = SMSTemplateCreateSerializer
    permission_classes = (IsAuthenticated,)

    # override POST /sms_template/
    # 添加短信模板
    # Receive ----------------------------------
    # name: 短信模板名称
    # Return -----------------------------------
    # 200 添加成功 400-1 数据格式错误
    def create(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.add_smstemplate'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # 添加短信模板
            sms_template = serializer.create(serializer.validated_data)

            add_log(request.user, 1, '添加短信模板 %s' % sms_template.name)
            return success_response('添加成功')
        else:
            return error_response(1, serializer.errors)

    # override GET /sms_template/
    # 查看短信模板
    def list(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_smstemplate'])
        sms_templates = SMSTemplate.objects.all()
        serializer = SMSTemplateListSerializer(sms_templates, context={'request': request}, many=True)
        return success_response(serializer.data)

    # override GET /sms_template/sms_template_id/
    # 获取短信模板详情
    # Return -----------------------------------
    # 200 查看成功 400-1 短信模板不存在
    def retrieve(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_smstemplate'])
        try:
            sms_template = SMSTemplate.objects.get(pk=kwargs['pk'])
            serializer = SMSTemplateSerializer(sms_template, context={'request': request})
            return success_response(serializer.data)
        except ObjectDoesNotExist:
            return error_response(1, '短信模板不存在')

    # override PUT /sms_template/sms_template_id/
    # 部分更新短信模板
    # Return -----------------------------------
    # 200 短信模板信息 400-1 数据格式错误
    def update(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.change_smstemplate'])
        sms_template = SMSTemplate.objects.get(pk=kwargs['pk'])
        serializer = SMSTemplateSerializer(sms_template, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            add_log(request.user, 2, '修改短信模板 %s，%s' % (sms_template.name, queryset_str(request.data)))
            return success_response(serializer.data)
        else:
            return error_response(1, serializer.errors)

    # override Delete /sms_template/sms_template_id/
    # 删除短信模板
    # Return -----------------------------------
    # 200 删除成功 400-1 短信模板不存在
    def destroy(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.delete_smstemplate'])
        try:
            sms_template = SMSTemplate.objects.get(pk=kwargs['pk'])
            add_log(request.user, 3, '删除短信模板 %s' % sms_template.name)
            sms_template.delete()
            return success_response('删除成功')
        except ObjectDoesNotExist:
            return error_response(1, '短信模板不存在')


# 短信视图集
class SMSViewSet(viewsets.ModelViewSet):
    queryset = SMS.objects.all()
    serializer_class = SMSCreateSerializer
    permission_classes = (IsAuthenticated,)

    # override POST /sms/
    # 添加短信
    # Receive ----------------------------------
    # name: 短信名称
    # Return -----------------------------------
    # 200 添加成功 400-1 数据格式错误
    def create(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.add_sms'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # 添加短信
            sms = serializer.create(serializer.validated_data)

            add_log(request.user, 1, '添加短信 %s' % sms.name)
            return success_response('添加成功')
        else:
            return error_response(1, serializer.errors)

    # override GET /sms/
    # 查看短信
    def list(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_sms'])
        sms_templates = SMS.objects.all()
        serializer = SMSListSerializer(sms_templates, context={'request': request}, many=True)
        return success_response(serializer.data)

    # override GET /sms/sms_id/
    # 获取短信详情
    # Return -----------------------------------
    # 200 查看成功 400-1 短信不存在
    def retrieve(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_sms'])
        try:
            sms = SMS.objects.get(pk=kwargs['pk'])
            serializer = SMSSerializer(sms, context={'request': request})
            return success_response(serializer.data)
        except ObjectDoesNotExist:
            return error_response(1, '短信不存在')

    # override PUT /sms/sms_id/
    # 部分更新短信
    # Return -----------------------------------
    # 200 短信信息 400-1 数据格式错误
    def update(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.change_sms'])
        sms = SMS.objects.get(pk=kwargs['pk'])
        serializer = SMSSerializer(sms, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            add_log(request.user, 2, '修改短信 %s，%s' % (sms.name, queryset_str(request.data)))
            return success_response(serializer.data)
        else:
            return error_response(1, serializer.errors)

    # override Delete /sms/sms_id/
    # 删除短信
    # Return -----------------------------------
    # 200 删除成功 400-1 短信不存在
    def destroy(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.delete_sms'])
        try:
            sms = SMS.objects.get(pk=kwargs['pk'])
            add_log(request.user, 3, '删除短信 %s' % sms.content)
            sms.delete()
            return success_response('删除成功')
        except ObjectDoesNotExist:
            return error_response(1, '短信不存在')


# 短信记录视图集
class SMSRecordViewSet(viewsets.ModelViewSet):
    queryset = SMSRecord.objects.all()
    serializer_class = SMSRecordCreateSerializer
    permission_classes = (IsAuthenticated,)

    # override POST /sms_record/
    # 添加短信记录
    # Receive ----------------------------------
    # Return -----------------------------------
    # 200 添加成功 400-1 数据格式错误
    def create(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.add_smsrecord'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # 添加短信
            sms = serializer.create(serializer.validated_data)

            add_log(request.user, 1, '添加短信记录 %s' % sms.to_user_tel)
            return success_response('添加成功')
        else:
            return error_response(1, serializer.errors)

    # override GET /sms_record/
    # 查看短信记录
    def list(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_smsrecord'])
        sms_records = SMSRecord.objects.all()
        serializer = SMSRecordListSerializer(sms_records, context={'request': request}, many=True)
        return success_response(serializer.data)

    # override GET /sms_record/sms_record_id/
    # 获取短信记录详情
    # Return -----------------------------------
    # 200 查看成功 400-1 短信记录不存在
    def retrieve(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_smsrecord'])
        try:
            sms_record = SMSRecord.objects.get(pk=kwargs['pk'])
            serializer = SMSRecordSerializer(sms_record, context={'request': request})
            return success_response(serializer.data)
        except ObjectDoesNotExist:
            return error_response(1, '短信记录不存在')

    # override PUT /sms_record/sms_record_id/
    # 部分更新短信记录
    # Return -----------------------------------
    # 200 短信记录信息 400-1 数据格式错误
    def update(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.change_smsrecord'])
        sms_record = SMSRecord.objects.get(pk=kwargs['pk'])
        serializer = SMSRecordSerializer(sms_record, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            add_log(request.user, 2, '修改短信记录 %s，%s' % (sms_record.to_user_tel, queryset_str(request.data)))
            return success_response(serializer.data)
        else:
            return error_response(1, serializer.errors)

    # override Delete /sms_record/sms_id/
    # 删除短信记录
    # Return -----------------------------------
    # 200 删除成功 400-1 短信记录不存在
    def destroy(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.delete_smsrecord'])
        try:
            sms_record = SMSRecord.objects.get(pk=kwargs['pk'])
            add_log(request.user, 3, '删除短信 %s' % sms_record.content)
            sms_record.delete()
            return success_response('删除成功')
        except ObjectDoesNotExist:
            return error_response(1, '短信记录不存在')


# 短信分配视图集
class SMSAssignViewSet(viewsets.ModelViewSet):
    queryset = SMSAssign.objects.all()
    serializer_class = SMSAssignCreateSerializer
    permission_classes = (IsAuthenticated,)

    # override POST /sms_assign/
    # 添加短信分配
    # Receive ----------------------------------
    # Return -----------------------------------
    # 200 添加成功 400-1 数据格式错误
    def create(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.add_smsassign'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # 添加短信分配
            sms_assign = serializer.create(serializer.validated_data)

            add_log(request.user, 1, '添加短信分配 %s' % sms_assign.user.get_full_name())
            return success_response('添加成功')
        else:
            return error_response(1, serializer.errors)

    # override GET /sms_assign/
    # 查看短信分配
    def list(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_smsassign'])
        sms_assigns = SMSAssign.objects.all()
        serializer = SMSAssignListSerializer(sms_assigns, context={'request': request}, many=True)
        return success_response(serializer.data)

    # override GET /sms_assign/sms_assign_id/
    # 获取短信分配详情
    # Return -----------------------------------
    # 200 查看成功 400-1 短信分配不存在
    def retrieve(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.view_smsassign'])
        try:
            sms_assign = SMSAssign.objects.get(pk=kwargs['pk'])
            serializer = SMSAssignSerializer(sms_assign, context={'request': request})
            return success_response(serializer.data)
        except ObjectDoesNotExist:
            return error_response(1, '短信分配不存在')

    # override PUT /sms_assign/sms_assign_id/
    # 部分更新短信分配
    # Return -----------------------------------
    # 200 短信分配信息 400-1 数据格式错误
    def update(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.change_smsassign'])
        sms_assign = SMSAssign.objects.get(pk=kwargs['pk'])
        serializer = SMSAssignSerializer(sms_assign, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            add_log(request.user, 2, '修改短信分配 %s，%s' % (sms_assign.user.get_full_name(), queryset_str(request.data)))
            return success_response(serializer.data)
        else:
            return error_response(1, serializer.errors)

    # override Delete /sms_assign/sms_assign_id/
    # 删除短信分配
    # Return -----------------------------------
    # 200 删除成功 400-1 短信分配不存在
    def destroy(self, request, *args, **kwargs):
        permission_required(request.user, ['oa.delete_smsassign'])
        try:
            sms_assign = SMSAssign.objects.get(pk=kwargs['pk'])
            add_log(request.user, 3, '删除短信分配 %s' % sms_assign.user.get_full_name())
            sms_assign.delete()
            return success_response('删除成功')
        except ObjectDoesNotExist:
            return error_response(1, '短信分配不存在')