# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-17 02:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0009_lab'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
