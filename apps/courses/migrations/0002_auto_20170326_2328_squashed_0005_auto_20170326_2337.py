# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 21:38
from __future__ import unicode_literals

import apps.utils.position_field
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('courses', '0002_auto_20170326_2328'), ('courses', '0003_auto_20170326_2336'), ('courses', '0004_auto_20170326_2337'), ('courses', '0005_auto_20170326_2337')]

    dependencies = [
        ('courses', '0001_squashed_0009_course_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['order', 'title']},
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(choices=[('main', 'main'), ('secondary', 'secondary')], default='main', max_length=9),
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['category', 'order', 'title']},
        ),
        migrations.AlterField(
            model_name='course',
            name='order',
            field=apps.utils.position_field.PositionField(default=1),
        ),
        migrations.AlterField(
            model_name='course',
            name='order',
            field=apps.utils.position_field.PositionField(default=2),
        ),
        migrations.AlterField(
            model_name='course',
            name='order',
            field=apps.utils.position_field.PositionField(default=-1),
        ),
    ]
