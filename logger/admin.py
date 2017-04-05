from django.contrib import admin

from .models import *


# 操作日志
class LoggerAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user', 'category', 'content', 'update_time')
    search_fields = ('user__name', )
    list_filter = ('is_abandon', 'category')

    def get_user(self, obj):
        return obj.user.get_full_name()
    get_user.short_description = '操作人'
admin.site.register(Logger, LoggerAdmin)
