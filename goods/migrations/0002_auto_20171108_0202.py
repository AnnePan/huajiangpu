# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertising',
            name='adv_image1',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='advertising',
            name='adv_image2',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='advertising',
            name='adv_image3',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='goods',
            name='g_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
