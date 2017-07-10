# coding=utf-8
from django.db import models

# Create your models here.

from df_user.models import *

from goods.models import GoodsInfo


class CartInfo(models.Model):
    cart_goods = models.ForeignKey(GoodsInfo)
    cart_num = models.IntegerField()
    cart_user = models.ForeignKey(UserInfo)

    def __unicode__(self):
        return self.cart_goods.gtitle

    def show_title(self):
        return self.cart_goods.gtitle