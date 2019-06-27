from django.contrib import admin

# Register your models here.
from .models import User


# 定义管理模型类
class UserAdmin(admin.ModelAdmin):
    # 需要显示的字段信息
    list_display = ("id", "username", "password", "IsAdmin", "IsProp", "mobile","dispalyName")
    # 设置那些字段可以点击进入编辑页面
    list_display_links = ("id", "username", "password", "IsAdmin", "IsProp", "mobile","dispalyName")





# 注册管理类
admin.site.register(User, UserAdmin)




