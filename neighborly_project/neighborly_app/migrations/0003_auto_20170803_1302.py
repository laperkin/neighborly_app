# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-03 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborly_app', '0002_auto_20170803_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]
