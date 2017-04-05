from django.db import models
from django.conf import settings


# 操作日志
class Logger(models.Model):
    # 操作人
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='logger_user',
                             null=True,
                             verbose_name=u'操作人')
    # 操作类型
    CATEGORY = {
        0: u'查看',
        1: u'新增',
        2: u'修改',
        3: u'删除',
        4: u'其他',
    }
    category = models.IntegerField(choices=CATEGORY.items(),
                                   null=True,
                                   verbose_name=u'操作类型')
    # 日志内容
    content = models.TextField(verbose_name=u'日志内容')
    # 是否作废
    is_abandon = models.BooleanField(default=False,
                                     verbose_name=u'是否作废')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '操作日志'
        verbose_name_plural = '操作日志'

    def __str__(self):
        return self.user.name + ' 内容:' + self.content
