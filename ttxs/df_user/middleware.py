# coding=utf-8

from django.http import HttpRequest


# 定义中间件类，用于记录用户登录前输入的无效url， 用户登陆后直接转入该url

class UrlRedirectMiddleware:
    # 匹配完成之后才会执行该函数
    def process_view(self, request, view_func, view_args, view_kwargs):
        path = request.get_full_path()
        path1 = request.path
        if path1 not in [
            "/user/login/",
            "/user/login_handle/",
            "/user/register/",
            "/user/register_handle/",
            "/user/uname_valid/",
        ]:
            request.session["path"] = path


