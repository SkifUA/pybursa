# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addres',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_index', models.IntegerField(max_length=8, null=True, blank=True)),
                ('country', models.CharField(max_length=70)),
                ('region', models.CharField(max_length=80)),
                ('area', models.CharField(max_length=80, null=True, blank=True)),
                ('street', models.CharField(max_length=100)),
                ('build', models.CharField(max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
