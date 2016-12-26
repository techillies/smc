# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_restaurant_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='id',
        ),
        migrations.AlterField(
            model_name='gallery',
            name='restaurant_photo',
            field=models.ImageField(upload_to=b'C:\\Users\\Soumya\\Desktop\\smc\\smc\\media/'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu_image',
            field=models.ImageField(upload_to=b'C:\\Users\\Soumya\\Desktop\\smc\\smc\\media/'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='cover_photo',
            field=models.ImageField(null=True, upload_to=b'C:\\Users\\Soumya\\Desktop\\smc\\smc\\media/'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name_slug',
            field=models.SlugField(primary_key=True, serialize=False),
        ),
    ]
