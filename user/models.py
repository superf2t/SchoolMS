import os
import binascii
from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.utils import six, timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator, UnicodeUsernameValidator

from .storage import ImageStorage


# 用户
class User(AbstractBaseUser, PermissionsMixin):
    # 手机号码
    username_validator = UnicodeUsernameValidator() if six.PY3 else ASCIIUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("该号码已被注册"),
        },
    )
    # 头像存储
    user_portrait = ImageStorage(location=settings.MEDIA_ROOT + '/user/',
                                 base_url='/media/user/',)
    # 头像
    portrait = models.ImageField(storage=user_portrait,
                                 blank=True,
                                 default='default.png',
                                 verbose_name=u'头像')
    # 性别 必选
    GENDER = {
        0: u'女',
        1: u'男',
        2: u'保密',
    }
    gender = models.IntegerField(choices=GENDER.items(),
                                 null=True,
                                 blank=True,
                                 verbose_name=u'性别',)
    # 姓名
    name = models.CharField(max_length=30,
                            blank=True,
                            verbose_name='姓名')
    # 生日
    birth_day = models.DateField(null=True,
                                 blank=True,
                                 default=timezone.now,
                                 verbose_name='生日')
    # 电子邮件
    email = models.EmailField(blank=True,
                              verbose_name='电子邮件')
    # 手机号码
    tel = models.CharField(max_length=20,
                           null=True,
                           blank=True,
                           verbose_name=u'手机号码')
    # 固定电话
    fixed_tel = models.CharField(max_length=20,
                                 null=True,
                                 blank=True,
                                 verbose_name=u'固定电话')
    # QQ
    qq = models.CharField(max_length=20,
                          null=True,
                          blank=True,
                          verbose_name=u'QQ')
    # 微信
    we_chat = models.CharField(max_length=40,
                               null=True,
                               blank=True,
                               verbose_name=u'微信')
    # 联系地址
    contact_address = models.CharField(max_length=255,
                                       null=True,
                                       blank=True,
                                       verbose_name=u'联系地址')
    # 可见校区
    branches = models.ManyToManyField('school.Branch',
                                      blank=True,
                                      verbose_name='校区')
    # 控制该用户是否可以登录admin site
    is_staff = models.BooleanField(_('staff status'),
                                   default=False,)
    # 反选既等同于删除用户
    is_active = models.BooleanField(_('active'),
                                    default=True,)
    # 账号创建时间
    date_joined = models.DateTimeField(_('date joined'),
                                       auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('用户')
        verbose_name_plural = _('用户')

        permissions = (
            ("view_user", "Can view 用户"),
        )

    # 头像更新时删除旧头像
    def save(self, *args, **kwargs):
        if not self.id:
            # 增
            if self.portrait == 'default.png':
                # 根据性别自动选择默认头像
                if self.gender == 0:
                    self.portrait = 'default_female.png'
                elif self.gender == 1:
                    self.portrait = 'default_male.png'
        else:
            # 改 更换头像后删除旧头像文件
            this = User.objects.get(id=self.id)
            if this.portrait != self.portrait:
                this.portrait.delete(save=False)
        super(User, self).save(*args, **kwargs)

    # 获取全名
    def get_full_name(self):
        if self.name == '':
            return self.username
        else:
            return self.name
    get_full_name.short_description = '全名'

    # 获取名称
    def get_short_name(self):
        return self.name

    # 向该用户发送邮件
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return str(self.id)+' '+self.username

User._meta.get_field('groups').verbose_name = '职务'


# Token
class Token(models.Model):
    # 用户 级联删除
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                null=True,
                                on_delete=models.CASCADE,
                                verbose_name=u'对应用户')

    # 授权Token AT
    access_token = models.CharField(default='',
                                    max_length=40,
                                    verbose_name=u'授权Token')
    # 刷新Token RT
    refresh_token = models.CharField(default='',
                                     max_length=40,
                                     verbose_name=u'刷新Token')

    class Meta:
        verbose_name = '令牌'
        verbose_name_plural = '令牌'

    # 保存AT&RT
    def save(self, *args, **kwargs):
        if not self.access_token:
            self.access_token = self.generate_key()
        if not self.refresh_token:
            self.refresh_token = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    # 使用RT来刷新AT
    def refresh_access_token(self):
        self.access_token = self.generate_key()

    # 生成20位随机数
    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.access_token
