# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kofiapp', '0006_coffeepic_processed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeepic',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date_uploaded'),
        ),
    ]
