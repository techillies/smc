# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_restaurant_name_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='additional_info',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='air_conditioned',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='catering',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='delivery',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='history',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='opening_hours',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='out_seating',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='reservation',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
