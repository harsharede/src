# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-24 10:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import dreambuy.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dreambuy', '0003_auto_20171005_0240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_id', models.CharField(default=dreambuy.models.prdtcode, max_length=50)),
                ('Product_name', models.CharField(max_length=250)),
                ('userid', models.IntegerField(default=1)),
                ('bid_time', models.CharField(max_length=250)),
                ('bid_count', models.IntegerField()),
                ('pymnt_status', models.CharField(default=1, max_length=10)),
                ('cur_prdt_bid_price', models.IntegerField(default=500)),
                ('purpose', models.CharField(default=1, max_length=10)),
                ('payment_request_id', models.CharField(default=1, max_length=10)),
                ('bid_username', models.CharField(default=1, max_length=10)),
                ('bid_id', models.CharField(default=1, max_length=10)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userbids',
            name='bid_count',
        ),
        migrations.AlterField(
            model_name='userbids',
            name='Product_id',
            field=models.CharField(default=dreambuy.models.prdtcode, max_length=50),
        ),
    ]
