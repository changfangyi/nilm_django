# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-14 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '0009_auto_20180614_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validresult',
            name='end_date',
            field=models.CharField(max_length=50, verbose_name='End'),
        ),
        migrations.AlterField(
            model_name='validresult',
            name='start_date',
            field=models.CharField(max_length=50, verbose_name='Start'),
        ),
    ]
