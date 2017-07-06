# coding=utf-8

from django.shortcuts import render, redirect

from django.http import JsonResponse, HttpResponse

# Create your views here.


from models import UserInfo

from hashlib import sha1


def register(request):
    return render(request, 'df_user/register.html')


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
    return render(request, 'df_user/login.html', {"name": name})


# 登录信息验证
def login_handle(request):
    # 获取用户输入信息
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')

    value = request.POST.get("remember")
    print(value, "-----")
    user = UserInfo.objects.filter(uname=name)

    s1 = sha1()
    s1.update(pwd)
    pwd_sha1 = s1.hexdigest()

    context = {"name": name, "pwd": pwd}

    # 用户存在
    if user:
        upwd = user[0].upwd
        # 用户名和密码匹配
        if upwd == pwd_sha1:
            request.session["uid"] = user[0].id
            if value == "1":
                response = redirect("/user/center/")
                response.set_cookie("name", name)
                return response


        else:
            context["pwd_error"] = "用户密码错误"
            return render(request, 'df_user/login.html', context)

    # 用户不存在
    else:
        context['user_error'] = "用户不存在"
        return render(request, 'df_user/login.html', context)


def center(request):
    uid = request.session.get("uid")

    user = UserInfo.objects.filter(id=uid)[0]
    return render(request, 'df_user/center.html', {"user": user})


def site(request):

    context = {}
    # 如果请求方法是post，说明是form表单提交
    if request.method == "POST":
        post = request.POST
        ushou = post.get("shou")
        uaddr = post.get("uaddr")
        ucode = post.get("ucode")
        uphone = post.get("uphone")

        # 讲用户收货信息写入数据库
        uid = request.session.get("uid")
        user = UserInfo.objects.filter(id=uid)[0]
        user.ushou = ushou
        user.uaddr = uaddr
        user.ucode = ucode
        user.uphone = uphone
        user.save()
        context = {"uaddr": uaddr, "ushou": ushou, "uphone": uphone}

    return render(request, 'df_user/site.html', context)


def order(request):
    uid = request.session.get("uid")
    user = UserInfo.objects.filter(id=uid)[0]

    return render(request, 'df_user/order.html', {"user": user})


