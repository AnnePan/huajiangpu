# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20171116_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='anno_title',
            field=models.CharField(max_length=15),
        ),
    ]
