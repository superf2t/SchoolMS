from django.contrib import admin

from .models import *


# 优惠券
class DiscountCouponAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    search_fields = ('name',)
admin.site.register(DiscountCoupon, DiscountCouponAdmin)


# 优惠卷发行
class DiscountCouponPublishAdmin(admin.ModelAdmin):
    list_display = ['id', 'count', ]
    search_fields = ('discount_coupon__name',)
admin.site.register(DiscountCouponPublish, DiscountCouponPublishAdmin)


# 优惠券领取记录
class DiscountCouponRecordAdmin(admin.ModelAdmin):
    list_display = ['id', ]
    search_fields = ('coupon__name',)
admin.site.register(DiscountCouponRecord, DiscountCouponRecordAdmin)


# 优惠活动
class DiscountEventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    search_fields = ('name',)
admin.site.register(DiscountEvent, DiscountEventAdmin)
