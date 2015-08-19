# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20150110_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='name_slug',
            field=models.SlugField(default='manishas'),
            preserve_default=False,
        ),
    ]
