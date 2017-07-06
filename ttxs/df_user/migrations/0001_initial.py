# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReceInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('raddr', models.CharField(max_length=100)),
                ('rphone', models.CharField(max_length=11)),
                ('rcode', models.CharField(max_length=6)),
                ('rshou', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('umail', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='receinfo',
            name='ruser',
            field=models.ForeignKey(to='df_user.UserInfo'),
        ),
    ]
