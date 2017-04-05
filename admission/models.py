from django.db import models
from django.conf import settings
from django.utils import timezone


# ------------------------------------------- 准学员 开始 -----------------------------------------
# 准学员来源
class PreStudentSource(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='pre_student_source_branch',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'校区')
    # 准学员来源名称
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
        verbose_name = '准学员来源'
        verbose_name_plural = '准学员来源'

    def __str__(self):
        return self.name


# 准学员所属年级
class PreStudentClass(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='pre_student_class_branch',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'校区')
    # 准学员所属年级名称
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
        verbose_name = '准学员所属年级'
        verbose_name_plural = '准学员所属年级'

    def __str__(self):
        return self.name


# 准学员所属学校
class PreStudentSchool(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='pre_student_school_branch',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'校区')
    # 准学员所属学校名称
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
        verbose_name = '准学员所属学校'
        verbose_name_plural = '准学员所属学校'

    def __str__(self):
        return self.name


# 准学员所属分类
class PreStudentCategory(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='pre_student_category_branch',
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
        verbose_name = '准学员所属分类'
        verbose_name_plural = '准学员所属分类'

    def __str__(self):
        return self.name


# 准学员
class PreStudent(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='pre_student_branch',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'校区')
    # 用户 级联删除
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                null=True,
                                on_delete=models.CASCADE,
                                verbose_name=u'对应用户')
    # 当前跟进人
    follower = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 related_name='pre_student_follower',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name=u'当前跟进人')
    # 意向课程
    courses = models.ManyToManyField('education.Course',
                                     blank=True,
                                     verbose_name=u'意向课程')
    # 来源渠道
    source = models.ForeignKey(PreStudentSource,
                               related_name='pre_student_source',
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'来源渠道')
    # 所属年级
    source_class = models.ForeignKey(PreStudentClass,
                                     related_name='pre_student_source_class',
                                     null=True,
                                     blank=True,
                                     on_delete=models.SET_NULL,
                                     verbose_name=u'所属年级')
    # 来源学校
    source_school = models.ForeignKey(PreStudentSchool,
                                      related_name='pre_student_source_school',
                                      null=True,
                                      blank=True,
                                      on_delete=models.SET_NULL,
                                      verbose_name=u'来源学校')
    # 所属分类
    category = models.ForeignKey(PreStudentCategory,
                                 related_name='consult_category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name=u'所属分类')
    # 是否在跟进
    is_following = models.BooleanField(default=False,
                                       verbose_name=u'跟进中')

    class Meta:
        verbose_name = '准学员'
        verbose_name_plural = '准学员'

    def __str__(self):
        return self.user.get_full_name()
# ------------------------------------------- 准学员 结束 -----------------------------------------


# ------------------------------------------- 咨询 开始 -----------------------------------------
# 准学员联系人
class Contact(models.Model):
    # 联系人姓名
    name = models.CharField(max_length=255,
                            null=True,
                            verbose_name=u'姓名')
    # 电话号码
    tel = models.CharField(max_length=20,
                           null=True,
                           verbose_name=u'手机号码')
    # 关系类型
    CATEGORY = {
        0: u'父亲',
        1: u'母亲',
        2: u'爷爷',
        3: u'奶奶',
        4: u'外公',
        5: u'外婆',
    }
    category = models.IntegerField(choices=CATEGORY.items(),
                                   null=True,
                                   verbose_name=u'关系类型')

    class Meta:
        verbose_name = '准学员联系人'
        verbose_name_plural = '准学员联系人'

    def __str__(self):
        return self.name + ':' + self.tel


# 咨询标签
class ConsultTag(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='consult_tag_branch',
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
        verbose_name = '咨询标签'
        verbose_name_plural = '咨询标签'

    def __str__(self):
        return self.name


# 咨询记录
class Consult(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='consult_branch',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'校区')
    # 准学员
    pre_student = models.ForeignKey(PreStudent,
                                    related_name='consult_pre_student',
                                    null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL,
                                    verbose_name=u'准学员')
    # 咨询人
    follower = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 related_name='consult_follower',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name=u'咨询人')
    # 是否回复
    is_reply = models.BooleanField(default=True,
                                   verbose_name=u'是否回复')
    # 未回复原因
    not_reply_reason = models.CharField(max_length=255,
                                        null=True,
                                        blank=True,
                                        verbose_name=u'未回复原因')
    # 咨询方式 必选
    WAY = {
        0: u'QQ',
        1: u'电话',
        2: u'微信',
    }
    way = models.IntegerField(choices=WAY.items(),
                              null=True,
                              verbose_name=u'咨询方式')
    # 市场活动
    event = models.ForeignKey('market.DiscountEvent',
                              related_name='consult_event',
                              null=True,
                              blank=True,
                              on_delete=models.SET_NULL,
                              verbose_name=u'市场活动')
    # 所属等级
    grade = models.CharField(max_length=255,
                             null=True,
                             blank=True,
                             verbose_name=u'所属等级')
    # 市场人员
    marketer = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 related_name='consult_marketer',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name=u'市场人员')
    # 联系人
    contacts = models.ManyToManyField(Contact,
                                      blank=True,
                                      verbose_name=u'联系人')
    # 标签
    tags = models.ManyToManyField(ConsultTag,
                                  blank=True,
                                  verbose_name=u'标签')
    # 意向课程
    courses = models.ManyToManyField('education.Course',
                                     blank=True,
                                     verbose_name=u'意向课程')
    # 备注
    remark = models.CharField(max_length=255,
                              null=True,
                              blank=True,
                              verbose_name=u'备注')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '咨询记录'
        verbose_name_plural = '咨询记录'

    def __str__(self):
        return self.pre_student.user.get_full_name()
