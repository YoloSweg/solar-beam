# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 20:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarifas', '0016_dac_anio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dac',
            name='Anio',
        ),
    ]
