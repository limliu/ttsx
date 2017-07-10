# coding=utf-8

from django.shortcuts import render, redirect

from django.http import JsonResponse, HttpResponse

# Create your views here.


from models import UserInfo, ReceInfo

from goods.models import GoodsInfo
from hashlib import sha1

import datetime

from decorators import is_login


def register(request):
    context = {"top": "0", "title": "注册"}
    return render(request, 'df_user/register.html', context)


# 判断用户名是否已存在
def uname_valid(request):
    uname = request.GET.get("uname")

    num = UserInfo.objects.filter(uname=uname).count()
    if num == 0:
        msg = ""
        return JsonResponse({"msg": msg})
    else:
        msg = "用户名已存在"
        return JsonResponse({"msg": msg})


# 注册处理， 把用户信息写入数据库
def register_handle(request):
    user = UserInfo()
    post = request.POST
    uname = post.get("uname")
    upwd = post.get("pwd")
    umail = post.get("email")

    # 对密码加密
    s1 = sha1()
    s1.update(upwd)
    pwd_sha1 = s1.hexdigest()

    # 把用户数据保存到数据库
    user.uname = uname
    user.umail = umail
    user.upwd = pwd_sha1
    user.save()

    return redirect('/user/login/')


# 登陆网页
def login(request):
    name = request.COOKIES.get("name", "")

    return render(request, 'df_user/login.html', {"name": name, "top": "0", "title": "登录"})


# 登录信息验证
def login_handle(request):
    # 获取用户输入信息
    name = request.POST.get('name')
    print(name, "------")
    pwd = request.POST.get('pwd')
    print(pwd, "=====")
    value = request.POST.get("remember")


    user = UserInfo.objects.filter(uname=name)

    s1 = sha1()
    s1.update(pwd)
    pwd_sha1 = s1.hexdigest()

    context = {"name": name, "pwd": pwd, "top": "0", "title": "登录"}

    # 用户存在
    if user:
        upwd = user[0].upwd

        # 用户名和密码匹配
        if upwd == pwd_sha1:
            request.session["uid"] = user[0].id
            request.session["uname"] = user[0].uname
            request.session['is_login'] = 1
            path = request.session.get("path", "/user/center/")
            response = redirect(path)

            # 记住用户名
            if value == "1":
                # 获取当前时间，加14天，得到cookie过期时间
                now = datetime.datetime.now()
                save_day = datetime.timedelta(days=14)
                final_time = now + save_day
                # 设置cookie过期时间
                response.set_cookie("name", name, expires=final_time)


            else:
                # 忘记用户名
                # 设置cookie过期时间

                response.set_cookie("name", "", max_age=-1)
            return response

        else:
            context["pwd_error"] = "用户密码错误"
            return render(request, 'df_user/login.html', context)

    # 用户不存在
    else:
        context['user_error'] = "用户不存在"
        return render(request, 'df_user/login.html', context)

@is_login
def center(request):
    uid = request.session.get("uid")
    user = UserInfo.objects.filter(id=uid)[0]

    # 获取存在cookie里的最近浏览商品信息,若没有则赋值为"",把最后一个去掉
    gid_list = request.COOKIES.get("gids", "").split(",")
    if gid_list[-1] == "":
        gid_list.pop()

    # 根据gid查询商品， 并把商品对象加入商品列表。
    goods_list = []
    for gid in gid_list:
        goods_list.append(GoodsInfo.objects.get(id=gid))
    return render(request, 'df_user/center.html',\
           {"user": user, "title": "个人中心", "goods_list": goods_list, "show_cart": "1"})


@is_login
def site(request):
    uid = request.session.get("uid")
    user = UserInfo.objects.filter(id=uid)[0]

    context = {}

    # 如果请求方法是post，说明是form表单提交
    if request.method == "POST":

        post = request.POST
        ushou = post.get("shou")
        uaddr = post.get("uaddr")
        ucode = post.get("ucode")
        uphone = post.get("uphone")



        # 将用户收货信息写入数据库
        recv = ReceInfo()
        recv.rshou = ushou
        recv.raddr = uaddr
        recv.rcode = ucode
        recv.rphone = uphone
        recv.ruser = user
        recv.save()


        # context = {"uaddr": uaddr, "ushou": ushou, "uphone": uphone, "title": "详情"}


        # 获取该用户的所有收货信息，并写入页面

    reces = user.receinfo_set.all()
    rece_lsit = []
    for rece in reces:
        rece_lsit.append(rece)

    context["recv_list"] = rece_lsit
    context["user"] = user
    return render(request, 'df_user/site.html', context)

@is_login
def order(request):
    uid = request.session.get("uid")
    user = UserInfo.objects.filter(id=uid)[0]

    return render(request, 'df_user/order.html', {"user": user, "title": "订单"})


def logoff(request):
    # 退出把session都清空
    request.session["uid"] = ""
    request.session["uname"] = ""
    request.session['is_login'] = ""
    return redirect("/user/login/")
