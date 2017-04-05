from django.db import models
from django.conf import settings
from django.utils import timezone

from user.storage import ImageStorage


# 课程分类
class CourseCategory(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='course_category_branch',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'校区')
    # 所属分类名称
    name = models.CharField(max_length=255,
                            null=True,
                            verbose_name=u'名称')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '课程分类'
        verbose_name_plural = '课程分类'

    def __str__(self):
        return self.name


# 学员
class Student(models.Model):
    # 准学员
    pre_student = models.ForeignKey('admission.PreStudent',
                                    related_name='student_pre_student',
                                    null=True,
                                    on_delete=models.SET_NULL,
                                    verbose_name=u'准学员')
    # 报名时间
    sign_up_time = models.DateTimeField(default=timezone.now,
                                        verbose_name=u'报名时间')
    # 卡号
    card_no = models.CharField(max_length=40,
                               null=True,
                               blank=True,
                               verbose_name=u'卡号')
    # 学号
    student_no = models.CharField(max_length=40,
                                  null=True,
                                  blank=True,
                                  verbose_name=u'学号')
    # 相片存储
    user_photo = ImageStorage(location=settings.MEDIA_ROOT + '/user/',
                              base_url='/media/user_photo/', )
    # 相片
    photo = models.ImageField(storage=user_photo,
                              blank=True,
                              default='default.png',
                              verbose_name=u'相片')
    # 报名课程
    courses = models.ManyToManyField('education.Course',
                                     blank=True,
                                     verbose_name=u'报名课程')

    class Meta:
        verbose_name = '学员'
        verbose_name_plural = '学员'

    def __str__(self):
        return self.pre_student.user.get_full_name()


