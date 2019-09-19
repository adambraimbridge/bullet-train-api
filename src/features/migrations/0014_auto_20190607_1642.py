# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-07 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0013_auto_20190607_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuresegment',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='featuresegment',
            name='feature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='features.Feature'),
        ),
    ]
