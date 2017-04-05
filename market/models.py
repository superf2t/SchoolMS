from django.db import models
from django.conf import settings
from django.utils import timezone


# 优惠券
class DiscountCoupon(models.Model):
    # 名称
    name = models.CharField(max_length=255,
                            null=True,
                            verbose_name=u'名称')
    # 优惠劵类别 必选
    CATEGORY = {
        0: u'打折券',
        1: u'优惠券',
    }
    category = models.IntegerField(choices=CATEGORY.items(),
                                   null=True,
                                   verbose_name=u'优惠劵类别')
    # 折扣比例 打折券
    discount_percent = models.DecimalField(default=0.00,
                                           max_digits=3,
                                           decimal_places=2,
                                           blank=True,
                                           verbose_name='折扣比例')
    # 折扣金额 优惠券
    discount_amount = models.DecimalField(default=0.00,
                                          max_digits=10,
                                          decimal_places=2,
                                          blank=True,
                                          verbose_name='折扣金额')
    # 优惠劵内容
    content = models.CharField(max_length=255,
                               null=True,
                               blank=True,
                               verbose_name=u'优惠劵内容')
    # 最低消费
    minimum_consumption = models.IntegerField(default=0,
                                              verbose_name='最低消费')
    # 有效期类型 必选
    EXPIRATION_TYPE = {
        0: u'长期有效',
        1: u'固定日期到期',
        2: u'自领取后几日到期',
    }
    expiration_type = models.IntegerField(choices=EXPIRATION_TYPE.items(),
                                          null=True,
                                          verbose_name=u'有效期类型')
    # 到期时间-固定日期到期
    expiration_time = models.DateTimeField(default=timezone.now,
                                           null=True,
                                           blank=True,
                                           verbose_name=u'到期时间')
    # 可持续天数-自领取后几日到期
    expiration_day = models.IntegerField(default=0,
                                         null=True,
                                         blank=True,
                                         verbose_name=u'可持续天数')
    # 是否停用 已发放的优惠卷需要同步停用
    is_abandon = models.BooleanField(default=False,
                                     verbose_name=u'是否停用')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '优惠券'
        verbose_name_plural = '优惠券'

    def __str__(self):
        return self.name


# 优惠券发放
class DiscountCouponPublish(models.Model):
    # 发放人
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  related_name='discount_coupon_publisher',
                                  null=True,
                                  on_delete=models.SET_NULL,
                                  verbose_name=u'发放人')
    # 优惠券
    discount_coupon = models.ForeignKey('market.DiscountCoupon',
                                        related_name='publish_discount_coupon',
                                        null=True,
                                        on_delete=models.SET_NULL,
                                        verbose_name=u'优惠券')
    # 预发数量
    count = models.IntegerField(default=0,
                                verbose_name='预发数量')
    # 限领数量 单人每天
    limit_everyday = models.IntegerField(default=0,
                                         verbose_name='限领数量-单人每天')
    # 限领数量 单人总领取数量
    limit_all = models.IntegerField(default=0,
                                    verbose_name='限领数量-单人总领取数量')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '优惠券发放'
        verbose_name_plural = '优惠券发放'

    def __str__(self):
        return self.discount_coupon.name


# 优惠券领取记录 (多张既创建多个)
class DiscountCouponRecord(models.Model):
    # 优惠券快照 领取后需要生成快照(保证优惠券在被修改后已领取的优惠券不受影响)
    coupon = models.ForeignKey('market.DiscountCoupon',
                               related_name='coupon_record_coupon',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'优惠券')
    # 优惠券快照 当原始优惠券被停用 本优惠卷同步停用
    coupon_original = models.ForeignKey('market.DiscountCoupon',
                                        related_name='coupon_record_coupon_original',
                                        null=True,
                                        on_delete=models.SET_NULL,
                                        verbose_name=u'原始优惠券')
    # 用户
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='coupon_record_user',
                             null=True,
                             on_delete=models.SET_NULL,
                             verbose_name=u'用户')
    # 领取时间
    receive_time = models.DateTimeField(default=timezone.now,
                                        verbose_name=u'领取时间')
    # 到期时间
    expiration_time = models.DateTimeField(default=timezone.now,
                                           verbose_name=u'到期时间')
    # 是否被锁定
    is_locked = models.BooleanField(default=False,
                                    verbose_name=u'是否锁定')
    # 是否已使用
    is_used = models.BooleanField(default=False,
                                  verbose_name=u'是否已使用')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '优惠券领取记录'
        verbose_name_plural = '优惠券领取记录'

    def __str__(self):
        return self.coupon.name + ' ' + self.user.get_full_name() + " " + str(self.count) + '张'


# 优惠活动
class DiscountEvent(models.Model):
    # 活动名称
    name = models.CharField(max_length=255,
                            null=True,
                            verbose_name=u'名称')
    # 开始时间
    start_time = models.DateTimeField(default=timezone.now,
                                      null=True,
                                      verbose_name=u'开始时间')
    # 结束时间
    end_time = models.DateTimeField(default=timezone.now,
                                    null=True,
                                    verbose_name=u'结束时间')
    # 优惠活动类别 必选
    CATEGORY = {
        0: u'打折',
        1: u'充值送金额',
        2: u'充值送积分',
        3: u'消费满减金额',
        4: u'消费满送余额',
        5: u'消费送积分',
    }
    category = models.IntegerField(choices=CATEGORY.items(),
                                   null=True,
                                   verbose_name=u'优惠活动类别')
    # 优惠详情
    details = models.TextField(verbose_name=u'优惠详情')
    # 折扣比例 活动类型为打折
    discount_percent = models.DecimalField(default=0.00,
                                           max_digits=3,
                                           decimal_places=2,
                                           blank=True,
                                           verbose_name='折扣比例')
    # 满减\送类型 必选
    CATEGORY_TYPE = {
        0: u'只满减',
        1: u'每满x减\送x',
    }
    category_type = models.IntegerField(choices=CATEGORY_TYPE.items(),
                                        null=True,
                                        verbose_name=u'满减\送类型')
    # 满x
    satisfy = models.DecimalField(default=0.00,
                                  max_digits=10,
                                  decimal_places=2,
                                  verbose_name=u'满x')
    # 减\送x
    subtract_give = models.DecimalField(default=0.00,
                                        max_digits=10,
                                        decimal_places=2,
                                        verbose_name=u'减\送x')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '优惠活动'
        verbose_name_plural = '优惠活动'

    def __str__(self):
        return self.name
