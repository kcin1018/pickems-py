# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 05:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial_models'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamWinLoss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wl', models.DecimalField(decimal_places=3, max_digits=4)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Team')),
            ],
        ),
    ]
