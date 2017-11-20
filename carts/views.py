from django.shortcuts import render
from django.http import JsonResponse
from utils.wrapper import *
from .models import *


def index(request):
    return render(request, 'carts/cart_cart.html', locals())


# 添加商品到购物车
def add_goods(request):
    u_id = get_cookie(request, 'u_id')
    if not u_id:
        return JsonResponse({'ret': 0})

    goods_id = post(request, 'goods_id')
    goods_num = post(request, 'goods_num')

    c = Carts()
    c.u_id = u_id
    c.goods_id = goods_id
    c.goods_num = goods_num
    c.save()

