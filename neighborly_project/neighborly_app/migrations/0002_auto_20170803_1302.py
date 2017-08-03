# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-03 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborly_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.IntegerField(max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]