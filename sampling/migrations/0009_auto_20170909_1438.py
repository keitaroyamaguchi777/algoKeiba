# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-09-09 05:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sampling', '0008_auto_20170909_1401'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tyokuzen',
            new_name='Chokuzen',
        ),
        migrations.RenameField(
            model_name='chokuzen',
            old_name='kisyu_code',
            new_name='kishu_code',
        ),
        migrations.RenameField(
            model_name='kishu_sabun',
            old_name='kisyu_code',
            new_name='kishu_code',
        ),
        migrations.RenameField(
            model_name='kishu_sabun',
            old_name='kisyu_fukusyou',
            new_name='kishu_fukusyou',
        ),
        migrations.RenameField(
            model_name='kishu_sabun',
            old_name='kisyu_mei',
            new_name='kishu_mei',
        ),
    ]
