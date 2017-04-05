from django.db import models
from django.utils import timezone
from django.conf import settings


# ------------------------------------------- 准学员缴费 开始 -----------------------------------------
# 准学员购课记录
class PreStudentPaymentRecords(models.Model):
    # 用户 (统一学员和准学员购课)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='pre_student_payment_records_user',
                             null=True,
                             on_delete=models.SET_NULL,
                             verbose_name=u'用户')
    # 购买课程
    courses = models.ManyToManyField('education.Course',
                                     blank=True,
                                     verbose_name=u'报名课程')
    # 子订单支付记录
    items = models.ManyToManyField('finance.PreStudentPaymentItem',
                                   blank=True,
                                   verbose_name=u'子订单支付记录')
    # 优惠券领取记录
    discount_coupon_record = models.ForeignKey('market.DiscountCouponRecord',
                                               related_name='pre_student_payment_records_discount_coupon_record',
                                               null=True,
                                               blank=True,
                                               on_delete=models.SET_NULL,
                                               verbose_name=u'优惠券领取记录')
    # 市场活动
    event = models.ForeignKey('market.DiscountEvent',
                              related_name='pre_student_payment_records_event',
                              null=True,
                              blank=True,
                              on_delete=models.SET_NULL,
                              verbose_name=u'市场活动')
    # 总金额
    total_amount = models.DecimalField(default=0.00,
                                       max_digits=10,
                                       decimal_places=2,
                                       verbose_name=u'总金额')
    # 折扣金额
    discount_amount = models.DecimalField(default=0.00,
                                          max_digits=10,
                                          decimal_places=2,
                                          verbose_name=u'折扣金额')
    # 实际支付金额
    real_amount = models.DecimalField(default=0.00,
                                      max_digits=10,
                                      decimal_places=2,
                                      verbose_name=u'实际支付金额')
    # 收支记录
    income_expense = models.ForeignKey('finance.IncomeExpense',
                                       related_name='pre_student_payment_records_income_expense',
                                       null=True,
                                       blank=True,
                                       on_delete=models.SET_NULL,
                                       verbose_name=u'收支记录')
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
        verbose_name = '购课记录'
        verbose_name_plural = '购课记录'

    def __str__(self):
        return self.user.username + ' 金额:' + str(self.real_amount)


# 用户购课单条记录 (相当于购物车下单后进行订单拆分)
class PreStudentPaymentItem(models.Model):
    # 用户 (统一学员和准学员购课)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='pre_student_payment_item_user',
                             null=True,
                             on_delete=models.SET_NULL,
                             verbose_name=u'用户')
    # 购买课程
    course = models.ForeignKey('education.Course',
                               related_name='pre_student_payment_item_course',
                               null=True,
                               on_delete=models.SET_NULL,
                               verbose_name=u'课程名称')
    # 总金额
    total_amount = models.DecimalField(default=0.00,
                                       max_digits=10,
                                       decimal_places=2,
                                       verbose_name=u'总金额')
    # 折扣金额
    discount_amount = models.DecimalField(default=0.00,
                                          max_digits=10,
                                          decimal_places=2,
                                          verbose_name=u'折扣金额')
    # 实际支付金额
    real_amount = models.DecimalField(default=0.00,
                                      max_digits=10,
                                      decimal_places=2,
                                      verbose_name=u'实际支付金额')
    # 收支记录
    income_expense = models.ForeignKey('finance.IncomeExpense',
                                       related_name='pre_student_payment_item_income_expense',
                                       null=True,
                                       blank=True,
                                       on_delete=models.SET_NULL,
                                       verbose_name=u'收支记录')
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
        verbose_name = '购课子记录'
        verbose_name_plural = '购课子记录'

    def __str__(self):
        return self.user.username + ' 金额:' + str(self.real_amount)

# ------------------------------------------- 准学员缴费 结束 -----------------------------------------


