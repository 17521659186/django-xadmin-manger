import xadmin

from .models import Log, Product, QaLogEc, Activity


# 日志管理类
class LogAdmin(object):
    list_display = ['user_id', 'conversion_id', "question", "answer", "create_time", "intent"]
    search_fields = ['user_id', 'conversion_id', "question", "answer", "create_time", "intent"]
    list_filter = ['user_id', 'conversion_id', "question", "answer", "create_time", "intent"]
    list_per_page = 100


"""
# 微信日志管理类
class WxLogAdmin(object):
    list_display = ['openid',  "question", "answer", "create_time"]
    search_fields = ['openid',  "question", "answer", "create_time"]
    list_filter = ['openid',  "question", "answer", "create_time"]

"""


# EC日志管理类
class QaLogEcAdmin(object):
    list_display = ["id", "question", "answer", "create_time", "source_type", "intent"]
    search_fields = ['user_id', "session_id", "source_type", "question", "create_time"]
    list_filter = ['user_id', "session_id", "source_type", "question", "create_time"]
    list_editable = ['user_id', 'question']  # 可以编辑的字段
    list_per_page = 50
    reversion_enable = True


# 产品管理类
class ProductAdmin(object):
    # 展示的字段
    list_display = ['id', 'pid', 'cat_lv1', 'cat_lv2', 'cat_lv3', 'series', 'product', 'intro', 'capacity', "price",
                    'color', 'color_series', 'is_best_color', "ec_activity", "efficacy", "skin_type", "complexion",
                    "image", "link", "mini_app_link", "series_link", "use_steps", "cat_link", "create_time",
                    "update_time", "ec_image_name", "ec_image_link", "ec_use_steps", "ec_link", "ec_activity"]
    # 　可以搜索的字段
    search_fields = ['pid', 'cat_lv1', 'cat_lv2', 'cat_lv3', 'series', 'product', 'intro', 'capacity', "price", "color",
                     'color_series', 'is_best_color', "ec_activity", "efficacy", "skin_type", "complexion", "image",
                     "link", "mini_app_link", "series_link", "use_steps", "cat_link", "create_time", "update_time",
                     "ec_image_name", "ec_image_link", "ec_use_steps", "ec_link", "ec_activity"]
    # 　可以过滤的字段
    list_filter = ['pid', 'cat_lv1', 'cat_lv2', 'cat_lv3', 'series', 'product', 'intro', 'capacity', "price", "color",
                   'color_series', 'is_best_color', "ec_activity", "efficacy", "skin_type", "complexion", "image",
                   "link", "mini_app_link", "series_link", "use_steps", "cat_link", "create_time", "update_time",
                   "ec_image_name", "ec_image_link", "ec_use_steps", "ec_link", "ec_activity"]
    # 可以编辑的字段
    list_editable = ['pid', 'cat_lv1', 'cat_lv2', 'cat_lv3', 'series', 'product', 'intro', 'capacity', "price", "color",
                     'color_series', 'is_best_color', "ec_activity", "efficacy", "skin_type", "complexion", "image",
                     "link", "mini_app_link", "series_link", "use_steps", "cat_link", "create_time", "update_time",
                     "ec_image_name", "ec_image_link", "ec_use_steps", "ec_link", "ec_activity"]
    # 每页显示的条数
    list_per_page = 100


# 活动管理类
class ActivityAdmin(object):
    list_display = ['id', 'title', 'pic_src', 'content', 'create_time', 'remark1', "remark2", "remark3"]
    search_fields = ['title', 'pic_src', 'content', 'create_time', 'remark1', "remark2", "remark3"]
    list_filter = ['title', 'pic_src', 'content', 'create_time', 'remark1', "remark2", "remark3"]
    list_editable = ['title', 'pic_src', 'content', 'create_time', 'remark1', "remark2", "remark3"]  # 可以编辑的字段
    list_per_page = 100


# 管理类注册
xadmin.site.register(Log, LogAdmin)
# xadmin.site.register(WxLog,WxLogAdmin)
xadmin.site.register(QaLogEc, QaLogEcAdmin)
xadmin.site.register(Product, ProductAdmin)
xadmin.site.register(Activity, ActivityAdmin)
