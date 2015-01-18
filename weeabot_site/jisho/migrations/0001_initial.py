# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Definition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channel', models.CharField(max_length=128)),
                ('nick', models.CharField(max_length=128)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name=b'date published')),
                ('url', models.CharField(max_length=2048)),
                ('text', models.CharField(max_length=256)),
                ('word', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