# ------------------------------------------- 咨询 结束 -----------------------------------------


# 邀约
class Invitation(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='invitation_branch',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'校区')
    # 准学员
    pre_student = models.ForeignKey(PreStudent,
                                    related_name='invitation_pre_student',
                                    null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL,
                                    verbose_name=u'准学员')
    # 邀约人
    follower = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 related_name='invitation_follower',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name=u'邀约人')
    # 是否回复
    is_reply = models.BooleanField(default=True,
                                   verbose_name=u'是否回复')
    # 未回复原因
    not_reply_reason = models.CharField(max_length=255,
                                        null=True,
                                        blank=True,
                                        verbose_name=u'未回复原因')
    # 邀请时间
    invitation_time = models.DateTimeField(default=timezone.now,
                                           null=True,
                                           blank=True,
                                           verbose_name=u'邀请时间')
    # 是否应邀
    agree_invitation = models.BooleanField(default=True,
                                           verbose_name=u'是否应邀')
    # 应邀时间
    agree_time = models.DateTimeField(default=timezone.now,
                                      null=True,
                                      blank=True,
                                      verbose_name=u'应邀时间')
    # 面谈内容
    interview_contents = models.TextField(blank=True,
                                          verbose_name=u'面谈内容')
    # 备注
    remark = models.CharField(max_length=255,
                              null=True,
                              blank=True,
                              verbose_name=u'备注')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '邀约'
        verbose_name_plural = '邀约'

    def __str__(self):
        return self.pre_student.user.get_full_name()


# 试听记录
class AuditionRecord(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='audition_record_branch',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'校区')
    # 准学员
    pre_student = models.ForeignKey(PreStudent,
                                    related_name='audition_record_pre_student',
                                    null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL,
                                    verbose_name=u'准学员')
    # 试听安排人
    follower = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 related_name='audition_record_follower',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name=u'试听安排人')
    # 是否上课
    is_reply = models.BooleanField(default=True,
                                   verbose_name=u'是否上课')
    # 翘课原因
    not_reply_reason = models.CharField(max_length=255,
                                        null=True,
                                        blank=True,
                                        verbose_name=u'翘课原因')
    # 试听课程
    course = models.ForeignKey('education.Course',
                               related_name='audition_course',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'试听课程')
    # 上课状态
    state = models.TextField(verbose_name=u'上课状态')
    # 备注
    remark = models.CharField(max_length=255,
                              null=True,
                              blank=True,
                              verbose_name=u'备注')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '试听记录'
        verbose_name_plural = '试听记录'

    def __str__(self):
        return self.pre_student.user.get_full_name() + " 试听 " + self.course.name


# 推荐记录
class RecommendRecord(models.Model):
    # 推荐人号码
    from_user_tel = models.CharField(max_length=20,
                                     null=True,
                                     verbose_name=u'推荐人号码')
    # 被推荐人
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='recommend_record_to_user',
                                null=True,
                                on_delete=models.SET_NULL,
                                verbose_name=u'被推荐人')
    # 推荐时间
    time = models.DateTimeField(default=timezone.now,
                                verbose_name=u'推荐时间')
    # 是否继续返利
    is_rebate = models.BooleanField(default=True,
                                    verbose_name=u'是否继续返利')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '推荐记录'
        verbose_name_plural = '推荐记录'

    def __str__(self):
        return self.from_user_tel + " 推荐 " + self.to_user.name
