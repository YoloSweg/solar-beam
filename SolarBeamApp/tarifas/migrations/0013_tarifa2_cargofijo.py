# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 04:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarifas', '0012_auto_20170314_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarifa2',
            name='Cargofijo',
            field=models.FloatField(default=60),
        ),
    ]
