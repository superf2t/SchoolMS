from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Permission, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.contenttypes.models import ContentType

from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import *
from .serializers import *
from .permissions import *
from logger.views import add_log, queryset_str

import logging
logger = logging.getLogger("app_info")


# 成功时返回 200-code
def success_response(data):
    return Response(data=data, status=status.HTTP_200_OK)


# 错误时返回 400-code
def error_response(code, data):
    logger.error("code: %d, data: %s" % (code, data))
    return Response(data={'code': code, 'data': data}, status=status.HTTP_400_BAD_REQUEST)


# 用户视图集
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    # 403 错误均为未登录
    permission_classes = (IsAuthenticated,)

    # 重写 create 方法权限为AllowAny
    def get_permissions(self):
        if self.action in ('create', ):
            self.permission_classes = [AllowAny, ]
        return super(self.__class__, self).get_permissions()

    # override POST /user/
    # 用户注册
    # Receive ----------------------------------
    # username: 手机号码
    # password: md5后密码
    # Return -----------------------------------
    # 200 注册成功 400-1 数据格式错误
    def create(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            # 注册一个真实用户
            user = serializer.create(serializer.validated_data)
            if not user.is_superuser:
                # 为该用户生成Token
                token = Token.objects.create(user=user)
                token.save()

                # 设置权限
                assign_group(user, '任课老师')
            add_log(user, 1, '注册账号')
            return success_response('注册成功')
        else:
            return error_response(1, serializer.errors)

    # override GET /user/
    # 查看用户列表
    # Return -----------------------------------
    # 200 列表信息
    def list(self, request, *args, **kwargs):
        permission_required(request.user, ['user.view_user'])
        if group_required(request.user, '任课老师'):
            users = User.objects.filter(groups__name__contains='学生')
        else:
            users = User.objects.all()
        serializer = UserListSerializer(users, context={'request': request}, many=True)
        return success_response(serializer.data)

    # override GET /user/user_id/
    # 获取用户信息
    # Return -----------------------------------
    # 200 用户信息 400-1 用户不存在
    def retrieve(self, request, *args, **kwargs):
        permission_required(request.user, ['user.view_user'])
        try:
            user = User.objects.get(pk=kwargs['pk'])
            if user == request.user:
                serializer = UserSerializer(request.user, context={'request': request})
                return success_response(serializer.data)
        except ObjectDoesNotExist:
            return error_response(1, '用户不存在')

    # override PUT /user/user_id/
    # 部分更新用户
    # Return -----------------------------------
    # 200 用户信息 400-1 数据格式错误
    def update(self, request, *args, **kwargs):
        permission_required(request.user, ['user.change_user'])
        user = User.objects.get(pk=kwargs['pk'])
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            add_log(request.user, 2, '修改用户%s的信息，%s' % (user.get_full_name(), queryset_str(request.data)))
            return success_response(serializer.data)
        else:
            return error_response(1, serializer.errors)

    # override Delete /user/user_id/
    # 删除用户
    # Return -----------------------------------
    # 200 删除成功 400-1 用户不存在
    def destroy(self, request, *args, **kwargs):
        permission_required(request.user, ['user.delete_user'])
        try:
            user = User.objects.get(pk=kwargs['pk'])
            add_log(request.user, 3, '删除用户%s' % user.get_full_name())
            user.delete()
            return success_response('删除成功')
        except ObjectDoesNotExist:
            return error_response(1, '用户不存在')

    # 用户登陆
    # Receive ----------------------------------
    # username: 手机号码
    # password: md5后密码
    # Return -----------------------------------
    # 200 登陆成功 400-1 数据格式错误
    # 400-2 无此用户 400-3 密码错误
    @list_route(methods=['POST'], permission_classes=[AllowAny])
    def login(self, request):
        try:
            if not User.objects.filter(username=request.data['username']).exists():
                return error_response(2, '无此用户')
            user = authenticate(username=request.data['username'],
                                password=request.data['password'])
            if user is not None:
                # 登陆系统
                login(request, user)
                # 获取授权信息
                token = user.token
                data = {'id': user.id, 'token': token.access_token}
                return success_response(data)
            else:
                return error_response(3, '密码错误')
        except Exception as e:
            return error_response(1, '获取参数%s失败' % e)


