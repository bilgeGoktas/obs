# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-26 17:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obs_course', '0004_auto_20161226_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='departmentd',
            new_name='department',
        ),
    ]
