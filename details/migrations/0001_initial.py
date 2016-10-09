# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 05:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.TextField(default='')),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='swag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.TextField(default='')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.details')),
            ],
        ),
    ]
