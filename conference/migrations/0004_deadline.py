# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-02 06:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0003_auto_20170102_0545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deadline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='e.g. Early Bird Registration', max_length=128)),
                ('date', models.DateTimeField()),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conference.Conference')),
            ],
        ),
    ]
