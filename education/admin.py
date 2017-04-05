from django.contrib import admin

from .models import *


# 课程分类
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    search_fields = ('name',)
admin.site.register(CourseCategory, CourseCategoryAdmin)


# 学员
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'card_no', 'student_no']
    search_fields = ('id',)
admin.site.register(Student, StudentAdmin)


# 课程
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    search_fields = ('name',)
admin.site.register(Course, CourseAdmin)


# 教室
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'place']
    search_fields = ('name',)
admin.site.register(ClassRoom, ClassRoomAdmin)


# 班级
class ClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacher', 'class_room']
    search_fields = ('teacher__user__name', 'class_room__name')
    filter_horizontal = ('course', 'students')
admin.site.register(Class, ClassAdmin)


# 课程表单条记录
class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'start_time', 'end_time', 'class_room']
    search_fields = ('teacher__user__name', 'class_room__name')
admin.site.register(ClassSchedule, ClassScheduleAdmin)


# 临时调课记录
class TemporaryClassScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'operate']
    list_filter = ('operate', )
admin.site.register(TemporaryClassSchedule, TemporaryClassScheduleAdmin)


# 学员考勤记录
class StudentAttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'time']
    list_filter = ('status', )
admin.site.register(StudentAttendanceRecord, StudentAttendanceRecordAdmin)


# 教师考勤记录
class TeacherAttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'time']
    list_filter = ('status', )
admin.site.register(TeacherAttendanceRecord, TeacherAttendanceRecordAdmin)


# 学员课消记录
class ClassExpenseRecordAdmin(admin.ModelAdmin):
    list_display = ['id',]
admin.site.register(ClassExpenseRecord, ClassExpenseRecordAdmin)