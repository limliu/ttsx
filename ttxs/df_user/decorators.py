# coding=utf-8

from django.shortcuts import redirect

# 定义一个装饰器， 用于判断用户是否登录，如果未登录直接访问中心页，则转向登录页面
def is_login(func):
    def innerfunc(request, *args, **kwargs):
        if request.session.get("is_login", ""):
            return func(request, *args, **kwargs)
        else:
            return redirect("/user/login/")
    return innerfunc