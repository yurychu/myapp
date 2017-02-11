# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20170205_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='present',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='book',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='book_covers'),
        ),
    ]
