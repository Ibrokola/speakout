# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-05 00:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('convo', '0007_auto_20170421_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='convo',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='convo.Convo'),
        ),
    ]
