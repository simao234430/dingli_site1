# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-10 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_web', '0002_auto_20181110_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherinfo',
            name='range_weight',
            field=models.IntegerField(default=0),
        ),
    ]