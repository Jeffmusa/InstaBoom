# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-08 13:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0006_auto_20181008_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='usr',
            new_name='user',
        ),
    ]
