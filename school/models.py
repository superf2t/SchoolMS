from django.db import models
from django.conf import settings


# 学校
class School(models.Model):
    # 学校名称
    name = models.CharField(max_length=255,
                            null=True,
                            verbose_name=u'名称')
    # 排序
    list_order = models.IntegerField(default=0,
                                     verbose_name='排序')
    # 校区
    branches = models.ManyToManyField('school.Branch',
                                      blank=True,
                                      verbose_name='校区')
    # 部门
    departments = models.ManyToManyField('school.Department',
                                         blank=True,
                                         verbose_name='部门')

    class Meta:
        verbose_name = '学校'
        verbose_name_plural = '学校'

        permissions = (
            ("view_school", "Can view 学校"),
        )

    def __str__(self):
        return self.name


# 校区
class Branch(models.Model):
    # 校区名称
    name = models.CharField(max_length=255,
                            null=True,
                            verbose_name=u'名称')
    # 排序
    list_order = models.IntegerField(default=0,
                                     verbose_name='排序')
    # 部门
    departments = models.ManyToManyField('school.Department',
                                         blank=True,
                                         verbose_name='部门')

    class Meta:
        verbose_name = '校区'
        verbose_name_plural = '校区'

        permissions = (
            ("view_branch", "Can view 校区"),
        )

    def __str__(self):
        return self.name


# 部门
class Department(models.Model):
    # 部门名称
    name = models.CharField(max_length=255,
                            null=True,
                            verbose_name=u'名称')
    # 排序
    list_order = models.IntegerField(default=0,
                                     verbose_name='排序')
    # 子部门
    departments = models.ManyToManyField('self',
                                         blank=True,
                                         verbose_name='子部门')
    # 员工
    staffs = models.ManyToManyField('school.Staff',
                                    blank=True,
                                    verbose_name='员工')

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = '部门'

        permissions = (
            ("view_department", "Can view 部门"),
        )

    def __str__(self):
        return str(self.name)


# 员工
class Staff(models.Model):
    # 校区
    branch = models.ForeignKey('school.Branch',
                               related_name='staff_branch',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'校区')
    # 用户 级联删除
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                null=True,
                                on_delete=models.CASCADE,
                                verbose_name=u'对应用户')
    # 员工类型 必选
    CATEGORY = {
        0: u'教学人员',
        1: u'招生人员',
        2: u'管理人员',
        3: u'其他',
    }
    category = models.IntegerField(choices=CATEGORY.items(),
                                   null=True,
                                   blank=True,
                                   verbose_name=u'员工类型')
    # 身份证号码
    id_no = models.CharField(max_length=20,
                             null=True,
                             blank=True,
                             verbose_name=u'身份证')
    # 银行卡号码
    bank_no = models.CharField(max_length=30,
                               null=True,
                               blank=True,
                               verbose_name=u'银行卡号码')
    # 社保号
    social_security_no = models.CharField(max_length=30,
                                          null=True,
                                          blank=True,
                                          verbose_name=u'社保号')
    # 是否在职
    on_job = models.BooleanField(default=True,
                                 blank=True,
                                 verbose_name=u'是否在职')
    # 入职类型 必选
    JOB_STATE = {
        0: u'全职',
        1: u'兼职',
    }
    job_state = models.IntegerField(choices=JOB_STATE.items(),
                                    null=True,
                                    blank=True,
                                    verbose_name=u'入职类型')

    class Meta:
        verbose_name = '员工'
        verbose_name_plural = '员工'

        permissions = (
            ("view_staff", "Can view 员工"),
        )

    def __str__(self):
        if self.user:
            return self.user.get_full_name()
        else:
            return ''