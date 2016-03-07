# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-06 11:24
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326),
        ),
    ]