# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='cover_photo',
            field=models.ImageField(null=True, upload_to=b'/home/pratik/samosameetschai/smc/media/'),
        ),
    ]
