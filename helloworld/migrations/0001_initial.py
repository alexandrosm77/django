# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-16 18:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('uuid', models.CharField(default=b'fbdb1091-db13-4e98-9b82-bb4cee9da2a4', editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'task',
            },
        ),
    ]
