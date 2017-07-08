# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gtitle', models.CharField(max_length=20)),
                ('gpic', models.ImageField(upload_to=b'goods/')),
                ('gprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('gclick', models.IntegerField()),
                ('gunit', models.CharField(max_length=10)),
                ('isDelete', models.BooleanField(default=False)),
                ('gsubtitle', models.CharField(max_length=100)),
                ('gleft', models.IntegerField()),
                ('gcontent', tinymce.models.HTMLField()),
            ],
            options={
                'db_table': 'df_goods_goodsinfo',
            },
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ttitle', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField()),
            ],
            options={
                'db_table': 'df_goods_typeinfo',
            },
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='goods.TypeInfo'),
        ),
    ]
