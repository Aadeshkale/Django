# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-11 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relapp', '0007_auto_20180911_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='cid',
            field=models.OneToOneField(null=True, on_delete=models.SET(11), to='relapp.Student'),
        ),
    ]
