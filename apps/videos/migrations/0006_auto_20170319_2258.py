# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_auto_20170319_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]