# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 11:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_remove_progress_person'),
        ('team', '0005_person_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='progress',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='tasks.Progress'),
        ),
    ]
