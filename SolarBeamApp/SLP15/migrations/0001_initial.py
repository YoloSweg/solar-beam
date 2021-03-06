# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Central',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('central', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Centrales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cen', models.TextField(blank=True, null=True)),
                ('central', models.IntegerField(blank=True, null=True)),
                ('capapl', models.IntegerField(blank=True, null=True)),
                ('zpcen', models.IntegerField(blank=True, null=True)),
                ('zgcen', models.IntegerField(blank=True, null=True)),
                ('zprcen', models.IntegerField(blank=True, null=True)),
                ('zicen', models.IntegerField(blank=True, null=True)),
                ('gen', models.IntegerField(blank=True, null=True)),
                ('prelacion', models.IntegerField(blank=True, null=True)),
                ('zpcen2', models.TextField(blank=True, null=True)),
                ('zgcen2', models.TextField(blank=True, null=True)),
                ('zprcen2', models.TextField(blank=True, null=True)),
                ('zicen2', models.TextField(blank=True, null=True)),
                ('cent_acept', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CentralOv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gen', models.IntegerField(blank=True, null=True)),
                ('paquetes', models.IntegerField(blank=True, null=True)),
                ('central', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conpaqexc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conpaqexc', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Erc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('erc', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gen', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nodoof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sistemainter', models.IntegerField(blank=True, null=True)),
                ('zona', models.IntegerField(blank=True, null=True)),
                ('region', models.IntegerField(blank=True, null=True)),
                ('nodo', models.IntegerField(blank=True, null=True)),
                ('limpotn', models.IntegerField(blank=True, null=True)),
                ('nombrenodo', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ofererc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dpot', models.IntegerField(blank=True, null=True)),
                ('ppot', models.IntegerField(blank=True, null=True)),
                ('deea', models.IntegerField(blank=True, null=True)),
                ('peea', models.IntegerField(blank=True, null=True)),
                ('dcel', models.IntegerField(blank=True, null=True)),
                ('pcel', models.IntegerField(blank=True, null=True)),
                ('fechairrantp', models.IntegerField(blank=True, null=True)),
                ('fechairrdespp', models.IntegerField(blank=True, null=True)),
                ('fechairrante', models.IntegerField(blank=True, null=True)),
                ('fechairrdespe', models.IntegerField(blank=True, null=True)),
                ('fechairrantc', models.IntegerField(blank=True, null=True)),
                ('fechairrdespc', models.IntegerField(blank=True, null=True)),
                ('erc', models.IntegerField(blank=True, null=True)),
                ('ofertas', models.IntegerField(blank=True, null=True)),
                ('zpoterc', models.IntegerField(blank=True, null=True)),
                ('sinterc', models.IntegerField(blank=True, null=True)),
                ('rinerc', models.IntegerField(blank=True, null=True)),
                ('potajus', models.FloatField(blank=True, null=True)),
                ('eeaajus', models.IntegerField(blank=True, null=True)),
                ('celajus', models.IntegerField(blank=True, null=True)),
                ('ejecucion', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ofertas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ofertas', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paqexc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gen', models.IntegerField(blank=True, null=True)),
                ('conpaqexc', models.IntegerField(blank=True, null=True)),
                ('paquetes', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paqgen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paquetes', models.IntegerField(blank=True, null=True)),
                ('gen', models.IntegerField(blank=True, null=True)),
                ('capapl', models.IntegerField(blank=True, null=True)),
                ('gpot', models.IntegerField(blank=True, null=True)),
                ('geea', models.IntegerField(blank=True, null=True)),
                ('gcel', models.IntegerField(blank=True, null=True)),
                ('ppaq', models.FloatField(blank=True, null=True)),
                ('firrant', models.IntegerField(blank=True, null=True)),
                ('firrdes', models.IntegerField(blank=True, null=True)),
                ('sint', models.IntegerField(blank=True, null=True)),
                ('zonin', models.IntegerField(blank=True, null=True)),
                ('rin', models.IntegerField(blank=True, null=True)),
                ('nin', models.IntegerField(blank=True, null=True)),
                ('prelacion', models.IntegerField(blank=True, null=True)),
                ('factordevesp', models.FloatField(blank=True, null=True)),
                ('pct20', models.FloatField(blank=True, null=True)),
                ('vpnindexdls', models.FloatField(blank=True, null=True)),
                ('vpnindexpesos', models.FloatField(blank=True, null=True)),
                ('indexusd', models.IntegerField(blank=True, null=True)),
                ('idejec', models.IntegerField(blank=True, null=True)),
                ('nppaq', models.FloatField(blank=True, null=True)),
                ('ev_ppajus', models.IntegerField(blank=True, null=True)),
                ('ev_pporig', models.IntegerField(blank=True, null=True)),
                ('aceptado', models.IntegerField(blank=True, null=True)),
                ('nin2', models.BigIntegerField(blank=True, null=True)),
                ('rin2', models.BigIntegerField(blank=True, null=True)),
                ('zonin2', models.BigIntegerField(blank=True, null=True)),
                ('sint2', models.BigIntegerField(blank=True, null=True)),
                ('zongenf', models.IntegerField(blank=True, null=True)),
                ('fechaap', models.TextField(blank=True, null=True)),
                ('fechaen', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paqin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gen', models.IntegerField(blank=True, null=True)),
                ('paquetes', models.IntegerField(blank=True, null=True)),
                ('paquetes2', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paquetes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paquetes', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paquetes2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paquetes2', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Regionof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sistemainter', models.IntegerField(blank=True, null=True)),
                ('zona', models.IntegerField(blank=True, null=True)),
                ('region', models.IntegerField(blank=True, null=True)),
                ('nombrereg', models.TextField(blank=True, null=True)),
                ('limpot', models.IntegerField(blank=True, null=True)),
                ('pml', models.FloatField(blank=True, null=True)),
                ('id_region', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sistemainter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sistemainter', models.IntegerField(blank=True, null=True)),
                ('nombresi', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zonaof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zona', models.IntegerField(blank=True, null=True)),
                ('sistemainter', models.IntegerField(blank=True, null=True)),
                ('nombrezon', models.TextField(blank=True, null=True)),
                ('limpote', models.IntegerField(blank=True, null=True)),
                ('limeeae', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
