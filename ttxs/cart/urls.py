from django.conf.urls import url

import views

urlpatterns = [
    url(r'^cart_handle/$', views.cart_handle),
    url(r'^cart/$', views.cart),
    url(r'^order/$', views.order),
]