# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-02 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0004_deadline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Symposium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('pic', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('description', models.TextField(max_length=1000)),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conference.Conference')),
            ],
        ),
    ]