# 购课提成记录
class PreStudentPaymentDeduct(models.Model):
    # 购课记录
    payment_item = models.ForeignKey('finance.PreStudentPaymentItem',
                                     related_name='pre_student_payment_deduct_payment_item',
                                     null=True,
                                     on_delete=models.SET_NULL,
                                     verbose_name=u'购课记录')
    # 提成人 员工/学员
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='pre_student_payment_deduct_user',
                             null=True,
                             on_delete=models.SET_NULL,
                             verbose_name=u'提成人')
    # 提成原因
    REASON = {
        0: u'介绍',
        1: u'推荐人',
        2: u'主动咨询',
        3: u'邀约',
        4: u'安排试听',
        5: u'试听讲师',
        6: u'其他',
    }
    reason = models.IntegerField(choices=REASON.items(),
                                 null=True,
                                 verbose_name=u'提成原因')
    # 总提成金额
    total_amount = models.DecimalField(default=0.00,
                                       max_digits=10,
                                       decimal_places=2,
                                       verbose_name=u'总提成金额')
    # 修正金额
    discount_amount = models.DecimalField(default=0.00,
                                          max_digits=10,
                                          decimal_places=2,
                                          verbose_name=u'修正金额')
    # 实际提成金额
    real_amount = models.DecimalField(default=0.00,
                                      max_digits=10,
                                      decimal_places=2,
                                      verbose_name=u'实际提成金额')
    # 收支记录
    income_expense = models.ForeignKey('finance.IncomeExpense',
                                       related_name='pre_student_payment_deduct_income_expense',
                                       null=True,
                                       blank=True,
                                       on_delete=models.SET_NULL,
                                       verbose_name=u'收支记录')
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
        verbose_name = '购课提成'
        verbose_name_plural = '购课提成'

    def __str__(self):
        return self.user.username + ' 金额:' + str(self.real_amount)


# ------------------------------------------- 积分 开始 -----------------------------------------
# 积分
class Point(models.Model):
    # 用户
    user = models.OneToOneField('user.User',
                                on_delete=models.CASCADE,
                                verbose_name=u'用户')
    # 积分值
    value = models.IntegerField(default=0,
                                verbose_name=u'积分值')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '积分'
        verbose_name_plural = '积分'

    def add_point(self, value, reason):
        self.value += value
        self.save()
        PointChangeLog.objects.create(point=self, change_value=+value,
                                      value_after=self.value, change_reason=reason)

    def sub_point(self, value, reason):
        if self.value - value >= 0:
            self.value -= value
            self.save()
            point_change_log = PointChangeLog.objects.create(point=self, change_value=-value,
                                                             value_after=self.value, change_reason=reason)
            return point_change_log
        else:
            return None

    def __str__(self):
        return self.user.username + ':' + str(self.value)


# 积分变更记录
class PointChangeLog(models.Model):
    # 对应积分
    point = models.ForeignKey('finance.Point',
                              related_name='point_change_log_point',
                              on_delete=models.CASCADE,
                              verbose_name=u'积分')
    # 变更金额
    change_value = models.IntegerField(default=0,
                                       verbose_name=u'变更积分值')
    # 变更后积分值
    value_after = models.IntegerField(default=0,
                                      verbose_name=u'变更后积分值')
    # 变更原因 包括:
    # Up:充值 登录 邀请 发生活点滴
    # Down:兑换实体商品 礼物 虚拟商品
    change_reason = models.CharField(max_length=255,
                                     null=True,
                                     verbose_name=u'变更原因')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '积分变更记录'
        verbose_name_plural = '积分变更记录'

    def __str__(self):
        return self.point.user.username + ' 金额:' + str(self.change_value) + ' 原因:' + self.change_reason


# 积分充值订单
class PointReChargeLog(models.Model):
    # 对应积分
    point = models.ForeignKey('finance.Point',
                              related_name='point_recharge_log_point',
                              on_delete=models.CASCADE,
                              verbose_name=u'积分充值订单')
    # 商户订单编号
    out_trade_no = models.CharField(max_length=255,
                                    null=True,
                                    verbose_name=u'商户订单编号')
    # 支付平台选项
    PLATFORM = {
        0: u'支付宝',
        1: u'微信',
    }
    platform = models.IntegerField(choices=PLATFORM.items(),
                                   null=True,
                                   verbose_name=u'支付平台')
    # 支付平台编号
    trade_no = models.CharField(max_length=255,
                                null=True,
                                blank=True,
                                verbose_name=u'支付平台编号')
    # 充值金额
    recharge_amount = models.DecimalField(default=0.00,
                                          max_digits=10,
                                          decimal_places=2,
                                          verbose_name=u'充值金额')
    # 充值积分
    recharge_point = models.IntegerField(default=0,
                                         verbose_name=u'充值积分')
    # 是否付款
    is_pay = models.BooleanField(default=False,
                                 verbose_name=u'是否付款')
    # 付款时间
    pay_time = models.DateTimeField(null=True,
                                    blank=True,
                                    verbose_name=u'付款时间')
    # 超时时间
    timeout_express = models.CharField(max_length=10,
                                       null=True,
                                       verbose_name=u'超时时间')
    # 收支记录
    income_expense = models.ForeignKey('finance.IncomeExpense',
                                       related_name='point_recharge_log_income_expense',
                                       null=True,
                                       blank=True,
                                       on_delete=models.SET_NULL,
                                       verbose_name=u'收支记录')
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
        verbose_name = '积分充值记录'
        verbose_name_plural = '积分充值记录'

    def __str__(self):
        return self.point.user.username + ' 金额:' + str(self.recharge_amount)
