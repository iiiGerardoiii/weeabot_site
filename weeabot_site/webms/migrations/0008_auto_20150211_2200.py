# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('webms', '0007_auto_20150211_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webm',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='webm',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 11, 22, 0, 32, 409216), auto_now=True),
            preserve_default=True,
        ),
    ]
