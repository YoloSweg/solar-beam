# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 06:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarifas', '0002_auto_20170309_0031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarifa1x',
            old_name='Abr',
            new_name='Basico',
        ),
        migrations.RenameField(
            model_name='tarifa1x',
            old_name='Ago',
            new_name='CBasico',
        ),
        migrations.RenameField(
            model_name='tarifa1x',
            old_name='Dic',
            new_name='CExcedente',
        ),
        migrations.RenameField(
            model_name='tarifa1x',
            old_name='Ene',
            new_name='CInter_Bajo',
        ),
        migrations.RenameField(
            model_name='tarifa1x',
            old_name='Feb',
            new_name='CInter_Medio',
        ),
        migrations.RenameField(
            model_name='tarifa1x',
            old_name='Jul',
            new_name='Excedente',
        ),
        migrations.RenameField(
            model_name='tarifa1x',
            old_name='Jun',
            new_name='Inter_Bajo',
        ),
        migrations.RenameField(
            model_name='tarifa1x',
            old_name='Mar',
            new_name='Inter_Medio',
        ),
        migrations.RemoveField(
            model_name='tarifa1x',
            name='May',
        ),
        migrations.RemoveField(
            model_name='tarifa1x',
            name='Nov',
        ),
        migrations.RemoveField(
            model_name='tarifa1x',
            name='Oct',
        ),
        migrations.RemoveField(
            model_name='tarifa1x',
            name='Sep',
        ),
    ]
