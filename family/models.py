from django.db import models
from django.conf import settings
from django.utils import timezone


# 公告模板
class NoticeTemplate(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='notice_template_branch',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'校区')
    # 公告模板名称
    name = models.CharField(max_length=255,
                            null=True,
                            verbose_name=u'模板名称')
    # 正文
    content = models.TextField(verbose_name=u'模板内容')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '公告模板'
        verbose_name_plural = '公告模板'

        permissions = (
            ("view_noticetemplate", "Can view 公告模板"),
        )

    def __str__(self):
        return self.name


# 公告
class Notice(models.Model):
    # 公告撰写人 级联删除
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  related_name='notice_from_user',
                                  on_delete=models.CASCADE,
                                  verbose_name=u'撰写人')
    # 所属校区
    branches = models.ManyToManyField('school.Branch',
                                      blank=True,
                                      verbose_name='所属校区')
    # 是否发布
    is_publish = models.BooleanField(default=True,
                                     verbose_name=u'是否发布')
    # 是否置顶
    is_top = models.BooleanField(default=False,
                                 verbose_name=u'置顶')
    # 正文
    content = models.TextField(verbose_name=u'正文')
    # 发布时间
    publish_time = models.DateTimeField(default=timezone.now,
                                        verbose_name=u'发布时间')
    # 长期有效
    always_useful = models.BooleanField(default=False,
                                        verbose_name=u'长期有效')
    # 到期时间
    expiration_time = models.DateTimeField(default=timezone.now,
                                           blank=True,
                                           verbose_name=u'到期时间')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '公告'
        verbose_name_plural = '公告'

        permissions = (
            ("view_notice", "Can view 公告"),
        )

    # 获取校区名称
    def get_branches_name(self):
        branches_name = '['
        for branch in self.branches.all():
            branches_name += branch.name + " , "
            branches_name += ']'
        return branches_name
    get_branches_name.short_description = '校区'

    def __str__(self):
        return self.from_user.get_full_name()+" -> " + self.get_branches_name()


# 短信模板
class SMSTemplate(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='sms_template_branch',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'校区')
    # 短信模板名称
    name = models.CharField(max_length=255,
                            null=True,
                            verbose_name=u'模板名称')
    # 正文
    content = models.TextField(verbose_name=u'模板内容')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '短信模板'
        verbose_name_plural = '短信模板'

        permissions = (
            ("view_smstemplate", "Can view 短信模板"),
        )


    def __str__(self):
        return self.name


# 短信
class SMS(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='sms_branch',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'校区')
    # 短信撰写人 级联删除
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  related_name='sms_from_user',
                                  on_delete=models.CASCADE,
                                  verbose_name=u'撰写人')
    # 接收用户
    to_users = models.TextField(verbose_name=u'接收用户')
    # 短信内容
    content = models.TextField(verbose_name=u'短信内容')
    # 短信签名
    signature = models.CharField(max_length=255,
                                 null=True,
                                 blank=True,
                                 verbose_name=u'短信签名')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '短信'
        verbose_name_plural = '短信'

        permissions = (
            ("view_sms", "Can view 短信"),
        )


    def __str__(self):
        return self.from_user.get_full_name() + " : " + self.content


# 短信记录
class SMSRecord(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='sms_record_branch',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'校区')
    # 发送人
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  related_name='sms_record_from_user',
                                  on_delete=models.CASCADE,
                                  verbose_name=u'发送人')
    # 接收人姓名
    to_user_name = models.CharField(max_length=255,
                                    null=True,
                                    verbose_name=u'接收人姓名')
    # 接收人电话
    to_user_tel = models.CharField(max_length=255,
                                   null=True,
                                   verbose_name=u'接收人电话')
    # 短信内容
    content = models.TextField(verbose_name=u'短信内容')
    # 短信字数
    word_count = models.IntegerField(default=0,
                                     blank=True,
                                     verbose_name='短信字数')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '短信记录'
        verbose_name_plural = '短信记录'

        permissions = (
            ("view_smsrecord", "Can view 短信记录"),
        )

    def __str__(self):
        return self.from_user.get_full_name() + " -> " + self.to_user_name+":"+self.to_user_tel


# 短信分配
class SMSAssign(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='sms_assign_branch',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'校区')
    # 员工
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='sms_assign_user',
                             on_delete=models.CASCADE,
                             verbose_name=u'员工')
    # 本期分配条数
    assign_sum = models.IntegerField(default=0,
                                     verbose_name='本期分配条数')
    # 已使用
    used = models.IntegerField(default=0,
                               verbose_name='已使用')
    # 剩余
    remain = models.IntegerField(default=0,
                                 verbose_name='剩余')
    # 一周期结束 是否自动清零
    auto_reset = models.BooleanField(default=True,
                                     verbose_name=u'月底自动清零')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '短信分配'
        verbose_name_plural = '短信分配'

        permissions = (
            ("view_smsassign", "Can view 短信分配"),
        )

    def __str__(self):
        return self.user.get_full_name() + ": " + str(self.used)+"/"+str(self.assign_sum)

