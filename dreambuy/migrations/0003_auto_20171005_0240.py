# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-04 21:10
from __future__ import unicode_literals

from django.db import migrations, models
import dreambuy.models


class Migration(migrations.Migration):

    dependencies = [
        ('dreambuy', '0002_auto_20170927_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbids',
            name='bid_username',
            field=models.CharField(default=1, max_length=10),
        ),
        migrations.AlterField(
            model_name='userbids',
            name='Product_id',
            field=models.CharField(default=dreambuy.models.prdtcode, max_length=50, unique=True),
        ),
    ]
