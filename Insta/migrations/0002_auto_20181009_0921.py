# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-09 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=80, null=True),
        ),
    ]