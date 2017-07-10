# coding=utf-8

from django.shortcuts import render

from django.http import JsonResponse

# Create your views here.

from models import *

from df_user.models import *

from goods.models import *


def cart_handle(request):

    # 获取商品详情页用户传过来的购物车信息
    request = request.GET
    uname = request.get("uname")
    gid = request.get("gid")
    num = int(request.get("num"))

    # 根据获取的信息找到用户对象和商品对象
    user = UserInfo.objects.filter(uname=uname)[0]
    goods = GoodsInfo.objects.filter(id=gid)[0]

    # 如果购物车数据库已有该商品，则只增加他的数量就行了
    if CartInfo.objects.filter(cart_goods=goods):
        cart1 = CartInfo.objects.get(cart_goods=goods)
        cart1.cart_num += num
        cart1.save()

    # 如果没有该商品则新建该商品
    else:
        # 保存数据到数据库
        cart = CartInfo()
        cart.cart_num = num
        cart.cart_goods = goods
        cart.cart_user = user
        cart.save()

    context = {"msg": "已添加到购物车"}
    return JsonResponse(context)


def cart(request):
    uname = request.session["uname"]
    user = UserInfo.objects.filter(uname=uname)[0]

    cart_list = user.cartinfo_set.all()
    context = {"top": "1", "show_cart": "1", "cart_list": cart_list}
    return render(request, "cart/cart.html", context)


def order(request):
    context = {"top": "1", "show_cart": "1"}
    return render(request, "cart/order.html", context)