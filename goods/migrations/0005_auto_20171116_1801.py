# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20171116_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='act_image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='anno_image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
