# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 10:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('education', '0001_initial'),
        ('admission', '0002_auto_20170329_1801'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporaryclassschedule',
            name='operator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='temporary_class_schedule_operator', to=settings.AUTH_USER_MODEL, verbose_name='操作人'),
        ),
        migrations.AddField(
            model_name='teacherattendancerecord',
            name='class_schedule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_attendance_record_class_schedule', to='education.ClassSchedule', verbose_name='课表记录'),
        ),
        migrations.AddField(
            model_name='teacherattendancerecord',
            name='operator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_attendance_record_operator', to=settings.AUTH_USER_MODEL, verbose_name='操作人'),
        ),
        migrations.AddField(
            model_name='teacherattendancerecord',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_attendance_record_teacher', to='school.Staff', verbose_name='教师'),
        ),
        migrations.AddField(
            model_name='studentattendancerecord',
            name='class_schedule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_attendance_record_class_schedule', to='education.ClassSchedule', verbose_name='课表记录'),
        ),
        migrations.AddField(
            model_name='studentattendancerecord',
            name='operator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_attendance_record_operator', to=settings.AUTH_USER_MODEL, verbose_name='操作人'),
        ),
        migrations.AddField(
            model_name='studentattendancerecord',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_attendance_record_student', to='education.Student', verbose_name='学员'),
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, to='education.Course', verbose_name='报名课程'),
        ),
        migrations.AddField(
            model_name='student',
            name='pre_student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_pre_student', to='admission.PreStudent', verbose_name='准学员'),
        ),
        migrations.AddField(
            model_name='coursecategory',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_category_branch', to='school.Branch', verbose_name='校区'),
        ),
        migrations.AddField(
            model_name='course',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_branch', to='school.Branch', verbose_name='校区'),
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_category', to='education.CourseCategory', verbose_name='所属分类'),
        ),
        migrations.AddField(
            model_name='classschedule',
            name='class_room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_schedule_room', to='education.ClassRoom', verbose_name='教室'),
        ),
        migrations.AddField(
            model_name='classschedule',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_schedule_course', to='education.Course', verbose_name='课程'),
        ),
        migrations.AddField(
            model_name='classschedule',
            name='on_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_schedule_class', to='education.Class', verbose_name='班级'),
        ),
        migrations.AddField(
            model_name='classschedule',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_schedule_teacher', to='school.Staff', verbose_name='教师'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_room_branch', to='school.Branch', verbose_name='校区'),
        ),
        migrations.AddField(
            model_name='classexpenserecord',
            name='class_schedule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_expense_class_schedule', to='education.ClassSchedule', verbose_name='课表记录'),
        ),
        migrations.AddField(
            model_name='classexpenserecord',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_expense_student', to='education.Student', verbose_name='学员'),
        ),
        migrations.AddField(
            model_name='class',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_branch', to='school.Branch', verbose_name='校区'),
        ),
        migrations.AddField(
            model_name='class',
            name='class_room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_class_room', to='education.ClassRoom', verbose_name='教室'),
        ),
        migrations.AddField(
            model_name='class',
            name='course',
            field=models.ManyToManyField(to='education.Course', verbose_name='课程'),
        ),
        migrations.AddField(
            model_name='class',
            name='in_charge',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='班级负责人'),
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(to='education.Student', verbose_name='学员'),
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_teacher', to='school.Staff', verbose_name='教师'),
        ),
    ]
