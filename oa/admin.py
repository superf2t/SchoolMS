from django.contrib import admin

from .models import *


# 邮件模板
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    search_fields = ('name',)
admin.site.register(EmailTemplate, EmailTemplateAdmin)


# 邮件
class EmailAdmin(admin.ModelAdmin):
    list_display = ['id', 'from_user', 'to_user', 'is_read']
    search_fields = ('from_user__username', 'to_user__username', )
admin.site.register(Email, EmailAdmin)


# 通知模板
class NotificationTemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    search_fields = ('name',)
admin.site.register(NotificationTemplate, NotificationTemplateAdmin)


# 通知
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'from_user', 'get_group_name', 'is_active', ]
    filter_horizontal = ('groups',)
    search_fields = ('name',)
admin.site.register(Notification, NotificationAdmin)


# 工作报告模板
class WorkReportTemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    search_fields = ('name',)
admin.site.register(WorkReportTemplate, WorkReportTemplateAdmin)

# 员工工作报告
class WorkReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'report_user']
    search_fields = ('report_user__username', )
admin.site.register(WorkReport, WorkReportAdmin)
