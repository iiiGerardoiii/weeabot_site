# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jisho', '0002_auto_20150119_0611'),
    ]

    operations = [
        migrations.AddField(
            model_name='definition',
            name='kana',
            field=models.CharField(default=b'', max_length=64),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='definition',
            name='kanji',
            field=models.CharField(default=b'', max_length=32),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='definition',
            name='romaji',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
    ]
