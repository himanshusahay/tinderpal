# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-14 03:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170113_2244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='line',
            options={'ordering': ('line_text',), 'verbose_name_plural': 'categories'},
        ),
    ]