from datetime import datetime

from django.db import models



# Create your models here.
# 日志模型
class Log(models.Model):
    user_id = models.CharField(max_length=45, verbose_name="用户id", blank=True)
    conversion_id = models.TextField(verbose_name="对话id", blank=True)
    question = models.TextField(verbose_name="问题", blank=True)
    answer = models.TextField(verbose_name="答案", blank=True)
    create_time = models.DateTimeField(verbose_name="创建日期", blank=True)
    intent = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'qa_log'
        verbose_name = '日志信息'
        verbose_name_plural = verbose_name


"""
#微信日志模型
class WxLog(models.Model):
    openid = models.CharField(max_length=11)
    question = models.TextField()
    answer = models.TextField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'wx_qa_log'
        verbose_name = '微信日志信息'
        verbose_name_plural = verbose_name

"""


# EC日志模型
class QaLogEc(models.Model):
    user_id = models.CharField(max_length=255, verbose_name="用户id", blank=True)
    session_id = models.TextField(verbose_name="session_id", blank=True)
    source_type = models.CharField(max_length=16, verbose_name="来源类型", blank=True)
    question = models.TextField(verbose_name="问题", blank=True)
    answer = models.TextField(verbose_name="答案", blank=True)
    create_time = models.DateTimeField(verbose_name="创建时间", blank=True)
    intent = models.CharField(max_length=255, verbose_name="intent", blank=True)

    class Meta:
        db_table = 'qa_log_ec'
        verbose_name = '日志EC'
        verbose_name_plural = verbose_name


# 产品模型
class Product(models.Model):
    pid = models.CharField(max_length=45, blank=True)
    cat_lv1 = models.CharField(max_length=45, blank=True)
    cat_lv2 = models.CharField(max_length=45, blank=True)
    cat_lv3 = models.CharField(max_length=45, blank=True)
    series = models.CharField(max_length=45, verbose_name="系列", blank=True)
    product = models.CharField(max_length=45, verbose_name="产品名称", blank=False)
    product_en = models.CharField(max_length=512, verbose_name="产品英文名", blank=True)
    intro = models.CharField(max_length=512, verbose_name="产品介绍", blank=True)
    capacity = models.CharField(max_length=512, verbose_name="容量", blank=True)
    price = models.CharField(max_length=45, verbose_name="价格", blank=True)
    color = models.CharField(max_length=45, verbose_name="颜色", blank=True)
    color_series = models.CharField(max_length=45, verbose_name="颜色系列", blank=True)
    is_best_color = models.IntegerField(blank=True)
    color_image = models.CharField(max_length=45, blank=True)
    color_series_image = models.CharField(max_length=45, blank=True)
    is_new = models.IntegerField(blank=True)
    is_best = models.IntegerField(blank=True)
    efficacy = models.CharField(max_length=512, blank=True)
    efficacy_words = models.CharField(max_length=512, blank=True)
    skin_type = models.CharField(max_length=512, blank=True)
    complexion = models.CharField(max_length=512, blank=True)
    image = models.ImageField(upload_to="image", blank=True, verbose_name="产品图片")
    link = models.CharField(max_length=512, blank=True)
    mini_app_link = models.CharField(max_length=512, blank=True)
    series_link = models.CharField(max_length=512, blank=True)
    use_steps = models.CharField(max_length=512, blank=True)
    cat_link = models.CharField(max_length=512, blank=True)
    create_time = models.DateTimeField(verbose_name="创建日期", blank=True)
    update_time = models.DateTimeField(verbose_name="更新日期", blank=True)
    ec_image_name = models.CharField(max_length=255, blank=True)
    ec_image_link = models.CharField(max_length=255, blank=True)
    ec_use_steps = models.CharField(max_length=512, blank=True)
    ec_link = models.CharField(max_length=512, blank=True)
    ec_activity = models.CharField(max_length=16, blank=True)

    class Meta:
        db_table = 'product'
        verbose_name = '产品信息'
        verbose_name_plural = verbose_name

    # 活动模型


class Activity(models.Model):
    Product_logic_id = models.CharField(max_length=45, blank=True, verbose_name="产品日志id")
    title = models.CharField(max_length=45, blank=True, verbose_name="活动标题")
    pic_src = models.CharField(max_length=45, blank=True, verbose_name="活动地址")
    content = models.CharField(max_length=45, blank=True, verbose_name="活动内容")
    create_time = models.CharField(max_length=45, blank=True, verbose_name="创建日期")
    remark1 = models.CharField(max_length=45, blank=True, verbose_name="")
    remark2 = models.CharField(max_length=45, blank=True, verbose_name="")
    remark3 = models.CharField(max_length=45, blank=True, verbose_name="")

    class Meta:
        db_table = 'activity'
        verbose_name = '活动'
        verbose_name_plural = verbose_name
