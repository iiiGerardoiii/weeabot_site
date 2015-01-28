# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webms', '0004_webm_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='webm',
            name='thumbnail',
            field=models.CharField(default=b'missing.jpg', max_length=256),
            preserve_default=True,
        ),
    ]
