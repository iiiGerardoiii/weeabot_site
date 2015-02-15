# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('youtubes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtube',
            name='tags',
            field=models.ManyToManyField(related_name='youtubes', to='youtubes.Tag', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='youtube',
            name='thumbnail',
            field=models.CharField(default=b'missing.jpg', max_length=1024),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='youtube',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 14, 15, 23, 26, 700655), auto_now=True),
            preserve_default=True,
        ),
    ]
