# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kofiapp', '0004_coffeepic_processed_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffeepic',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]