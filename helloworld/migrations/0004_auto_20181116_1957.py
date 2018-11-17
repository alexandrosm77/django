# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-16 19:57
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0003_auto_20181116_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]