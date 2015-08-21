# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cuisine_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('restaurant_photo', models.ImageField(upload_to=b'/home/pratik/samosameetschai/smc/media/')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('menu_image', models.ImageField(upload_to=b'/home/pratik/samosameetschai/smc/media/')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('full_name', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('full_address', models.CharField(max_length=255)),
                ('contact', models.IntegerField()),
                ('website', models.CharField(max_length=200, null=True, blank=True)),
                ('name_slug', models.SlugField()),
                ('opening_hours', models.CharField(max_length=50, null=True, blank=True)),
                ('additional_info', models.CharField(max_length=200, null=True, blank=True)),
                ('history', models.TextField(null=True)),
                ('serves_alcohol', models.BooleanField(default=False)),
                ('non_veg', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=True)),
                ('air_conditioned', models.BooleanField(default=False)),
                ('out_seating', models.BooleanField(default=False)),
                ('delivery', models.BooleanField(default=False)),
                ('reservation', models.BooleanField(default=False)),
                ('catering', models.BooleanField(default=False)),
                ('cost_for_two', models.IntegerField(null=True)),
                ('geolocation', geoposition.fields.GeopositionField(max_length=42)),
                ('cuisines', models.ManyToManyField(to='restaurant.Cuisine')),
                ('location', models.ManyToManyField(to='restaurant.Location')),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('restaurant_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='rest_type',
            field=models.ManyToManyField(to='restaurant.RestaurantType'),
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_name',
            field=models.ForeignKey(related_name='menu', to='restaurant.Restaurant'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='restaurant_photo_name',
            field=models.ForeignKey(related_name='gallery', to='restaurant.Restaurant'),
        ),
    ]
