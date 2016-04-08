# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-03 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0004_auto_20160403_2036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='dob',
            new_name='D_O_B',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='phone',
        ),
        migrations.AddField(
            model_name='signup',
            name='branch',
            field=models.CharField(choices=[('CSE', 'Computer Engineering'), ('ISE', 'Information Engineering'), ('ME', 'Mechanical Engineering'), ('ECE', 'Electronics Engineering'), ('EEE', 'Electrical Engineering'), ('TE', 'Telecom Engineering'), ('BT', 'Bio-Technology'), ('CV', 'Civil Engineering')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='phone_no',
            field=models.IntegerField(default=9999999999L),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='signup',
            name='club_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='signup',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='signup',
            name='sem',
            field=models.CharField(choices=[('1', 'I'), ('2', 'II'), ('3', 'III'), ('4', 'IV'), ('5', 'V'), ('6', 'VI'), ('7', 'VII'), ('8', 'VIII')], max_length=1),
        ),
    ]