# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curr_user',
            fields=[
                ('User_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
    ]
