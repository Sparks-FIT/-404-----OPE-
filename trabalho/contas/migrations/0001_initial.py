# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 22:42
from __future__ import unicode_literals

import contas.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('ra', models.IntegerField(unique=True, verbose_name='RA')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-Mail')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('perfil', models.CharField(choices=[('A', 'Aluno'), ('P', 'Professor')], max_length=1, verbose_name='Perfil')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', contas.models.UsuarioManager()),
            ],
        ),
    ]
