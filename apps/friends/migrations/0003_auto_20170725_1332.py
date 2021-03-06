# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 20:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('friends', '0002_auto_20170725_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='users',
            new_name='friends',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='name',
        ),
        migrations.AddField(
            model_name='friend',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.User'),
        ),
    ]
