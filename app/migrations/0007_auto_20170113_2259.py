# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-14 03:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170113_2258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('category_name',), 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='line',
            options={'ordering': ('line_text',)},
        ),
    ]