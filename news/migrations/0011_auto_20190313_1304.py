# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-13 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20190313_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, upload_to='articles/'),
        ),
    ]
