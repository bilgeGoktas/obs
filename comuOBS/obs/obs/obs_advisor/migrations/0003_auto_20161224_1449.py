# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-24 14:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obs_advisor', '0002_auto_20161224_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advisor',
            old_name='years',
            new_name='year',
        ),
    ]