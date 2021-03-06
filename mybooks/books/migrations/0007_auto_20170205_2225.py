# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 19:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20170205_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='number_of_pages',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Publisher'),
        ),
    ]
