from django.db import models

# Create your models here.


class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uaddr = models.CharField(max_length=100)
    ushou = models.CharField(max_length=20, blank=False)
    uphone = models.CharField(max_length=11, blank=False)
    ucode = models.CharField(max_length=6, blank=False)
    umail = models.CharField(max_length=30, blank=False)
