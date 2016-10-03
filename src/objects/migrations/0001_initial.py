# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-03 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=128, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=256)),
                ('url', models.URLField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ObjectByIdentifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(default=uuid.uuid4, max_length=128)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.Object')),
            ],
        ),
    ]
