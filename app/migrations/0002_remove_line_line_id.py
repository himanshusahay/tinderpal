# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-14 03:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='line',
            name='line_id',
        ),
    ]
