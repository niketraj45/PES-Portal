# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-16 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='club_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='club',
            name='contact_info',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='signup',
            name='sem',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
