from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from users.models import *
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
    cate_id = get(request, 'id')
    try:
        cate_obj = Category.objects.get(id=cate_id)
    except Category.DoesNotExist:
        cate_obj = Category.objects.all().first()

    # 类别商品
    goods_list = Goods.objects.goods_by_cate(cate_id)

    return render(request, 'goods/goods_list.html', locals())


# 商品详情
def detail(request):
    goods_id = get(request, 'id')

    # 人气商品
    goods = Goods.objects.goods_by_id(goods_id)
    response = render(request, 'goods/goods_detail.html', locals())
    set_cookie(response, 'user', 'panjuanjuan')
    return response


# 投诉意见
def contact_message(request):
    ret = 0
    if check_contact_pramas(request):
        # 写入数据库
        save_contact_message(request)
        ret = 1

    return JsonResponse({"ret": ret})


def check_contact_pramas(request):
    c_name = post(request, 'c_name')
    if not c_name:
        return False

    c_email = post(request, 'c_tel')
    if 11 != len(c_email):
        return False

    c_message = post(request, 'c_message')
    if not c_message:
        return False

    return True


def save_contact_message(request):
    con = Contact()
    con.c_uname = post(request, 'c_name')
    con.c_tel = post(request, 'c_tel')
    con.c_message = post(request, 'c_message')
    con.save()


