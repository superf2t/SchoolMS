from django.contrib import admin
from .models import *


# 准学员购课记录
class PreStudentPaymentRecordsAdmin(admin.ModelAdmin):
    list_display = ('id', )
    filter_horizontal = ('courses', 'items')
    search_fields = ('pre_student__user__name',)
admin.site.register(PreStudentPaymentRecords, PreStudentPaymentRecordsAdmin)


# 准学员购课单条记录
class PreStudentPaymentItemAdmin(admin.ModelAdmin):
    list_display = ('id', )
    search_fields = ('pre_student__user__name',)
admin.site.register(PreStudentPaymentItem, PreStudentPaymentItemAdmin)


# 购课提成
class PreStudentPaymentDeductAdmin(admin.ModelAdmin):
    list_display = ('id', 'reason', 'total_amount', 'real_amount')
    search_fields = ('user__username',)
admin.site.register(PreStudentPaymentDeduct, PreStudentPaymentDeductAdmin)


# 积分
class PointAdmin(admin.ModelAdmin):
    list_display = ('user', 'value')
    search_fields = ('user',)
admin.site.register(Point, PointAdmin)


# 积分变更记录
class PointChangeLogAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'change_value', 'value_after', 'change_reason', 'create_time')
    search_fields = ('point__user__username',)

    def get_user(self, obj):
        return obj.point.user.username
    get_user.short_description = '用户'
admin.site.register(PointChangeLog, PointChangeLogAdmin)


# 积分充值记录
class PointReChargeLogAdmin(admin.ModelAdmin):
    list_display = ('point', 'out_trade_no', 'platform', 'recharge_amount', 'is_pay', 'update_time')
    search_fields = ('point__user__username',)
admin.site.register(PointReChargeLog, PointReChargeLogAdmin)


# 余额
class BalanceAdmin(admin.ModelAdmin):
    search_fields = ('user',)
    list_display = ('user', 'value')
admin.site.register(Balance, BalanceAdmin)


# 余额变更记录
class BalanceChangeLogAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'change_value', 'value_after', 'change_reason', 'create_time')
    search_fields = ('balance__user__username',)

    def get_user(self, obj):
        return obj.point.user.username
    get_user.short_description = '用户'
admin.site.register(BalanceChangeLog, BalanceChangeLogAdmin)


# 积分充值记录
class BalanceReChargeLogAdmin(admin.ModelAdmin):
    list_display = ('balance', 'out_trade_no', 'platform', 'recharge_amount', 'is_pay', 'update_time')
    search_fields = ('balance__user__username',)
admin.site.register(BalanceReChargeLog, BalanceReChargeLogAdmin)


# 收支款项经办
class IncomeExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'income_expense', 'category', 'get_user', 'reason', 'value', 'is_receive_pay',
                    'receive_pay_way', 'trade_no', 'receive_pay_time')
    search_fields = ('balance__user__username',)
    filter_horizontal = ('items', )

    def get_user(self, obj):
        return obj.agent.get_full_name()
    get_user.short_description = '经办人'
admin.site.register(IncomeExpense, IncomeExpenseAdmin)


# 子收支款项经办
class IncomeExpenseItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'income_expense', 'category', 'get_user', 'reason', 'value', 'is_receive_pay',
                    'receive_pay_way', 'trade_no', 'receive_pay_time')
    search_fields = ('balance__user__username',)

    def get_user(self, obj):
        return obj.user.get_full_name()
    get_user.short_description = '打/收款人'
admin.site.register(IncomeExpenseItem, IncomeExpenseItemAdmin)