from django.contrib import admin

from .models import *


class NoticeAdmin(admin.ModelAdmin):
    list_display = ['id', 'from_user', 'get_branches_name', 'is_publish']
    search_fields = ('from_user__username',)
    filter_horizontal = ('branches',)
    list_filter = ('is_publish', 'is_top')
admin.site.register(Notice, NoticeAdmin)


class NoticeTemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    search_fields = ('name',)
admin.site.register(NoticeTemplate, NoticeTemplateAdmin)


class SMSAdmin(admin.ModelAdmin):
    list_display = ['id', 'from_user', 'to_users', 'content']
    search_fields = ('from_user__username', 'content',)
admin.site.register(SMS, SMSAdmin)


class SMSTemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    search_fields = ('name',)
admin.site.register(SMSTemplate, SMSTemplateAdmin)


class SMSRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'from_user', 'to_user_name', 'to_user_tel']
    search_fields = ('from_user__username', 'to_user_name', 'to_user_tel')
admin.site.register(SMSRecord, SMSRecordAdmin)


class SMSAssignAdmin(admin.ModelAdmin):
    list_display = ['id', 'branch', 'user', 'assign_sum', 'used', 'remain', 'auto_reset']
    search_fields = ('user__username', )
admin.site.register(SMSAssign, SMSAssignAdmin)