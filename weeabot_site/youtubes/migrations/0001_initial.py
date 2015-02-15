# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=2048)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channel', models.CharField(max_length=128)),
                ('nick', models.CharField(max_length=128)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(max_length=2048)),
                ('name', models.CharField(default=b'', max_length=256)),
                ('desc', models.CharField(default=b'no description', max_length=2048)),
                ('thumbnail', models.CharField(default=b'missing.jpg', max_length=256)),
                ('updated', models.DateTimeField(default=datetime.datetime(2015, 2, 14, 13, 38, 1, 195421), auto_now=True)),
                ('hits', models.IntegerField(default=1)),
                ('tags', models.ManyToManyField(related_name='webms', to='youtubes.Tag', blank=True)),
            ],
            options={
                'ordering': ['-updated'],
            },
            bases=(models.Model,),
        ),
    ]
