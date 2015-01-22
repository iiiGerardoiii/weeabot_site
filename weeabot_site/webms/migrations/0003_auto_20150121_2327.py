# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webms', '0002_tag_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='entires',
        ),
        migrations.AddField(
            model_name='webm',
            name='tags',
            field=models.ManyToManyField(related_name='webms', to='webms.Tag', blank=True),
            preserve_default=True,
        ),
    ]
