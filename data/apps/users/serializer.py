import re

from rest_framework import serializers
from .models import User
class RegisterCreateSerializer(serializers.ModelSerializer):

    #用户再进行提交的时候有3个数据:校验密码,短信验证码,是否同意协议
    #所以,我们需要定义三个字段
    password2 = serializers.CharField(label='校验密码',allow_null=False,allow_blank=False,write_only=True)
    sms_code = serializers.CharField(label='短信验证码',max_length=6,min_length=6,allow_null=False,allow_blank=False,write_only=True)
    allow = serializers.CharField(label='是否同意协议',allow_null=False,allow_blank=False,write_only=True)

    class Meta:
        model = User
        fields = ('id','username','password','mobile','password2','sms_code','allow')
        extra_kwargs = {
            'id': {'read_only': True},
            'username': {
                'min_length': 5,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许5-20个字符的用户名',
                    'max_length': '仅允许5-20个字符的用户名',
                }
            },
            'password': {
                'write_only': True,
                'min_length': 8,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许8-20个字符的密码',
                    'max_length': '仅允许8-20个字符的密码',
                }
            }
        }

    # 进行校验
    # 单个字段的校验有 手机号码,是否同意协议
    def validate_mobile(self, value):
        if not re.match(r'1[345789]\d{9}', value):
            raise serializers.ValidationError('手机号格式不正确')
        return value

    def validate_allow(self, value):
        # 注意,前段提交的是否同意,我们已经转换为字符串
        if value != 'true':
            raise serializers.ValidationError('您未同意协议')
        return value

    # 多字段校验, 密码是否一致, 短信是否一致
    def validate(self, attrs):

        # 比较密码
        password = attrs['password']
        password2 = attrs['password2']

        if password != password2:
            raise serializers.ValidationError('密码不一致')
        # 比较手机验证码
        # 获取用户提交的验证码
        code = attrs['sms_code']
        # 获取redis中的验证码
        # redis_conn = get_redis_connection('code')
        # 获取手机号码
        # mobile = attrs['mobile']
        # redis_code = redis_conn.get('sms_%s' % mobile)
        # if redis_code is None:
        #     raise serializers.ValidationError('验证码过期')

        # if redis_code.decode() != code:
        #     raise serializers.ValidationError('验证码不正确')

        return attrs

    def create(self, validated_data):

        # 删除多余字段
        del validated_data['password2']
        del validated_data['sms_code']
        del validated_data['allow']

        user = super().create(validated_data)

        # 修改密码
        user.set_password(validated_data['password'])
        user.save()

        return user