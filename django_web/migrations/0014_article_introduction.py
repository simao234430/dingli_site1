# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-12 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_web', '0013_article_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='introduction',
            field=models.CharField(default='', max_length=128),
        ),
    ]
