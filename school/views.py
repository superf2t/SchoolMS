from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status, viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.permissions import IsAuthenticated

from user.views import success_response, error_response, logger
from user.permissions import permission_required, group_required
from .models import *
from .serializers import *
from logger.views import add_log, queryset_str


# 学校视图集
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolCreateSerializer
    permission_classes = (IsAuthenticated,)

    # override POST /school/
    # 添加学校
    # Receive ----------------------------------
    # name: 学校名称
    # list_order: 学校排序
    # Return -----------------------------------
    # 200 添加成功 400-1 数据格式错误
    def create(self, request, *args, **kwargs):
        permission_required(request.user, ['school.add_school'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # 添加学校
            school = serializer.create(serializer.validated_data)

            add_log(request.user, 1, '添加学校 %s' % school.name)
            return success_response('添加成功')
        else:
            return error_response(1, serializer.errors)

    # override GET /school/
    # 查看学校列表
    def list(self, request, *args, **kwargs):
        permission_required(request.user, ['school.view_school'])
        schools = School.objects.all()
        serializer = SchoolListSerializer(schools, context={'request': request}, many=True)
        return success_response(serializer.data)

    # override GET /school/school_id/
    # 获取学校信息
    # Return -----------------------------------
    # 200 查看成功 400-1 学校不存在
    def retrieve(self, request, *args, **kwargs):
        permission_required(request.user, ['school.view_school'])
        try:
            school = School.objects.get(pk=kwargs['pk'])
            serializer = SchoolSerializer(school, context={'request': request})
            return success_response(serializer.data)
        except ObjectDoesNotExist:
            return error_response(1, '学校不存在')

    # override PUT /school/school_id/
    # 部分更新学校
    # Return -----------------------------------
    # 200 学校信息 400-1 数据格式错误
    def update(self, request, *args, **kwargs):
        permission_required(request.user, ['school.change_school'])
        school = School.objects.get(pk=kwargs['pk'])
        serializer = SchoolSerializer(school, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            add_log(request.user, 2, '修改学校 %s信息，%s' % (school.name, queryset_str(request.data)))
            return success_response(serializer.data)
        else:
            return error_response(1, serializer.errors)

    # override Delete /school/school_id/
    # 删除某个学校
    # Return -----------------------------------
    # 200 删除成功 400-1 学校不存在
    def destroy(self, request, *args, **kwargs):
        permission_required(request.user, ['school.delete_school'])
        try:
            school = School.objects.get(pk=kwargs['pk'])
            add_log(request.user, 3, '删除学校 %s' % school.name)
            school.delete()
            return success_response('删除成功')
        except ObjectDoesNotExist:
            return error_response(1, '学校不存在')


# 校区视图集
class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchCreateSerializer
    permission_classes = (IsAuthenticated,)

    # override POST /branch/
    # 添加校区
    # Receive ----------------------------------
    # name: 校区名称
    # list_order: 校区排序
    # Return -----------------------------------
    # 200 添加成功 400-1 数据格式错误
    def create(self, request, *args, **kwargs):
        permission_required(request.user, ['school.add_branch'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # 添加校区
            branch = serializer.create(serializer.validated_data)

            add_log(request.user, 1, '添加校区 %s' % branch.name)
            return success_response('添加成功')
        else:
            return error_response(1, serializer.errors)

    # override GET /branch/
    # 查看校区列表
    def list(self, request, *args, **kwargs):
        permission_required(request.user, ['school.view_branch'])
        branches = Branch.objects.all()
        serializer = BranchListSerializer(branches, context={'request': request}, many=True)
        return success_response(serializer.data)

    # override GET /branch/branch_id/
    # 获取校区信息
    # Return -----------------------------------
    # 200 查看成功 400-1 校区不存在
    def retrieve(self, request, *args, **kwargs):
        permission_required(request.user, ['school.view_branch'])
        try:
            branch = Branch.objects.get(pk=kwargs['pk'])
            serializer = BranchSerializer(branch, context={'request': request})
            return success_response(serializer.data)
        except ObjectDoesNotExist:
            return error_response(1, '校区不存在')

    # override PUT /branch/branch_id/
    # 部分更新校区
    # Return -----------------------------------
    # 200 校区信息 400-1 数据格式错误
    def update(self, request, *args, **kwargs):
        permission_required(request.user, ['school.change_branch'])
        branch = Branch.objects.get(pk=kwargs['pk'])
        serializer = SchoolSerializer(branch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            add_log(request.user, 2, '修改校区 %s信息，%s' % (branch.name, queryset_str(request.data)))
            return success_response(serializer.data)
        else:
            return error_response(1, serializer.errors)

    # override Delete /branch/branch_id/
    # 删除某个校区
    # Return -----------------------------------
    # 200 删除成功 400-1 校区不存在
    def destroy(self, request, *args, **kwargs):
        permission_required(request.user, ['school.delete_branch'])
        try:
            branch = Branch.objects.get(pk=kwargs['pk'])
            add_log(request.user, 3, '删除校区 %s' % branch.name)
            branch.delete()
            return success_response('删除成功')
        except ObjectDoesNotExist:
            return error_response(1, '校区不存在')


# 部门视图集
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentCreateSerializer
    permission_classes = (IsAuthenticated,)

    # override POST /department/
    # 添加部门
    # Receive ----------------------------------
    # name: 部门名称
    # list_order: 部门排序
    # Return -----------------------------------
    # 200 添加成功 400-1 数据格式错误
    def create(self, request, *args, **kwargs):
        permission_required(request.user, ['school.add_department'])
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # 添加部门
            department = serializer.create(serializer.validated_data)

            add_log(request.user, 1, '添加部门 %s' % department.name)
            return success_response('添加成功')
        else:
            return error_response(1, serializer.errors)

    # override GET /department/
    # 查看部门列表
    def list(self, request, *args, **kwargs):
        permission_required(request.user, ['school.view_department'])
        departments = Department.objects.all()
        serializer = DepartmentListSerializer(departments, context={'request': request}, many=True)
        return success_response(serializer.data)

    # override GET /department/department_id/
    # 获取部门信息
    # Return -----------------------------------
    # 200 查看成功 400-1 部门不存在
    def retrieve(self, request, *args, **kwargs):
        permission_required(request.user, ['school.view_department'])
        try:
            department = Department.objects.get(pk=kwargs['pk'])
            serializer = DepartmentSerializer(department, context={'request': request})
            return success_response(serializer.data)
        except ObjectDoesNotExist:
            return error_response(1, '部门不存在')

    # override PUT /department/department_id/
    # 部分更新部门
    # Return -----------------------------------
    # 200 部门信息 400-1 数据格式错误
    def update(self, request, *args, **kwargs):
        permission_required(request.user, ['school.change_department'])
        department = Department.objects.get(pk=kwargs['pk'])
        serializer = DepartmentSerializer(department, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            add_log(request.user, 2, '修改部门 %s信息，%s' % (department.name, queryset_str(request.data)))
            return success_response(serializer.data)
        else:
            return error_response(1, serializer.errors)

    # override Delete /department/department_id/
    # 删除某个部门
    # Return -----------------------------------
    # 200 删除成功 400-1 部门不存在
    def destroy(self, request, *args, **kwargs):
        permission_required(request.user, ['school.delete_branch'])
        try:
            department = Department.objects.get(pk=kwargs['pk'])
            add_log(request.user, 3, '删除部门 %s' % department.name)
            department.delete()
            return success_response('删除成功')
        except ObjectDoesNotExist:
            return error_response(1, '部门不存在')


# 员工视图集
class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffCreateSerializer
    permission_classes = (IsAuthenticated,)

    # override POST /staff/
    # 添加员工
    # Receive ----------------------------------
    # name: 员工名称
    # Return -----------------------------------
    # 200 添加成功 400-1 数据格式错误
    def create(self, request, *args, **kwargs):
        permission_required(request.user, ['school.add_staff'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # 添加部门
            staff = serializer.create(serializer.validated_data)

            add_log(request.user, 1, '添加员工 %s' % staff.user.name)
            return success_response('添加成功')
        else:
            return error_response(1, serializer.errors)

    # override GET /staff/
    # 查看员工列表
    def list(self, request, *args, **kwargs):
        permission_required(request.user, ['school.view_staff'])
        departments = Staff.objects.all()
        serializer = StaffListSerializer(departments, context={'request': request}, many=True)
        return success_response(serializer.data)

    # override GET /staff/staff_id/
    # 获取员工信息
    # Return -----------------------------------
    # 200 查看成功 400-1 员工不存在
    def retrieve(self, request, *args, **kwargs):
        permission_required(request.user, ['school.view_staff'])
        try:
            staff = Staff.objects.get(pk=kwargs['pk'])
            serializer = StaffSerializer(staff, context={'request': request})
            return success_response(serializer.data)
        except ObjectDoesNotExist:
            return error_response(1, '员工不存在')

    # override PUT /staff/staff_id/
    # 部分更新员工
    # Return -----------------------------------
    # 200 员工信息 400-1 数据格式错误
    def update(self, request, *args, **kwargs):
        permission_required(request.user, ['school.change_staff'])
        staff = Staff.objects.get(pk=kwargs['pk'])
        serializer = StaffSerializer(staff, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            add_log(request.user, 2, '修改员工 %s信息，%s' % (staff.user.name, queryset_str(request.data)))
            return success_response(serializer.data)
        else:
            return error_response(1, serializer.errors)

    # override Delete /staff/staff_id/
    # 删除某个员工
    # Return -----------------------------------
    # 200 删除成功 400-1 员工不存在
    def destroy(self, request, *args, **kwargs):
        permission_required(request.user, ['school.delete_staff'])
        try:
            staff = Staff.objects.get(pk=kwargs['pk'])
            add_log(request.user, 3, '删除员工 %s' % staff.user.name)
            staff.delete()
            return success_response('删除成功')
        except ObjectDoesNotExist:
            return error_response(1, '员工不存在')