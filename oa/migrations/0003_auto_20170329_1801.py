# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 10:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0002_auto_20170329_1801'),
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oa', '0002_workreporttemplate_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='workreport',
            name='report_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_report_report_user', to=settings.AUTH_USER_MODEL, verbose_name='报告人'),
        ),
        migrations.AddField(
            model_name='notificationtemplate',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notification_template_branch', to='school.Branch', verbose_name='校区'),
        ),
        migrations.AddField(
            model_name='notification',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_from_user', to=settings.AUTH_USER_MODEL, verbose_name='通知发起人'),
        ),
        migrations.AddField(
            model_name='notification',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.Group', verbose_name='通知员工职务'),
        ),
        migrations.AddField(
            model_name='emailtemplate',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='email_template_branch', to='school.Branch', verbose_name='校区'),
        ),
        migrations.AddField(
            model_name='email',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_from_user', to=settings.AUTH_USER_MODEL, verbose_name='发件人'),
        ),
        migrations.AddField(
            model_name='email',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_to_user', to=settings.AUTH_USER_MODEL, verbose_name='收件人'),
        ),
    ]
