from django.conf.urls import url

import views

from search_view import *

urlpatterns = [
    # url(r'$', views.index),
    url(r'^$', views.index),
    url(r'^typelist(\d+)_(\d+)_(\d)/$', views.typelist),
    url(r'^(\d+)/$', views.detail),
    url(r'^query/', views.query),
    url(r'^search/?$', MySearchView.as_view()),
]