# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 05:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20170329_1801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school',
            options={'permissions': (('view_school', 'Can view 学校'),), 'verbose_name': '学校', 'verbose_name_plural': '学校'},
        ),
    ]
