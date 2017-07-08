from django.conf.urls import url

import views

urlpatterns = [
    # url(r'$', views.index),
    url(r'^$', views.index),
    url(r'^typelist(\d+)_(\d+)_(\d)/$', views.typelist),
    url(r'^(\d+)/$', views.detail),
]