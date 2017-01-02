# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-02 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('start', models.DateTimeField()),
                ('finish', models.DateTimeField()),
            ],
        ),
    ]
