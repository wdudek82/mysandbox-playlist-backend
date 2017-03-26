# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 21:21
from __future__ import unicode_literals

import apps.utils.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('courses', '0001_initial'), ('courses', '0002_lecture'), ('courses', '0003_auto_20170323_2344'), ('courses', '0004_auto_20170324_0011'), ('courses', '0005_auto_20170324_2249'), ('courses', '0006_lecture_order'), ('courses', '0007_auto_20170326_1853'), ('courses', '0008_auto_20170326_1907'), ('courses', '0009_course_order')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0002_auto_20170321_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, help_text='Some help text for slug field')),
                ('description', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Course')),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='videos.Video')),
                ('order', models.IntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='lecture',
            unique_together=set([('slug', 'course')]),
        ),
        migrations.AlterModelOptions(
            name='lecture',
            options={'ordering': ['order', 'title']},
        ),
        migrations.AlterField(
            model_name='lecture',
            name='order',
            field=apps.utils.fields.PositionField(default=-1),
        ),
        migrations.AddField(
            model_name='course',
            name='order',
            field=apps.utils.fields.PositionField(default=-1),
        ),
    ]
