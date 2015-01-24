# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webms', '0003_auto_20150121_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='webm',
            name='name',
            field=models.CharField(default='Ayy Lmao', max_length=256),
            preserve_default=False,
        ),
    ]
