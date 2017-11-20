from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import *


def index(request):
    return render(request, 'users/user_order.html', locals())


def register(request):
    return render(request, 'users/user_register.html', locals())


def login(request):
    return render(request, 'users/user_login.html', locals())


def address(request):
    return render(request, 'users/user_address.html', locals())


# 注册逻辑
def register_handle(request):

    if check_register_params(request):
        # 数据入库
        User.objects.user_register(request)
        return redirect(reverse('users:login'))
    else:
        return redirect(reverse('users:register'))


# 登录逻辑
def login_handle(request):
    if check_login_params(request):
        response = redirect(reverse('goods:index'))
        keep_user_online(request, response)
        return response
    else:
        return redirect(reverse('users:login'))


def check_register_params(request):
    u_name = post(request, 'u_name')
    if not 5 <= len(u_name) <= 20:
        return False

    u_phone = post(request, 'u_phone')
    if not 11 == len(u_phone):
        return False

    u_pass = post(request, 'u_pass')
    if not 8 <= len(u_pass) <= 20:
        return False

    u_repass = post(request, 'u_repass')
    if not u_pass == u_repass:
        return False

    user = User.objects.user_by_name(u_name)
    if user:
        return False

    return True


def check_login_params(request):
    u_name = post(request, 'u_name')
    if not 5 <= len(u_name) <= 20:
        return False

    u_pass = post(request, 'u_pass')
    if not 8 <= len(u_pass) <= 20:
        return False

    user = User.objects.user_by_name(u_name)
    if not user:
        return False

    if not user.u_pass == password_encryption(u_pass):
        return False

    return True


def keep_user_online(request, response):
    u_name = post(request, 'u_name')
    user = User.objects.user_by_name(u_name)
    set_cookie(response, str(user.id), 'u_id')

