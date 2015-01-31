# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webms', '0005_webm_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webm',
            name='desc',
            field=models.CharField(default=b'no description', max_length=2048),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='webm',
            name='name',
            field=models.CharField(default=b'unnamed', max_length=256),
            preserve_default=True,
        ),
    ]
