# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


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
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('full_name', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('full_address', models.CharField(max_length=255)),
                ('contact', models.IntegerField(max_length=20)),
                ('website', models.CharField(max_length=200, null=True)),
                ('serves_alcohol', models.BooleanField(default=False)),
                ('non_veg', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=True)),
                ('cuisines', models.ManyToManyField(to='restaurant.Cuisine')),
                ('location', models.ManyToManyField(to='restaurant.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
