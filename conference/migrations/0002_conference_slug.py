# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-02 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='slug',
            field=models.SlugField(default='slug'),
            preserve_default=False,
        ),
    ]
