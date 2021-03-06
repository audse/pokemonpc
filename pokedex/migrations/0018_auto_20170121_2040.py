# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-22 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0017_dex'),
    ]

    operations = [
        migrations.AddField(
            model_name='dex',
            name='eggs',
            field=models.ManyToManyField(blank=True, related_name='eggs', to='pokedex.Pokemon'),
        ),
        migrations.AlterField(
            model_name='dex',
            name='pokemon',
            field=models.ManyToManyField(blank=True, related_name='pokemon', to='pokedex.Pokemon'),
        ),
    ]
