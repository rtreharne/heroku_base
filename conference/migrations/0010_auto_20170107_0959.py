# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-07 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0009_auto_20170107_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialtype',
            name='fa',
            field=models.CharField(max_length=25),
        ),
    ]
