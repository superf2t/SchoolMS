# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountCoupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='名称')),
                ('category', models.IntegerField(choices=[(0, '打折券'), (1, '优惠券')], null=True, verbose_name='优惠劵类别')),
                ('discount_percent', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=3, verbose_name='折扣比例')),
                ('discount_amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, verbose_name='折扣金额')),
                ('content', models.CharField(blank=True, max_length=255, null=True, verbose_name='优惠劵内容')),
                ('minimum_consumption', models.IntegerField(default=0, verbose_name='最低消费')),
                ('expiration_type', models.IntegerField(choices=[(0, '长期有效'), (1, '固定日期到期'), (2, '自领取后几日到期')], null=True, verbose_name='有效期类型')),
                ('expiration_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='到期时间')),
                ('expiration_day', models.IntegerField(blank=True, default=0, null=True, verbose_name='可持续天数')),
                ('is_abandon', models.BooleanField(default=False, verbose_name='是否停用')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '优惠券',
                'verbose_name_plural': '优惠券',
            },
        ),
        migrations.CreateModel(
            name='DiscountCouponPublish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, verbose_name='预发数量')),
                ('limit_everyday', models.IntegerField(default=0, verbose_name='限领数量-单人每天')),
                ('limit_all', models.IntegerField(default=0, verbose_name='限领数量-单人总领取数量')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '优惠券发放',
                'verbose_name_plural': '优惠券发放',
            },
        ),
        migrations.CreateModel(
            name='DiscountCouponRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receive_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='领取时间')),
                ('expiration_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='到期时间')),
                ('is_locked', models.BooleanField(default=False, verbose_name='是否锁定')),
                ('is_used', models.BooleanField(default=False, verbose_name='是否已使用')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('coupon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coupon_record_coupon', to='market.DiscountCoupon', verbose_name='优惠券')),
                ('coupon_original', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coupon_record_coupon_original', to='market.DiscountCoupon', verbose_name='原始优惠券')),
            ],
            options={
                'verbose_name': '优惠券领取记录',
                'verbose_name_plural': '优惠券领取记录',
            },
        ),
        migrations.CreateModel(
            name='DiscountEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='名称')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='开始时间')),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='结束时间')),
                ('category', models.IntegerField(choices=[(0, '打折'), (1, '充值送金额'), (2, '充值送积分'), (3, '消费满减金额'), (4, '消费满送余额'), (5, '消费送积分')], null=True, verbose_name='优惠活动类别')),
                ('details', models.TextField(verbose_name='优惠详情')),
                ('discount_percent', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=3, verbose_name='折扣比例')),
                ('category_type', models.IntegerField(choices=[(0, '只满减'), (1, '每满x减\\送x')], null=True, verbose_name='满减\\送类型')),
                ('satisfy', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='满x')),
                ('subtract_give', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='减\\送x')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '优惠活动',
                'verbose_name_plural': '优惠活动',
            },
        ),
    ]
