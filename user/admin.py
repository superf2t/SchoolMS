from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'get_full_name', 'gender', ]
    filter_horizontal = ('groups', 'branches')
    search_fields = ('username',)
admin.site.register(User, UserAdmin)


# 生产环境下取消
class TokenAdmin(admin.ModelAdmin):
    list_display = ['user', 'access_token', 'refresh_token']
    search_fields = ('user',)
admin.site.register(Token, TokenAdmin)
