# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-14 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validation', '0008_auto_20180614_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validresult',
            name='end_date',
            field=models.DateField(blank=True, default='2018-01-01'),
        ),
        migrations.AlterField(
            model_name='validresult',
            name='start_date',
            field=models.DateField(blank=True, default='2018-01-01'),
        ),
    ]