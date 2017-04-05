from collections import OrderedDict

from rest_framework import serializers
from rest_framework.fields import SkipField

from .models import *


# 将None序列化为 '' 而不是 'null'
class ModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        """
              Object instance -> Dict of primitive data types.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                key = field.get_attribute(instance)
            except SkipField:
                continue
            if key is not None:
                value = field.to_representation(key)
                # 子对象中有对象为空 依旧序列化
                # if value is None:
                #     # Do not serialize empty objects
                #     print('empty objects')
                #     continue
                # 子对象中有列表为空 依旧序列化 eg:Moment->photos为空依旧要序列化
                # if isinstance(value, list) and not value:
                #     # Do not serialize empty lists
                #     print('empty lists')
                #     continue
                ret[field.field_name] = value
                # print(field.field_name, value)
            else:
                # value None to '' rather tan 'null'
                # print(field.field_name, field.to_representation(key), '有空值')
                ret[field.field_name] = ''

        # 为serializers中动态添加的context赋值输出
        for field in self.context:
            # context defaults to including 'request', 'view' and 'format' keys.
            if field not in ['request', 'view', 'format']:
                ret[field] = self.context[field]
        return ret


# 动态获取Fields
class DynamicFieldsModelSerializer(ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


# --------------------------------- 用户 ---------------------------------
# 创建用户
class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data, is_real=False):
        # 使用create_user不是create
        instance = User.objects.create_user(username=validated_data['username'],
                                            password=validated_data['password'],)
        return instance


# 列表用户
class UserListSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'portrait', 'gender', 'get_full_name', )


# 全部信息
class UserSerializer(ModelSerializer):
    # 设置修改email时返回400错误
    def validate_email(self, value):
        if value:
            raise serializers.ValidationError("Email需要验证后才可修改")
        return value

    class Meta:
        model = User
        fields = ('id', 'username', 'portrait', 'gender', 'name', 'birth_day', 'email',
                  'tel', 'fixed_tel', 'qq', 'we_chat', 'contact_address', )
        read_only_fields = ('username',)