# ------------------------------------------- 积分 结束 -----------------------------------------


# ------------------------------------------- 余额 开始 -----------------------------------------
# 余额
class Balance(models.Model):
    # 用户
    user = models.OneToOneField('user.User',
                                on_delete=models.CASCADE,
                                verbose_name=u'用户')
    # 账户余额
    value = models.DecimalField(default=0.00,
                                max_digits=12,
                                decimal_places=2,
                                verbose_name='账户余额')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '余额'
        verbose_name_plural = '余额'

    def add_point(self, value, reason):
        self.value += value
        self.save()
        BalanceChangeLog.objects.create(point=self, change_value=+value,
                                        value_after=self.value, change_reason=reason)

    def sub_point(self, value, reason):
        if self.value - value >= 0:
            self.value -= value
            self.save()
            point_change_log = BalanceChangeLog.objects.create(point=self, change_value=-value,
                                                               value_after=self.value, change_reason=reason)
            return point_change_log
        else:
            return None

    def __str__(self):
        return self.user.username + ':' + str(self.value)


# 余额变更记录
class BalanceChangeLog(models.Model):
    # 对应余额
    balance = models.ForeignKey('finance.Balance',
                                related_name='balance_change_log_balance',
                                on_delete=models.CASCADE,
                                verbose_name=u'余额')
    # 变更金额
    change_value = models.DecimalField(default=0.00,
                                       max_digits=12,
                                       decimal_places=2,
                                       verbose_name='变更金额')
    # 变更后积分值
    value_after = models.DecimalField(default=0.00,
                                      max_digits=12,
                                      decimal_places=2,
                                      verbose_name='变更后余额')
    # 变更原因 包括:
    # Up:充值 登录 邀请 发生活点滴
    # Down:兑换实体商品 礼物 虚拟商品
    change_reason = models.CharField(max_length=255,
                                     null=True,
                                     verbose_name=u'变更原因')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')

    class Meta:
        verbose_name = '余额变更记录'
        verbose_name_plural = '余额变更记录'

    def __str__(self):
        return self.balance.user.username + ' 金额:' + str(self.change_value) + ' 原因:' + self.change_reason


# 余额充值订单
class BalanceReChargeLog(models.Model):
    # 对应余额
    balance = models.ForeignKey('finance.Balance',
                                related_name='balance_recharge_log_balance',
                                on_delete=models.CASCADE,
                                verbose_name=u'余额')
    # 商户订单编号
    out_trade_no = models.CharField(max_length=255,
                                    null=True,
                                    verbose_name=u'商户订单编号')
    # 对应优惠券领取记录
    discount_coupon_record = models.ForeignKey('market.DiscountCouponRecord',
                                               related_name='balance_recharge_log_discount_coupon_record',
                                               on_delete=models.CASCADE,
                                               verbose_name=u'对应优惠券')
    # 优惠活动
    discount_event = models.ForeignKey('market.DiscountEvent',
                                       related_name='balance_recharge_log_discount_event',
                                       on_delete=models.CASCADE,
                                       verbose_name=u'优惠活动')
    # 支付平台选项
    PLATFORM = {
        0: u'支付宝',
        1: u'微信',
    }
    platform = models.IntegerField(choices=PLATFORM.items(),
                                   null=True,
                                   verbose_name=u'支付平台')
    # 支付平台编号
    trade_no = models.CharField(max_length=255,
                                null=True,
                                blank=True,
                                verbose_name=u'支付平台编号')
    # 充值金额
    recharge_amount = models.DecimalField(default=0.00,
                                          max_digits=12,
                                          decimal_places=2,
                                          verbose_name=u'充值金额')
    # 实际到账金额
    recharge_real = models.DecimalField(default=0.00,
                                        max_digits=12,
                                        decimal_places=2,
                                        verbose_name=u'实际到账金额')
    # 是否付款
    is_pay = models.BooleanField(default=False,
                                 verbose_name=u'是否付款')
    # 付款时间
    pay_time = models.DateTimeField(null=True,
                                    blank=True,
                                    verbose_name=u'付款时间')
    # 超时时间
    timeout_express = models.CharField(max_length=10,
                                       null=True,
                                       verbose_name=u'超时时间')
    # 收支记录
    income_expense = models.ForeignKey('finance.IncomeExpense',
                                       related_name='balance_recharge_log_income_expense',
                                       null=True,
                                       blank=True,
                                       on_delete=models.SET_NULL,
                                       verbose_name=u'收支记录')
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
        verbose_name = '余额充值记录'
        verbose_name_plural = '余额充值记录'

    def __str__(self):
        return self.balance.user.username + ' 金额:' + str(self.recharge_amount)
