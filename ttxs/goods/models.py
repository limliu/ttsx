from django.db import models

# Create your models here.

from tinymce.models import HTMLField


class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField()

    class Meta:
        db_table = "df_goods_typeinfo"


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to="goods/")
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    gclick = models.IntegerField()
    gunit = models.CharField(max_length=10)
    isDelete = models.BooleanField(default=False)
    gsubtitle = models.CharField(max_length=100)
    gleft = models.IntegerField()
    gcontent = HTMLField()
    gtype = models.ForeignKey("TypeInfo")

    class Meta:
        db_table = "df_goods_goodsinfo"


