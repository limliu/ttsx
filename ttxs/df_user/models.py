# coding=utf-8

from django.db import models

# Create your models here.


class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    umail = models.CharField(max_length=30, blank=False)

    def __unicode__(self):
        return self.uname


class ReceInfo(models.Model):
    raddr = models.CharField(max_length=100, blank=False, null=False)
    rphone = models.CharField(max_length=11, blank=False, null=False)
    rcode = models.CharField(max_length=6, blank=False)
    rshou = models.CharField(max_length=20, blank=False, null=False)
    # 通过ruser属性把recv对象与user对象关联起来，
    ruser = models.ForeignKey("userinfo")

    def __unicode__(self):
        return self.rshou