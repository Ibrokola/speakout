# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-15 10:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('convo', '0002_auto_20170415_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='convo',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='convo',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='convo',
            name='content',
            field=models.CharField(max_length=250),
        ),
    ]
