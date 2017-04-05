from collections import OrderedDict

from rest_framework import serializers
from rest_framework.fields import SkipField

from user.serializers import ModelSerializer, DynamicFieldsModelSerializer, UserListSerializer
from .models import *


# --------------------------------- 员工 ---------------------------------
# 创建员工
class StaffCreateSerializer(ModelSerializer):
    user = UserListSerializer()

    class Meta:
        model = Staff
        fields = ('user', 'category', 'id_no', 'bank_no', 'social_security_no', 'on_job', 'job_state')


# 列表员工
class StaffListSerializer(ModelSerializer):
    class Meta:
        model = Staff
        fields = ('id', 'user', 'category', 'id_no', 'bank_no', 'social_security_no', 'on_job', 'job_state')


# 员工
class StaffSerializer(ModelSerializer):
    class Meta:
        model = Staff
        fields = ('id', 'user', 'category', 'id_no', 'bank_no', 'social_security_no', 'on_job', 'job_state')


# --------------------------------- 学校 ---------------------------------
# 创建学校
class SchoolCreateSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = ('name', 'list_order')


# 列表学校
class SchoolListSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name', 'list_order', 'branches', 'departments')


# 学校
class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name', 'list_order', 'branches', 'departments')


# --------------------------------- 校区 ---------------------------------
# 创建校区
class BranchCreateSerializer(ModelSerializer):
    class Meta:
        model = Branch
        fields = ('name', 'list_order')


# 列表校区
class BranchListSerializer(ModelSerializer):
    class Meta:
        model = Branch
        fields = ('id', 'name', 'list_order', 'departments')


# 校区
class BranchSerializer(ModelSerializer):
    class Meta:
        model = Branch
        fields = ('id', 'name', 'list_order', 'departments')


# --------------------------------- 部门 ---------------------------------
# 创建部门
class DepartmentCreateSerializer(serializers.ModelSerializer):
    staffs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ('name', 'list_order', 'staffs')


# 列表部门
class DepartmentListSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'list_order', 'departments', 'staffs')


# 部门
class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'list_order', 'departments', 'staffs')