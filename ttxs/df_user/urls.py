from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_handle/$', views.register_handle),
    url(r'^login/$', views.login),
    url(r'^uname_valid/$', views.uname_valid),
    url(r'^login_handle/$', views.login_handle),
    url(r'^center/$', views.center),
    url(r'^site/$', views.site),
    url(r'^order/$', views.order),

]