# ------------------------------------------- 积分 结束 -----------------------------------------


# 收支款项经办
class IncomeExpense(models.Model):
    # 收入or支出
    INCOME_EXPENSE = {
        0: u'收入',
        1: u'支出',
    }
    income_expense = models.IntegerField(choices=INCOME_EXPENSE.items(),
                                         null=True,
                                         verbose_name=u'收入/支出')
    # 收支类型
    CATEGORY = {
        0: u'购课',
        1: u'充值',
        2: u'其他入账',
        3: u'工资',
        4: u'提成',
        5: u'其他出账',
    }
    category = models.IntegerField(choices=CATEGORY.items(),
                                   null=True,
                                   verbose_name=u'收支类型')
    # 子收支款项记录
    items = models.ManyToManyField('finance.IncomeExpenseItem',
                                   verbose_name=u'子收支款项')
    # 收支款原因
    reason = models.TextField(verbose_name=u'收支款原因')
    # 收款-打款人 支出-收款人
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='income_expense_user',
                             null=True,
                             on_delete=models.SET_NULL,
                             verbose_name=u'打/收款人')
    # 经办人
    agent = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='income_expense_agent',
                              null=True,
                              on_delete=models.SET_NULL,
                              verbose_name=u'经办人')
    # 审批人
    approval_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      related_name='income_expense_approval_user',
                                      on_delete=models.CASCADE,
                                      verbose_name=u'审批人')
    # 审批结果选项
    APPROVAL_RESULT = {
        0: u'待审批',
        1: u'审批通过',
        2: u'审批拒绝',
    }
    approval_result = models.IntegerField(choices=APPROVAL_RESULT.items(),
                                          null=True,
                                          verbose_name=u'审批结果')
    # 经办金额
    value = models.DecimalField(default=0.00,
                                max_digits=12,
                                decimal_places=2,
                                verbose_name=u'经办金额')
    # 是否收款\支付
    is_receive_pay = models.BooleanField(default=False,
                                         verbose_name=u'是否收支款')
    # 收支方式
    receive_pay_way = models.CharField(max_length=255,
                                       null=True,
                                       verbose_name=u'收支款方式')
    # 收支流水号
    trade_no = models.CharField(max_length=255,
                                null=True,
                                verbose_name=u'收支款流水号')
    # 收支时间
    receive_pay_time = models.DateTimeField(default=timezone.now,
                                            verbose_name=u'收支款时间')
    # 备注
    note = models.CharField(max_length=255,
                            null=True,
                            verbose_name=u'备注')
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
        verbose_name = '收支款项'
        verbose_name_plural = '收支款项'

    def __str__(self):
        return self.agent.name + ' 金额:' + str(self.value)


# 子收支款项记录
class IncomeExpenseItem(models.Model):
    # 收入or支出
    INCOME_EXPENSE = {
        0: u'收入',
        1: u'支出',
    }
    income_expense = models.IntegerField(choices=INCOME_EXPENSE.items(),
                                         null=True,
                                         verbose_name=u'收入/支出')
    # 收支类型
    CATEGORY = {
        0: u'购课',
        1: u'充值',
        2: u'其他入账',
        3: u'工资',
        4: u'提成',
        5: u'其他出账',
    }
    category = models.IntegerField(choices=CATEGORY.items(),
                                   null=True,
                                   verbose_name=u'收支类型')
    # 收支款原因
    reason = models.TextField(verbose_name=u'收支款原因')
    # 收款-打款人 支出-收款人
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='income_expense_item_user',
                             null=True,
                             on_delete=models.SET_NULL,
                             verbose_name=u'打/收款人')
    # 经办金额
    value = models.DecimalField(default=0.00,
                                max_digits=12,
                                decimal_places=2,
                                verbose_name=u'经办金额')
    # 是否收款\支付
    is_receive_pay = models.BooleanField(default=False,
                                         verbose_name=u'是否收支款')
    # 收支方式
    receive_pay_way = models.CharField(max_length=255,
                                       null=True,
                                       verbose_name=u'收支款方式')
    # 收支流水号
    trade_no = models.CharField(max_length=255,
                                null=True,
                                verbose_name=u'收支款流水号')
    # 收支时间
    receive_pay_time = models.DateTimeField(default=timezone.now,
                                            verbose_name=u'收支款时间')
    # 备注
    note = models.CharField(max_length=255,
                            null=True,
                            verbose_name=u'备注')
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
        verbose_name = '收支子款项'
        verbose_name_plural = '收支子款项'

    def __str__(self):
        return self.user.name + ' 金额:' + str(self.value)