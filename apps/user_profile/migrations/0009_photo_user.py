# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-31 07:31
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0008_auto_20180130_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE,
                                       related_name='user_profile_photo', to='user_profile.User_details'),
            preserve_default=False,
        ),
    ]
