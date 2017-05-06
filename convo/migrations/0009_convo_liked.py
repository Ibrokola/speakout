# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-05 09:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('convo', '0008_convo_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='convo',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
