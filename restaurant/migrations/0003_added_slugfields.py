# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_added_cover_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuisine',
            name='cuisine_slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='location_slug',
            field=models.SlugField(null=True),
        ),
    ]
