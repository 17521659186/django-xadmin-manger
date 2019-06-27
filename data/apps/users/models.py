from django.contrib.auth.models import AbstractUser,UserManager
from django.db import models


# Create your models here.

# 用户模型类

class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    IsAdmin = models.IntegerField(default=0)
    IsProp = models.IntegerField(default=0)
    dispalyName = models.CharField(max_length=11,default="user")


    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户的详细信息'
        verbose_name_plural = verbose_name


# # 日志模型类
# class Qa(models.Model):
#
#     user_id = models.CharField(max_length=45)
#     conversion_id = models.TextField()
#     question = models.TextField()
#     answer = models.TextField()
#     create_time = models.DateTimeField()
#     intent = models.CharField(max_length=255)
#
#     class Meta:
#         db_table = 'qa_log'
#         verbose_name = '日志'
#         verbose_name_plural = verbose_name
