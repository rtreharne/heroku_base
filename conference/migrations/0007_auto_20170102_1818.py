# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-02 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0006_auto_20170102_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]