from django.shortcuts import render
import random
from .models import *
from utils.wrapper import *


def index(request):
    # 公告
    anno = Announcement.objects.all().order_by('-id')[:1].first()

    # 活动
    acti = Activity.objects.filter(act_activiting=True).order_by('-create_time')[:1].first()

    # 类别
    cate_list = Category.objects.all()

    # 人气商品
    # hot_list = Goods.objects.goods_by_hot()

    return render(request, 'goods/goods_index.html', locals())


def g_list(request):
    # cate_id = get(request, 'id')

    # 类别商品
    # cate_list = Goods.objects.goods_by_cate(cate_id)

    return render(request, 'goods/goods_list.html', locals())


def detail(request):
    # goods_id = get(request, 'id')
    # 人气商品
    # goods = Goods.objects.goods_by_id(goods_id)

    return render(request, 'goods/goods_detail.html', locals())






