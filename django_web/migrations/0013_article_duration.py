# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-11 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_web', '0012_auto_20181111_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='duration',
            field=models.CharField(default='', max_length=64),
        ),
    ]