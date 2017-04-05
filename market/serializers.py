from collections import OrderedDict

from rest_framework import serializers
from rest_framework.fields import SkipField

from user.serializers import ModelSerializer, DynamicFieldsModelSerializer, UserListSerializer
from .models import *


# --------------------------------- 优惠券 ---------------------------------
# 创建优惠券
class DiscountCouponCreateSerializer(ModelSerializer):
    class Meta:
        model = DiscountCoupon
        fields = ('name', 'category', 'discount_percent', 'discount_amount', 'content', 'minimum_consumption',
                  'expiration_type', 'expiration_time', 'expiration_day', 'is_abandon')


# 列表优惠券
class DiscountCouponListSerializer(ModelSerializer):
    class Meta:
        model = DiscountCoupon
        fields = ('id', 'name', 'category', 'discount_percent', 'discount_amount', 'content',
                  'minimum_consumption', 'expiration_type', 'expiration_time', 'expiration_day', 'is_abandon')


# 优惠券
class DiscountCouponSerializer(ModelSerializer):
    class Meta:
        model = DiscountCoupon
        fields = ('id', 'name', 'category', 'discount_percent', 'discount_amount', 'content',
                  'minimum_consumption', 'expiration_type', 'expiration_time', 'expiration_day', 'is_abandon')


# --------------------------------- 优惠券发放 ---------------------------------
# 创建优惠券发放
class DiscountCouponPublishCreateSerializer(ModelSerializer):
    class Meta:
        model = DiscountCouponPublish
        fields = ('publisher', 'discount_coupon', 'count', 'limit_everyday', 'limit_all')


# 列表优惠券发放
class DiscountCouponPublishListSerializer(ModelSerializer):
    class Meta:
        model = DiscountCouponPublish
        fields = ('id', 'publisher', 'discount_coupon', 'count', 'limit_everyday', 'limit_all')


# 优惠券发放
class DiscountCouponPublishSerializer(ModelSerializer):
    class Meta:
        model = DiscountCouponPublish
        fields = ('id', 'publisher', 'discount_coupon', 'count', 'limit_everyday', 'limit_all')


# --------------------------------- 优惠券领取记录 ---------------------------------
# 创建优惠券领取记录
class DiscountCouponRecordCreateSerializer(ModelSerializer):
    class Meta:
        model = DiscountCouponRecord
        fields = ('coupon', 'coupon_original', 'user', 'receive_time', 'expiration_time', 'is_locked', 'is_used')


# 列表优惠券领取记录
class DiscountCouponRecordListSerializer(ModelSerializer):
    class Meta:
        model = DiscountCouponRecord
        fields = ('id', 'coupon', 'coupon_original', 'user', 'receive_time', 'expiration_time', 'is_locked', 'is_used')


# 优惠券领取记录
class DiscountCouponRecordSerializer(ModelSerializer):
    class Meta:
        model = DiscountCouponRecord
        fields = ('id', 'coupon', 'coupon_original', 'user', 'receive_time', 'expiration_time', 'is_locked', 'is_used')


# --------------------------------- 优惠活动 ---------------------------------
# 创建优惠活动
class DiscountEventCreateSerializer(ModelSerializer):
    class Meta:
        model = DiscountEvent
        fields = ('name', 'start_time', 'end_time', 'category', 'details', 'discount_percent', 'category_type',
                  'satisfy', 'subtract_give')


# 列表优惠活动
class DiscountEventListSerializer(ModelSerializer):
    class Meta:
        model = DiscountEvent
        fields = ('id', 'name', 'start_time', 'end_time', 'category', 'details', 'discount_percent',
                  'category_type', 'satisfy', 'subtract_give')


# 优惠活动
class DiscountEventSerializer(ModelSerializer):
    class Meta:
        model = DiscountEvent
        fields = ('id', 'name', 'start_time', 'end_time', 'category', 'details', 'discount_percent',
                  'category_type', 'satisfy', 'subtract_give')
