# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20170324_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]