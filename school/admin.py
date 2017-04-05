from django.contrib import admin

from .models import *


# 学校
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'list_order', ]
    filter_horizontal = ('branches', 'departments', )
    search_fields = ('name',)
admin.site.register(School, SchoolAdmin)


# 校区
class BranchAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'list_order', ]
    filter_horizontal = ('departments',)
    search_fields = ('name',)
admin.site.register(Branch, BranchAdmin)


# 部门
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'list_order', ]
    filter_horizontal = ('departments', 'staffs',)
    search_fields = ('name',)
admin.site.register(Department, DepartmentAdmin)


# 员工
class StaffAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_no', 'bank_no', 'social_security_no', 'on_job', 'job_state']
    search_fields = ('name',)
admin.site.register(Staff, StaffAdmin)