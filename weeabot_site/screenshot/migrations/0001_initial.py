# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channel', models.CharField(max_length=128)),
                ('nick', models.CharField(max_length=128)),
                ('timestamp', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('url', models.CharField(max_length=2048)),
                ('filename', models.CharField(max_length=256)),
                ('name', models.CharField(default=b'unnamed', max_length=256)),
                ('desc', models.CharField(default=b'no description', max_length=2048)),
                ('thumbnail', models.CharField(default=b'missing.jpg', max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
