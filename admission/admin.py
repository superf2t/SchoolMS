from django.contrib import admin

from .models import *


# 准学员来源
class PreStudentSourceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    search_fields = ('name',)
admin.site.register(PreStudentSource, PreStudentSourceAdmin)


# 准学员所属年级
class PreStudentClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    search_fields = ('name',)
admin.site.register(PreStudentClass, PreStudentClassAdmin)


# 准学员所属学校
class PreStudentSchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    search_fields = ('name',)
admin.site.register(PreStudentSchool, PreStudentSchoolAdmin)


# 准学员分类
class PreStudentCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    search_fields = ('name',)
admin.site.register(PreStudentCategory, PreStudentCategoryAdmin)


# 准学员
class PreStudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_following', ]
    filter_horizontal = ('courses', )
    search_fields = ('user__name',)
admin.site.register(PreStudent, PreStudentAdmin)


# 准学员联系人
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'tel', 'category']
    search_fields = ('name',)
admin.site.register(Contact, ContactAdmin)


# 咨询标签
class ConsultTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    search_fields = ('name',)
admin.site.register(ConsultTag, ConsultTagAdmin)


# 咨询
class ConsultAdmin(admin.ModelAdmin):
    list_display = ['id']
    search_fields = ('name',)
    filter_horizontal = ('contacts', 'tags', 'courses')
admin.site.register(Consult, ConsultAdmin)


# 邀约
class InvitationAdmin(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(Invitation, InvitationAdmin)


# 试听
class AuditionRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_consult', 'get_course']
    search_fields = ('consult__name', 'course__name')

    def get_consult(self, obj):
        return obj.consult.name
    get_consult.short_description = '咨询记录'

    def get_course(self, obj):
        return obj.course.name
    get_course.short_description = '试听课程'
admin.site.register(AuditionRecord, AuditionRecordAdmin)


# 推荐记录
class RecommendRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'from_user_tel', 'time']
    list_filter = ('is_rebate', )
admin.site.register(RecommendRecord, RecommendRecordAdmin)