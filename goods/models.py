from db.AbstractModel import BaseModel
from django.db import models


class Category(BaseModel):
    cate_name = models.CharField(max_length=20)
    cate_desc = models.CharField(max_length=500)

    def __str__(self):
        return self.cate_name


class GoodsManager(models.Manager):
    def goods_by_hot(self):
        return self.all().order_by('g_look')[:10]

    def goods_by_cate(self, cate_id):
        return self.filter(g_cate_id=cate_id)

    def goods_by_id(self, goods_id):
        try:
            return self.get(pk=goods_id)
        except Goods.DoesNotExist:
            return None
        except Exception as e:
            print(e)
            return None


class Goods(BaseModel):
    # 名字，
    g_name = models.CharField(max_length=30)
    # 类别，
    g_cate = models.ForeignKey(Category)
    # 主图，
    g_image = models.ImageField()
    # 描述，
    g_desc = models.CharField(max_length=100)
    # 单位，
    g_unit = models.CharField(max_length=10)
    # 价格，
    g_price = models.DecimalField(max_digits=10, decimal_places=2)
    # 人气，
    g_look = models.IntegerField(default=0)

    objects = GoodsManager()

    def __str__(self):
        return self.g_name


class Activity(BaseModel):
    # 是否活动中
    act_activiting = models.BooleanField(default=False)
    # 标题
    act_title = models.CharField(max_length=50)
    # 副标题
    act_subtitle = models.CharField(max_length=200)
    # 详情
    act_detail = models.CharField(max_length=500)
    # 图（1413*900）
    act_image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.act_title


class Announcement(BaseModel):
    # 公告标题
    anno_title = models.CharField(max_length=15)
    # 公告详情
    anno_detail = models.CharField(max_length=200)
    # 主图，
    anno_image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.anno_title