# 课程
class Course(models.Model):
    # 是否限制校区
    restrict_branch = models.BooleanField(default=True,
                                          verbose_name=u'是否限制校区')
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='course_branch',
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'校区')
    # 课程名称
    name = models.CharField(max_length=255,
                            null=True,
                            verbose_name=u'名称')
    # 所属分类
    category = models.ForeignKey(CourseCategory,
                                 related_name='course_category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name=u'所属分类')
    # 课程类型
    COURSE_TYPE = {
        0: u'集体班',
        1: u'一对一',
    }
    course_type = models.IntegerField(choices=COURSE_TYPE.items(),
                                      null=True,
                                      verbose_name=u'课程类型')
    # 课程状态
    COURSE_STATE = {
        0: u'启用',
        1: u'停用',
    }
    course_state = models.IntegerField(choices=COURSE_STATE.items(),
                                       null=True,
                                       verbose_name=u'课程状态')
    # 计费方式
    CHARGE_MODE = {
        0: u'按课时',
        1: u'按期',
    }
    charge_mode = models.IntegerField(choices=CHARGE_MODE.items(),
                                      null=True,
                                      verbose_name=u'计费方式')
    # 总课时
    total_hours = models.IntegerField(default=0,
                                      verbose_name=u'总课时')
    # 课时单价
    unit_price = models.DecimalField(default=0.00,
                                     blank=True,
                                     max_digits=10,
                                     decimal_places=2,
                                     verbose_name=u'课时单价')
    # 课程总价
    total_price = models.DecimalField(default=0.00,
                                      max_digits=10,
                                      decimal_places=2,
                                      verbose_name=u'课程总价')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'

    def __str__(self):
        return self.name


# 教室
class ClassRoom(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='class_room_branch',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'校区')
    # 教室名称
    name = models.CharField(max_length=255,
                            null=True,
                            verbose_name=u'名称')
    # 具体地点
    place = models.CharField(max_length=255,
                             null=True,
                             verbose_name=u'具体地点')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '教室'
        verbose_name_plural = '教室'

    def __str__(self):
        return self.name


# 班级
class Class(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='class_branch',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'校区')
    # 课程 M2M 预留拓展
    course = models.ManyToManyField('education.Course',
                                    verbose_name=u'课程')
    # 学员
    students = models.ManyToManyField('education.Student',
                                      verbose_name=u'学员')
    # 教师
    teacher = models.ForeignKey('school.Staff',
                                related_name='class_teacher',
                                null=True,
                                on_delete=models.SET_NULL,
                                verbose_name=u'教师')
    # 教师课时费单价
    teacher_unit_price = models.DecimalField(default=0.00,
                                             blank=True,
                                             max_digits=10,
                                             decimal_places=2,
                                             verbose_name=u'教师课时费单价')
    # 教室
    class_room = models.ForeignKey('education.ClassRoom',
                                   related_name='class_class_room',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name=u'教室')
    # 班级类型
    CLASS_TYPE = {
        0: u'集体班',
        1: u'一对一',
    }
    class_type = models.IntegerField(choices=CLASS_TYPE.items(),
                                     null=True,
                                     verbose_name=u'班级类型')
    # 班级负责人
    in_charge = models.OneToOneField(settings.AUTH_USER_MODEL,
                                     null=True,
                                     on_delete=models.SET_NULL,
                                     verbose_name=u'班级负责人')
    # 开班时间
    start_time = models.DateTimeField(default=timezone.now,
                                      verbose_name=u'开班时间')
    # 结班时间
    end_time = models.DateTimeField(default=timezone.now,
                                    verbose_name=u'结班时间')
    # 预招人数
    total_plan = models.IntegerField(default=0,
                                     verbose_name=u'预招人数')
    # 当前人数
    total_current = models.IntegerField(default=0,
                                        verbose_name=u'当前人数')
    # 已排课时
    arrange_hours_yet = models.IntegerField(default=0,
                                            verbose_name=u'已排课时')
    # 班级状态 必选
    CLASS_STATE = {
        0: u'待开班',
        1: u'进行中',
        2: u'已结班',
    }
    class_state = models.IntegerField(choices=CLASS_STATE.items(),
                                      null=True,
                                      verbose_name=u'班级状态')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')
    class Meta:
        verbose_name = '班级'
        verbose_name_plural = '班级'

    def __str__(self):
        return self.teacher.user.get_full_name()


# 课程表单条记录
class ClassSchedule(models.Model):
    # 班级
    on_class = models.ForeignKey('education.Class',
                                 related_name='class_schedule_class',
                                 null=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name=u'班级')
    # 课程
    course = models.ForeignKey('education.Course',
                               related_name='class_schedule_course',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'课程')
    # 日期
    date = models.DateField(default=timezone.now,
                            verbose_name=u'日期')
    # 上课时间
    start_time = models.TimeField(default=timezone.now,
                                  verbose_name=u'上课时间')
    # 下课时间
    end_time = models.TimeField(default=timezone.now,
                                verbose_name=u'下课时间')
    # 本次课时
    hours = models.IntegerField(default=0,
                                verbose_name=u'本次课时')
    # 教师
    teacher = models.ForeignKey('school.Staff',
                                related_name='class_schedule_teacher',
                                null=True,
                                on_delete=models.SET_NULL,
                                verbose_name=u'教师')
    # 教师课时费单价
    teacher_unit_price = models.DecimalField(default=0.00,
                                             blank=True,
                                             max_digits=10,
                                             decimal_places=2,
                                             verbose_name=u'教师课时费单价')
    # 教室
    class_room = models.ForeignKey('education.ClassRoom',
                                   related_name='class_schedule_room',
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name=u'教室')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '课程表'
        verbose_name_plural = '课程表'

    def __str__(self):
        return self.course.name


# 临时调课记录
class TemporaryClassSchedule(models.Model):
    # 操作选项 必选
    OPERATE_OPTIONS = {
        0: u'新增',
        1: u'调换',
        2: u'删除',
    }
    operate = models.IntegerField(choices=OPERATE_OPTIONS.items(),
                                  null=True,
                                  verbose_name=u'操作')
    # 旧课表记录
    old_class_schedule = models.ForeignKey('education.ClassSchedule',
                                           related_name='temporary_class_schedule_old',
                                           null=True,
                                           blank=True,
                                           on_delete=models.SET_NULL,
                                           verbose_name=u'旧课表记录')
    # 新课表记录
    new_class_schedule = models.ForeignKey('education.ClassSchedule',
                                           related_name='temporary_class_schedule_new',
                                           null=True,
                                           blank=True,
                                           on_delete=models.SET_NULL,
                                           verbose_name=u'新课表记录')
    # 操作人
    operator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 related_name='temporary_class_schedule_operator',
                                 null=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name=u'操作人')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '临时调课记录'
        verbose_name_plural = '临时调课记录'

    def __str__(self):
        return self.old_class_schedule.course.name + '->' + self.new_class_schedule.course.name


