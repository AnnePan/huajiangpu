# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('u_id', models.IntegerField()),
                ('goods_id', models.IntegerField()),
                ('goods_num', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
