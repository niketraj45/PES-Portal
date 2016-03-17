# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-04 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='event',
            name='id',
            field=models.AutoField(auto_created=True, default=-1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='club_id',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('club_id', 'event_id')]),
        ),
    ]