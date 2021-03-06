# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-14 03:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_line_line_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Category'),
        ),
        migrations.AlterField(
            model_name='line',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Tag'),
        ),
    ]
