from xadmin.models import Log
import xadmin
from xadmin import views
from xadmin.views import CommAdminView, BaseAdminObject, LoginView
from qa.models import Log, QaLogEc, Product, Activity
from .models import User


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(CommAdminView):
    # 左上角及浏览器标题
    site_title = 'Glossa后台管理'
    # 页脚版权信息
    site_footer = 'Copyright © 2019 Glossa'
    menu_style = 'accordion'
    global_models_icon = {
        User: "glyphicon glyphicon-user",
        QaLogEc: "fa fa-comments-o",
        Log:"fa fa-comments",
        Product:"fa fa-apple",
        Activity:"fa fa-heart"

    }  # 设置models的全局图标


class LoginViewAdmin(LoginView):
    title = 'Glossa后台管理'


xadmin.site.register(LoginView, LoginViewAdmin)
xadmin.site.register(CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView, BaseSetting)



