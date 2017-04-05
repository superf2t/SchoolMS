# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 13:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0003_auto_20170329_1801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'permissions': (('view_notice', 'Can view 公告'),), 'verbose_name': '公告', 'verbose_name_plural': '公告'},
        ),
        migrations.AlterModelOptions(
            name='noticetemplate',
            options={'permissions': (('view_noticetemplate', 'Can view 公告模板'),), 'verbose_name': '公告模板', 'verbose_name_plural': '公告模板'},
        ),
        migrations.AlterModelOptions(
            name='sms',
            options={'permissions': (('view_sms', 'Can view 短信'),), 'verbose_name': '短信', 'verbose_name_plural': '短信'},
        ),
        migrations.AlterModelOptions(
            name='smsassign',
            options={'permissions': (('view_smsassign', 'Can view 短信分配'),), 'verbose_name': '短信分配', 'verbose_name_plural': '短信分配'},
        ),
        migrations.AlterModelOptions(
            name='smsrecord',
            options={'permissions': (('view_smsrecord', 'Can view 短信记录'),), 'verbose_name': '短信记录', 'verbose_name_plural': '短信记录'},
        ),
        migrations.AlterModelOptions(
            name='smstemplate',
            options={'permissions': (('view_smstemplate', 'Can view 短信模板'),), 'verbose_name': '短信模板', 'verbose_name_plural': '短信模板'},
        ),
    ]
