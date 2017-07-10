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


def typelist(request, pid, pindex, orderby):
    # 根据用户点击获取商品类id，查询该商品类
    gtype = TypeInfo.objects.get(id=int(pid))
    new_list = GoodsInfo.objects.order_by("-gclick")[0:2]

    # 获取所有商品类
    type_list = TypeInfo.objects.all()

    # 如果f为0说明为默认排序， 获取以id排序的商品列表
    if orderby == "0":
        goods_list = gtype.goodsinfo_set.all().order_by("-id")

    # 定义价格的排序顺序desc，根据价格的获取顺序获取商品排序顺序， 然后改变desc值
    desc = "1"
    # 如果f为1说明为价格排序， 获取以价格排序的商品列表
    if orderby == "1":
        desc = request.GET.get("desc")
        if desc == "1":
            goods_list = gtype.goodsinfo_set.all().order_by("-gprice")
            desc = 0
        else:
            goods_list = gtype.goodsinfo_set.all().order_by("gprice")
            desc = 1
        print desc

    # 如果f为1说明为点击排序， 获取以点击排序的商品列表
    if orderby == "2":
        goods_list = gtype.goodsinfo_set.all().order_by("-gclick")

    paginator = Paginator(goods_list, 5)
    page = paginator.page(pindex)
    context = {"title": "商品分类", "show_cart": "1", "page": page, "new_list": new_list,\
               "gtype": gtype, "type_list": type_list, "show_cart": "1", "orderby": orderby, "desc": desc}
    return render(request, 'goods/list.html', context)


def detail(request, gid):
    # 根据该商品的id，获取该商品对象
    goods = GoodsInfo.objects.get(id=int(gid))

    # 进入商品详情页， 商品点击量+1.
    goods.gclick += 1
    goods.save()

    # 通过商品对象获取该商品类， 通过该商品类，获取所有商品，取两个最新商品.
    new_list = goods.gtype.goodsinfo_set.order_by("-id")[0:2]
    gtype = goods.gtype

    # 获取所有商品类
    type_list = TypeInfo.objects.all()

    # 构造上下文
    context = {"goods": goods, "new_list": new_list, "show_cart": "1",\
               "type_list": type_list, 'title': '详情页', "gtype": gtype}
    response = render(request, "goods/detail.html", context)

    # 保存最近五次浏览的商品，
    # 获取cookie值，如果没有则设置为"", 并把他换成列表，以便待会添加数据
    gids = request.COOKIES.get("gids", "").split(",")

    # 如果cookie里已有该gid，则把之前的值删掉， 并把该值加到最前面
    if gid in gids:
        gids.remove(gid)
    gids.insert(0, gid)

    # 如果cookie中数据大于5个，则把最后一个删掉。
    if len(gids) > 5:
        gids.pop()

    # 使用response对象设置 cookies，
    response.set_cookie("gids", ",".join(gids), max_age=60*60*24*7)
    return response



def query(request):
    return render(request, 'goods/query.html')


