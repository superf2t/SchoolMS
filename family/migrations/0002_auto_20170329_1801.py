# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('family', '0001_initial'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='smstemplate',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sms_template_branch', to='school.Branch', verbose_name='校区'),
        ),
        migrations.AddField(
            model_name='smsrecord',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sms_record_branch', to='school.Branch', verbose_name='校区'),
        ),
    ]
