from django.conf.urls import url
from . import views

urlpatterns = [

    # 登陆之前获取csrftoken
    url(r"^csrf$",views.CsrfTokenView.as_view()),
    # 分析师用户登陆界面
    url(r"^login$",views.UserLoginViews.as_view()),
    # 管理员后台登陆
    url(r"^admin$",views.AdminLoginViews.as_view()),
    # 用户名重复性校验
    url(r"^check$",views.UserNameCheckView.as_view()),
    # 分析师用户注册页面


]