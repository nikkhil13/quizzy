# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-22 14:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160315_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phpquestion',
            name='all_id',
        ),
        migrations.RemoveField(
            model_name='question',
            name='all_id',
        ),
    ]