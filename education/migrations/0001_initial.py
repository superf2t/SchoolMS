# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import user.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_unit_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, verbose_name='教师课时费单价')),
                ('class_type', models.IntegerField(choices=[(0, '集体班'), (1, '一对一')], null=True, verbose_name='班级类型')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='开班时间')),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='结班时间')),
                ('total_plan', models.IntegerField(default=0, verbose_name='预招人数')),
                ('total_current', models.IntegerField(default=0, verbose_name='当前人数')),
                ('arrange_hours_yet', models.IntegerField(default=0, verbose_name='已排课时')),
                ('class_state', models.IntegerField(choices=[(0, '待开班'), (1, '进行中'), (2, '已结班')], null=True, verbose_name='班级状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '班级',
                'verbose_name_plural': '班级',
            },
        ),
        migrations.CreateModel(
            name='ClassExpenseRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '学员课消记录',
                'verbose_name_plural': '学员课消记录',
            },
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='名称')),
                ('place', models.CharField(max_length=255, null=True, verbose_name='具体地点')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '教室',
                'verbose_name_plural': '教室',
            },
        ),
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='日期')),
                ('start_time', models.TimeField(default=django.utils.timezone.now, verbose_name='上课时间')),
                ('end_time', models.TimeField(default=django.utils.timezone.now, verbose_name='下课时间')),
                ('hours', models.IntegerField(default=0, verbose_name='本次课时')),
                ('teacher_unit_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, verbose_name='教师课时费单价')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '课程表',
                'verbose_name_plural': '课程表',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restrict_branch', models.BooleanField(default=True, verbose_name='是否限制校区')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='名称')),
                ('course_type', models.IntegerField(choices=[(0, '集体班'), (1, '一对一')], null=True, verbose_name='课程类型')),
                ('course_state', models.IntegerField(choices=[(0, '启用'), (1, '停用')], null=True, verbose_name='课程状态')),
                ('charge_mode', models.IntegerField(choices=[(0, '按课时'), (1, '按期')], null=True, verbose_name='计费方式')),
                ('total_hours', models.IntegerField(default=0, verbose_name='总课时')),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, verbose_name='课时单价')),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='课程总价')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
            },
        ),
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='名称')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '课程分类',
                'verbose_name_plural': '课程分类',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign_up_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='报名时间')),
                ('card_no', models.CharField(blank=True, max_length=40, null=True, verbose_name='卡号')),
                ('student_no', models.CharField(blank=True, max_length=40, null=True, verbose_name='学号')),
                ('photo', models.ImageField(blank=True, default='default.png', storage=user.storage.ImageStorage(base_url='/media/user_photo/', location='C:\\django\\SchoolMS\\media/user/'), upload_to='', verbose_name='相片')),
            ],
            options={
                'verbose_name': '学员',
                'verbose_name_plural': '学员',
            },
        ),
        migrations.CreateModel(
            name='StudentAttendanceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, '出勤'), (1, '缺勤')], null=True, verbose_name='出勤状态')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='考勤时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '学员考勤记录',
                'verbose_name_plural': '学员考勤记录',
            },
        ),
        migrations.CreateModel(
            name='TeacherAttendanceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, '出勤'), (1, '缺勤')], null=True, verbose_name='出勤状态')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='考勤时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '教师上课记录',
                'verbose_name_plural': '教师上课记录',
            },
        ),
        migrations.CreateModel(
            name='TemporaryClassSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operate', models.IntegerField(choices=[(0, '新增'), (1, '调换'), (2, '删除')], null=True, verbose_name='操作')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('new_class_schedule', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='temporary_class_schedule_new', to='education.ClassSchedule', verbose_name='新课表记录')),
                ('old_class_schedule', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='temporary_class_schedule_old', to='education.ClassSchedule', verbose_name='旧课表记录')),
            ],
            options={
                'verbose_name': '临时调课记录',
                'verbose_name_plural': '临时调课记录',
            },
        ),
    ]