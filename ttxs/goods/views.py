# coding=utf-8
from django.shortcuts import render

# Create your views here.

from models import *

from django.core.paginator import Paginator


def index(request):
    type_list = TypeInfo.objects.all()
    list = []
    for type1 in type_list:
        new_list = type1.goodsinfo_set.order_by("-id")[0:4]
        click_list = type1.goodsinfo_set.order_by("-gclick")[0:3]
        list.append({"type1": type1, "new_list": new_list, "click_list": click_list})
    content = {"list": list, "title": "首页", "show_cart": "1"}
    print(list[0])
    return render(request, "goods/index.html", content)


def typelist(request, pid, pindex, f):
    # 根据用户点击获取商品类id，查询该商品类
    gtype = TypeInfo.objects.get(id=int(pid))
    new_list = GoodsInfo.objects.order_by("-gclick")[0:2]

    # 获取所有商品类
    type_list = TypeInfo.objects.all()



    # 如果f为0说明为默认排序， 获取以id排序的商品列表
    if f == "0":
        goods_list = gtype.goodsinfo_set.all().order_by("-id")

    # 如果f为1说明为价格排序， 获取以价格排序的商品列表
    if f == "1":
        goods_list = gtype.goodsinfo_set.all().order_by("-gprice")

    # 如果f为1说明为点击排序， 获取以点击排序的商品列表
    if f == "2":
        goods_list = gtype.goodsinfo_set.all().order_by("-gclick")

    paginator = Paginator(goods_list, 15)
    page = paginator.page(pindex)
    context = {"title": "商品分类", "show_cart": "1", "page": page, "new_list": new_list,\
               "gtype": gtype, "type_list": type_list, "show_cart": "1"}

    return render(request, 'goods/list.html', context)


def detail(request, gid):
    # 根据该商品的id，获取该商品对象
    goods = GoodsInfo.objects.get(id=int(gid))

    # 通过商品对象获取该商品类， 通过该商品类，获取所有商品
    new_list = goods.gtype.goodsinfo_set.order_by("-id")[0:2]

    # 获取所有商品类
    type_list = TypeInfo.objects.all()

    context = {"goods": goods, "new_list": new_list, "show_cart": "1", "type_list": type_list}
    return render(request, "goods/detail.html", context)