# 学员考勤记录
class StudentAttendanceRecord(models.Model):
    # 课表记录
    class_schedule = models.ForeignKey('education.ClassSchedule',
                                       related_name='student_attendance_record_class_schedule',
                                       null=True,
                                       on_delete=models.SET_NULL,
                                       verbose_name=u'课表记录')
    # 学员
    student = models.ForeignKey('education.Student',
                                related_name='student_attendance_record_student',
                                null=True,
                                on_delete=models.SET_NULL,
                                verbose_name=u'学员')
    # 出勤状态 必选
    STATUS = {
        0: u'出勤',
        1: u'缺勤',
    }
    status = models.IntegerField(choices=STATUS.items(),
                                 null=True,
                                 verbose_name=u'出勤状态')
    # 考勤时间
    time = models.DateTimeField(default=timezone.now,
                                verbose_name=u'考勤时间')
    # 操作人
    operator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 related_name='student_attendance_record_operator',
                                 null=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name=u'操作人')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '学员考勤记录'
        verbose_name_plural = '学员考勤记录'

    def __str__(self):
        return self.class_schedule.course.name + '->' + self.student.pre_student.user.get_full_name() \
               + ' ' + self.get_status_display()


# 教师上课记录
class TeacherAttendanceRecord(models.Model):
    # 课表记录
    class_schedule = models.ForeignKey('education.ClassSchedule',
                                       related_name='teacher_attendance_record_class_schedule',
                                       null=True,
                                       on_delete=models.SET_NULL,
                                       verbose_name=u'课表记录')
    # 教师
    teacher = models.ForeignKey('school.Staff',
                                related_name='teacher_attendance_record_teacher',
                                null=True,
                                on_delete=models.SET_NULL,
                                verbose_name=u'教师')
    # 出勤状态 必选
    STATUS = {
        0: u'出勤',
        1: u'缺勤',
    }
    status = models.IntegerField(choices=STATUS.items(),
                                 null=True,
                                 verbose_name=u'出勤状态')
    # 考勤时间
    time = models.DateTimeField(default=timezone.now,
                                verbose_name=u'考勤时间')
    # 操作人
    operator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 related_name='teacher_attendance_record_operator',
                                 null=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name=u'操作人')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '教师上课记录'
        verbose_name_plural = '教师上课记录'

    def __str__(self):
        return self.class_schedule.course.name + '->' + self.teacher.user.get_full_name()


# 学员课消记录
class ClassExpenseRecord(models.Model):
    # 课表记录
    class_schedule = models.ForeignKey('education.ClassSchedule',
                                       related_name='class_expense_class_schedule',
                                       null=True,
                                       on_delete=models.SET_NULL,
                                       verbose_name=u'课表记录')
    # 学员
    student = models.ForeignKey('education.Student',
                                related_name='class_expense_student',
                                null=True,
                                on_delete=models.SET_NULL,
                                verbose_name=u'学员')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '学员课消记录'
        verbose_name_plural = '学员课消记录'

    def __str__(self):
        return self.class_schedule.course.name + '->' + self.student.pre_student.user.get_full_name()


