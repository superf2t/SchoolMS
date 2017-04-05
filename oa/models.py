from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group


# 邮件模板
class EmailTemplate(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='email_template_branch',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'校区')
    # 邮件模板名称
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
        verbose_name = '邮件模板'
        verbose_name_plural = '邮件模板'

        permissions = (
            ("view_emailtemplate", "Can view 邮件模板"),
        )

    def __str__(self):
        return self.name


# 邮件
class Email(models.Model):
    # 发件人 级联删除
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  related_name='email_from_user',
                                  on_delete=models.CASCADE,
                                  verbose_name=u'发件人')
    # 收件人 级联删除
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='email_to_user',
                                on_delete=models.CASCADE,
                                verbose_name=u'收件人')
    # 正文
    content = models.TextField(verbose_name=u'正文')
    # 阅读状态
    IS_READ = {
        0: u'未读',
        1: u'已读'
    }
    is_read = models.IntegerField(default=0,
                                  choices=IS_READ.items(),
                                  verbose_name=u'阅读状态')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '邮件'
        verbose_name_plural = '邮件'

        permissions = (
            ("view_email", "Can view 邮件"),
        )

    def __str__(self):
        return self.from_user.get_full_name()+" -> "+self.to_user.get_full_name()


# 通知模板
class NotificationTemplate(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='notification_template_branch',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'校区')
    # 通知模板名称
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
        verbose_name = '通知模板'
        verbose_name_plural = '通知模板'

        permissions = (
            ("view_notificationtemplate", "Can view 通知模板"),
        )

    def __str__(self):
        return self.name


# 通知
class Notification(models.Model):
    # 通知发起人
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  related_name='notification_from_user',
                                  on_delete=models.CASCADE,
                                  verbose_name=u'通知发起人')
    # 通知内容
    content = models.TextField(verbose_name=u'通知内容')
    # 是否有效
    is_active = models.BooleanField(default=True,
                                    verbose_name=u'是否有效')
    # 通知员工职务
    groups = models.ManyToManyField(Group,
                                    blank=True,
                                    verbose_name=u'通知员工职务')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '通知'
        verbose_name_plural = '通知'

        permissions = (
            ("view_notification", "Can view 通知"),
        )

    # 获取权限组名称
    def get_group_name(self):
        groups_name = '['
        for group in self.groups.all():
            groups_name += group.name + " , "
        groups_name += ']'
        return groups_name
    get_group_name.short_description = '通知员工职务'

    def __str__(self):
        return self.from_user.get_full_name()+" -> " + self.get_group_name()


# 工作报告模板
class WorkReportTemplate(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='work_report_template_branch',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'校区')
    # 工作报告模板名称
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
        verbose_name = '工作报告模板'
        verbose_name_plural = '工作报告模板'

        permissions = (
            ("view_workreporttemplate", "Can view 工作报告模板"),
        )

    def __str__(self):
        return self.name


# 员工工作报告
class WorkReport(models.Model):
    # 报告人
    report_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    related_name='work_report_report_user',
                                    on_delete=models.CASCADE,
                                    verbose_name=u'报告人')
    # 报告内容
    content = models.TextField(verbose_name=u'报告内容')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '工作报告'
        verbose_name_plural = '工作报告'

        permissions = (
            ("view_workreport", "Can view 工作报告"),
        )

    def __str__(self):
        return self.report_user.get_full_name()
