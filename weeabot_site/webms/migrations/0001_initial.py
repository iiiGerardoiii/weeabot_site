# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Webm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channel', models.CharField(max_length=128)),
                ('nick', models.CharField(max_length=128)),
                ('timestamp', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('url', models.CharField(max_length=2048)),
                ('filename', models.CharField(max_length=256)),
                ('filehash', models.CharField(max_length=128)),
                ('desc', models.CharField(max_length=2048)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tag',
            name='entires',
            field=models.ManyToManyField(related_name='webms', to='webms.Webm', blank=True),
            preserve_default=True,
        ),
    ]
